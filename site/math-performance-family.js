/* Performance-unit semantic aliases.
   Reuse the visual grammar of the matching content concept instead of generic reasoning cards. */
(()=>{const r=window.MathSemanticFamilies ||= {};
const aliases={
 "performance-n-iv-1-reasoning-v1":"n-7-2-factor-tree-v1",
 "performance-n-iv-2-reasoning-v1":"n-7-5-signed-number-line-v1",
 "performance-n-iv-3-reasoning-v1":"n-7-7-scientific-place-value-v1",
 "performance-n-iv-4-reasoning-v1":"n-7-8-ratio-table-v1",
 "performance-n-iv-5-reasoning-v1":"n-8-1-square-root-bracket-v1",
 "performance-n-iv-6-reasoning-v1":"n-8-2-root-number-line-v1",
 "performance-n-iv-7-reasoning-v1":"n-9-1-sequence-v1",
 "performance-n-iv-8-reasoning-v1":"n-9-1-series-v1"
};
for(const [target,source] of Object.entries(aliases)) if(typeof r[source]==="function") r[target]=r[source];
r["performance-n-iv-9-reasoning-v1"]=host=>{host.innerHTML="";const root=document.createElement("section");root.className="mnf-root";root.innerHTML='<header><p class="mnf-kicker">近似值 → 誤差 → 精度</p><h3>誤差不是「錯了多少位」</h3><p>同一真值用不同位數近似，直接比較絕對誤差。</p></header><label class="mnf-control"><span>近似方式</span><select data-sim-control="niv9Approx"><option value="3.1">3.1</option><option value="3.14">3.14</option><option value="3.142">3.142</option></select></label><div class="mnf-place" role="img" aria-label="圓周率真值與近似值誤差比較"></div><p class="mnf-evidence" aria-live="polite"></p><article class="mnf-card"><strong>遷移</strong><span>測量 12.4 cm 若記到小數第一位，解讀時要保留測量精度，不能假裝知道更多位數。</span></article>';host.append(root);const s=root.querySelector("select"),g=root.querySelector(".mnf-place"),e=root.querySelector(".mnf-evidence");const draw=()=>{const a=+s.value,truth=Math.PI,err=Math.abs(truth-a);g.innerHTML='<article class="mnf-card"><strong>參考真值</strong><span>π≈3.14159265</span></article><article class="mnf-card"><strong>近似值</strong><span>'+a+'</span></article><article class="mnf-card"><strong>絕對誤差</strong><span>'+err.toFixed(6)+'</span></article>';e.textContent="絕對誤差 = |真值−近似值|。多寫位數通常能減小誤差，但不能把近似值當成完全精確。";};s.addEventListener("change",draw);draw();};
})();