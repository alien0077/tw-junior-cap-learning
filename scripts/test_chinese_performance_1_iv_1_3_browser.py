#!/usr/bin/env python3
import argparse,asyncio,json
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
IDS=["lesson-chinese-performance-1-iv-1","lesson-chinese-performance-1-iv-2","lesson-chinese-performance-1-iv-3"]
async def run(url):
 errors=[]
 async with async_playwright() as p:
  b=await p.chromium.launch(headless=True);page=await b.new_page(viewport={"width":375,"height":1100},reduced_motion="reduce");page.on("pageerror",lambda e:errors.append(str(e)))
  await page.goto(url,wait_until="networkidle",timeout=60000);await page.get_by_role("status").filter(has_text="資料載入完成").wait_for(timeout=30000)
  results=[]
  for lesson_id in IDS:
   await page.locator("#search").fill(lesson_id);lab=page.locator(f'.chinese-manipulation-lab[data-lesson="{lesson_id}"]');await lab.wait_for(timeout=30000)
   first=lab.locator(".cml-card").first;await first.focus();await page.keyboard.press("Enter");zone=lab.locator(".cml-zone").first;await zone.focus();await page.keyboard.press("Enter")
   assert "關係成立" in await lab.locator(".cml-map").inner_text()
   inp=lab.locator("[data-explain]");await inp.fill("因為材料與問題的證據相符，所以先建立連結，但仍要檢查限制。");await lab.locator("[data-check]").click();assert "已記錄解釋" in await lab.locator("[data-feedback]").inner_text()
   if lesson_id.endswith("1-iv-2"):
    slider=lab.locator('[data-prosody="rate"]');await slider.fill("120");assert "120%" in await lab.locator("[data-prosody-view]").inner_text();await lab.locator('[data-stress="準時"]').click();assert "重音焦點" in await lab.locator("[data-prosody-view]").inner_text()
   await page.add_script_tag(content=(ROOT/"node_modules/axe-core/axe.min.js").read_text())
   axe=await page.evaluate("async el=>(await axe.run(el,{resultTypes:['violations']})).violations",await lab.element_handle());assert not axe,axe
   for width in (320,375,768):
    await page.set_viewport_size({"width":width,"height":1100});size=await page.evaluate("({v:innerWidth,s:document.documentElement.scrollWidth})");assert size["s"]<=size["v"],size
   results.append({"lesson":lesson_id,"interaction":True,"axeViolations":0})
  assert not errors,errors;await b.close();return {"status":"passed","results":results,"pageErrors":errors}
def main():
 a=argparse.ArgumentParser();a.add_argument("--url",default="http://127.0.0.1:8765/site/index.html");x=a.parse_args();print(json.dumps(asyncio.run(run(x.url)),ensure_ascii=False))
if __name__=="__main__":main()
