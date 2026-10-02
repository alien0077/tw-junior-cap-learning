/* Performance-unit semantic aliases.
   Reuse the visual grammar of the matching content concept instead of generic reasoning cards. */
(()=>{const r=window.MathSemanticFamilies ||= {};
const aliases={
 "performance-d-iv-1-reasoning-v1":"d-7-2-center-outlier-v1",
 "performance-g-iv-2-reasoning-v1":"a-7-6-system-graph-v1",
 "performance-g-iv-1-reasoning-v1":"g-8-1-distance-triangle-v1",
 "performance-f-iv-3-reasoning-v1":"f-9-2-parabola-vertex-v1",
 "performance-f-iv-2-reasoning-v1":"f-9-1-quadratic-meaning-v1",
 "performance-f-iv-1-reasoning-v1":"f-8-1-linear-two-point-v1",
 "performance-a-iv-4-reasoning-v1":"a-7-6-system-graph-v1",
 "performance-a-iv-3-reasoning-v1":"a-7-8-inequality-range-v1",
 "performance-a-iv-2-reasoning-v1":"a-7-3-balance-equation-v1",
 "performance-a-iv-1-reasoning-v1":"a-7-1-like-terms-v1",
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
r["performance-d-iv-2-reasoning-v1"]=host=>{host.innerHTML="";const root=document.createElement("section");root.className="mdf-root";root.innerHTML='<header><p class="mdf-kicker">分支 → 路徑 → 機率</p><h3>樹狀圖：每一步都沿分支乘，互斥路徑再相加</h3><p>兩次公平擲硬幣共有 HH、HT、TH、TT 四條等可能路徑。</p></header><label class="mdf-control"><span>事件</span><select data-sim-control="div2Event"><option value="one">恰一個正面</option><option value="two">兩個正面</option><option value="atleast">至少一個正面</option></select></label><div class="mdf-grid" role="img" aria-label="兩次擲硬幣的四條樹狀圖路徑"><span>H→H</span><span>H→T</span><span>T→H</span><span>T→T</span></div><p class="mdf-evidence" aria-live="polite"></p>';host.append(root);const s=root.querySelector("select"),g=root.querySelector(".mdf-grid"),e=root.querySelector(".mdf-evidence");const draw=()=>{const paths=[...g.children];paths.forEach(x=>x.classList.remove("hit"));let ids=[];if(s.value==="one")ids=[1,2];if(s.value==="two")ids=[0];if(s.value==="atleast")ids=[0,1,2];ids.forEach(i=>paths[i].classList.add("hit"));e.textContent="每條完整路徑機率 1/2×1/2=1/4；符合事件 "+ids.length+" 條，所以總機率 "+ids.length+"/4。不同完整路徑互斥，才把它們相加。";};s.addEventListener("change",draw);draw();};
})();