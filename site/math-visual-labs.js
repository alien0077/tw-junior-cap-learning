/* Visual-first math renderers. Concept-specific; no generic balance fallback. */
(() => {
  const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
  const selected = (a,b) => Number(a) === Number(b) ? " selected" : "";
  const select = (key,label,value,options) =>
    '<label class="mvl-control"><span>'+esc(label)+'</span><select data-sim-control="'+esc(key)+'" aria-label="'+esc(label)+'">'+
    options.map(o => '<option value="'+o[0]+'"'+selected(value,o[0])+'>'+esc(o[1])+'</option>').join("")+'</select></label>';
  const range = (key,label,value,min,max) =>
    '<label class="mvl-control"><span>'+esc(label)+' <output>'+esc(value)+'</output></span><input data-sim-control="'+esc(key)+'" type="range" min="'+min+'" max="'+max+'" step="1" value="'+esc(value)+'" aria-label="'+esc(label)+'"></label>';

  const areaSvgPlus = (a,b,reveal) => {
    const total=a+b, size=260, x=48, y=38, aPx=size*a/total, bPx=size*b/total;
    const labels = reveal
      ? '<text x="'+(x+aPx/2)+'" y="'+(y+aPx/2)+'" class="mvl-region-label">a²</text>'+
        '<text x="'+(x+aPx+bPx/2)+'" y="'+(y+aPx/2)+'" class="mvl-region-label">ab</text>'+
        '<text x="'+(x+aPx/2)+'" y="'+(y+aPx+bPx/2)+'" class="mvl-region-label">ab</text>'+
        '<text x="'+(x+aPx+bPx/2)+'" y="'+(y+aPx+bPx/2)+'" class="mvl-region-label">b²</text>'
      : '<text x="178" y="176" class="mvl-question">先預測四塊面積</text>';
    return '<svg viewBox="0 0 356 344" role="img" aria-label="邊長 a 加 b 的正方形面積分割">'+
      '<rect x="'+x+'" y="'+y+'" width="'+size+'" height="'+size+'" class="mvl-outline"/>'+
      '<rect x="'+x+'" y="'+y+'" width="'+aPx+'" height="'+aPx+'" class="mvl-a2"/>'+
      '<rect x="'+(x+aPx)+'" y="'+y+'" width="'+bPx+'" height="'+aPx+'" class="mvl-ab"/>'+
      '<rect x="'+x+'" y="'+(y+aPx)+'" width="'+aPx+'" height="'+bPx+'" class="mvl-ab mvl-hatch"/>'+
      '<rect x="'+(x+aPx)+'" y="'+(y+aPx)+'" width="'+bPx+'" height="'+bPx+'" class="mvl-b2"/>'+
      '<line x1="'+(x+aPx)+'" y1="'+y+'" x2="'+(x+aPx)+'" y2="'+(y+size)+'" class="mvl-split"/>'+
      '<line x1="'+x+'" y1="'+(y+aPx)+'" x2="'+(x+size)+'" y2="'+(y+aPx)+'" class="mvl-split"/>'+
      '<text x="'+(x+aPx/2)+'" y="24" class="mvl-dim">a = '+a+'</text><text x="'+(x+aPx+bPx/2)+'" y="24" class="mvl-dim">b = '+b+'</text>'+
      '<text x="18" y="'+(y+aPx/2)+'" class="mvl-dim">a</text><text x="18" y="'+(y+aPx+bPx/2)+'" class="mvl-dim">b</text>'+
      labels+'</svg>';
  };

  const areaSvgMinus = (a,b,reveal) => {
    const size=260,x=48,y=38, inner=size*(a-b)/a, cut=size*b/a;
    return '<svg viewBox="0 0 356 344" role="img" aria-label="由 a 乘 a 正方形扣除兩條寬 b 的長方形並補回重複角落">'+
      '<rect x="'+x+'" y="'+y+'" width="'+size+'" height="'+size+'" class="mvl-a2"/>'+
      '<rect x="'+(x+inner)+'" y="'+y+'" width="'+cut+'" height="'+size+'" class="mvl-remove"/>'+
      '<rect x="'+x+'" y="'+(y+inner)+'" width="'+size+'" height="'+cut+'" class="mvl-remove mvl-hatch"/>'+
      '<rect x="'+(x+inner)+'" y="'+(y+inner)+'" width="'+cut+'" height="'+cut+'" class="mvl-addback"/>'+
      '<rect x="'+x+'" y="'+y+'" width="'+inner+'" height="'+inner+'" class="mvl-result-square"/>'+
      (reveal ? '<text x="'+(x+inner/2)+'" y="'+(y+inner/2)+'" class="mvl-region-label">(a−b)²</text><text x="'+(x+inner+cut/2)+'" y="'+(y+inner/2)+'" class="mvl-region-label">−ab</text><text x="'+(x+inner/2)+'" y="'+(y+inner+cut/2)+'" class="mvl-region-label">−ab</text><text x="'+(x+inner+cut/2)+'" y="'+(y+inner+cut/2)+'" class="mvl-region-label">+b²</text>' : '<text x="178" y="176" class="mvl-question">哪一角被重複扣掉？</text>')+
      '<text x="178" y="24" class="mvl-dim">a = '+a+'，b = '+b+'</text></svg>';
  };

  const areaSvgDiff = (a,b,reveal) => {
    const scale=220/a, big=a*scale, small=b*scale, x=28,y=54;
    return '<svg viewBox="0 0 356 300" role="img" aria-label="大正方形 a 平方扣掉小正方形 b 平方，重排為邊長 a 加 b 與 a 減 b 的長方形">'+
      '<rect x="'+x+'" y="'+y+'" width="'+big+'" height="'+big+'" class="mvl-a2"/>'+
      '<rect x="'+(x+big-small)+'" y="'+(y+big-small)+'" width="'+small+'" height="'+small+'" class="mvl-b2 mvl-cutout"/>'+
      '<path d="M'+(x+big-small)+' '+y+' L'+(x+big-small)+' '+(y+big-small)+' L'+x+' '+(y+big-small)+'" class="mvl-cut-line"/>'+
      (reveal ? '<text x="'+(x+big/2)+'" y="'+(y+big/2-16)+'" class="mvl-region-label">a² − b²</text><text x="'+(x+big/2)+'" y="'+(y+big+30)+'" class="mvl-dim">重排後：長 (a+b)，寬 (a−b)</text>' : '<text x="178" y="170" class="mvl-question">交叉區會保留還是相消？</text>')+
      '<text x="178" y="28" class="mvl-dim">a = '+a+'，b = '+b+'</text></svg>';
  };

  const renderArea = (lesson,state) => {
    const a=Math.max(3,Number(state.a||4)), b=Math.max(1,Math.min(a-1,Number(state.b||2)));
    const mode=Number(state.formulaMode||0), prediction=Number(state.prediction||0), reveal=prediction>0;
    const modeNames=["(a+b)²","(a−b)²","(a+b)(a−b)"];
    const correct=[2,2,1][mode];
    const formula=[
      '(a+b)² = a² + ab + ab + b² = a² + 2ab + b²',
      '(a−b)² = a² − ab − ab + b² = a² − 2ab + b²',
      '(a+b)(a−b) = a² − ab + ab − b² = a² − b²'
    ][mode];
    const numeric=[
      '('+(a+b)+')² = '+((a+b)*(a+b))+'；'+(a*a)+' + '+(2*a*b)+' + '+(b*b)+' = '+((a+b)*(a+b)),
      '('+(a-b)+')² = '+((a-b)*(a-b))+'；'+(a*a)+' − '+(2*a*b)+' + '+(b*b)+' = '+((a-b)*(a-b)),
      (a+b)+'×'+(a-b)+' = '+((a+b)*(a-b))+'；'+(a*a)+' − '+(b*b)+' = '+((a+b)*(a-b))
    ][mode];
    const svg = mode===0 ? areaSvgPlus(a,b,reveal) : mode===1 ? areaSvgMinus(a,b,reveal) : areaSvgDiff(a,b,reveal);
    const feedback = !prediction ? '先選一個預測；圖上的結論與公式會保持隱藏。'
      : prediction===correct ? '預測吻合。請用圖中的區塊數量或相消位置說明，不要只背公式。'
      : mode===2 ? '再看兩個交叉乘積：−ab 與 +ab 大小相同、符號相反。'
      : '再數一次交叉區：有兩個長寬分別為 a、b 的區塊。';
    const transferA=Math.max(4,Number(state.transferA||5)), transferB=Math.max(1,Math.min(transferA-1,Number(state.transferB||1)));
    const transferPred=Number(state.transferPrediction||0);
    const transferExpected=(transferA+transferB)*(transferA+transferB);
    const transferFeedback=!transferPred?'換一組數字，再預測新正方形總面積。':transferPred===transferExpected?'正確。你把同一個關係帶到新數值，而不是記住原本的 4、2。':'再把四塊面積相加：a²、ab、ab、b²。';
    return '<section class="mvl mvl-area" aria-label="乘法公式面積模型">'+
      '<div class="mvl-task"><span class="mvl-step">1 預測</span><strong>'+esc(modeNames[mode])+' 的交叉區會怎麼變？</strong><p>先看圖形，不先看公式。</p></div>'+
      '<div class="mvl-layout"><figure class="mvl-visual">'+svg+'<figcaption>'+esc(reveal ? numeric : '公式暫時隱藏；先做預測。')+'</figcaption></figure>'+
      '<div class="mvl-panel">'+
      select('formulaMode','探索模式',mode,[[0,'和的平方'],[1,'差的平方'],[2,'平方差']])+
      range('a','a',a,3,8)+range('b','b',b,1,Math.max(1,a-1))+
      select('prediction','你的預測',prediction,[[0,'先不揭曉'],[1,'交叉項會相消'],[2,'會出現兩個交叉區']])+
      '<p class="mvl-feedback" aria-live="polite">'+esc(feedback)+'</p>'+
      (reveal?'<div class="mvl-equation" aria-label="公式證據"><span>圖形 → 符號</span><strong>'+esc(formula)+'</strong></div>':'')+
      '</div></div>'+
      '<div class="mvl-transfer"><span class="mvl-step">2 遷移</span><strong>換數字，不換概念</strong><div class="mvl-transfer-controls">'+
      range('transferA','新 a',transferA,4,9)+range('transferB','新 b',transferB,1,Math.max(1,transferA-1))+
      select('transferPrediction','預測 (a+b)²',transferPred,[[0,'選答案'],[transferExpected,' '+transferExpected],[transferExpected+transferB,' '+(transferExpected+transferB)],[transferA*transferA+transferB*transferB,' '+(transferA*transferA+transferB*transferB)]])+
      '</div><p class="mvl-feedback" aria-live="polite">'+esc(transferFeedback)+'</p></div>'+
      '<details class="mvl-evidence"><summary>我要看推理提示</summary><p>平方和：數兩個 ab。差平方：追蹤兩條被扣除的長方形與重複扣掉的 b²。平方差：追蹤 −ab 與 +ab 如何相消。</p></details>'+
      '</section>';
  };

  const factorRow = (title,tokens,common) =>
    '<div class="mvl-factor-row"><strong>'+esc(title)+'</strong><div class="mvl-token-row">'+tokens.map((t,i)=>'<span class="mvl-token '+(common.includes(i)?'is-common':'')+'">'+esc(t)+'</span>').join("")+'</div></div>';

  const renderFactor = (lesson,state) => {
    const model=lesson.simulation.model;
    const broad=model==='a-8-5-factorization-v1';
    const candidate=Number(state.commonFactor||0);
    const correct=2;
    const candidateText={0:'尚未選擇',1:'6',2:'6x',3:'12x'}[candidate]||'尚未選擇';
    const feedback=!candidate?'先比較兩列：只把「兩列都有」的因子圈起來。':candidate===correct?'正確：共同的數字因子是 2×3，共同字母至少有一個 x，所以最大共同因式是 6x。':candidate===1?'6 雖能整除係數，但兩項還共同含有 x；還沒提出完整。':'12x 不能整除 18x 成整式係數；逐項相除就會暴露問題。';
    const transfer=Number(state.factorTransfer||0);
    const transferFeedback=!transfer?'再做一次：15x²y 與 −10xy² 的共同部分是什麼？':transfer===3?'正確：係數共同 5，x 與 y 都取共同最低次方 1，所以是 5xy。':'把兩項的係數、x、y 分三欄比較；每一欄都只能取兩項共有的部分。';
    return '<section class="mvl mvl-factor" aria-label="因式分解共同因子視覺模型">'+
      '<div class="mvl-task"><span class="mvl-step">1 看共同材料</span><strong>12x² + 18x 可以先拿出什麼？</strong><p>不是先加括號，而是找兩項真正共有的因子。</p></div>'+
      '<div class="mvl-factor-board">'+
      factorRow('12x²',['2','2','3','x','x'],[0,2,3])+
      factorRow('18x',['2','3','3','x'],[0,1,3])+
      '<div class="mvl-common-strip"><span>兩列共同</span><b>2 × 3 × x = 6x</b></div></div>'+
      '<div class="mvl-factor-controls">'+
      select('commonFactor','先預測最大共同因式',candidate,[[0,'選一個'],[1,'6'],[2,'6x'],[3,'12x']])+
      '<p class="mvl-feedback" aria-live="polite">'+esc(feedback)+'</p>'+
      (candidate?'<div class="mvl-equation"><span>逐項相除檢查</span><strong>12x² ÷ '+esc(candidateText)+'；18x ÷ '+esc(candidateText)+'</strong>'+(candidate===correct?'<p>12x² + 18x = 6x(2x + 3) → 展開回原式。</p>':'')+'</div>':'')+
      '</div>'+
      (broad?'<div class="mvl-method-map"><span class="mvl-step">2 重新判斷剩式</span><div class="mvl-method-grid"><article><b>有共同因式</b><p>先提出，再看括號內。</p></article><article><b>兩平方相減</b><p>A²−B² → (A−B)(A+B)</p></article><article><b>三項式</b><p>同時檢查乘積與交叉和。</p></article></div></div>':'')+
      '<div class="mvl-transfer"><span class="mvl-step">3 遷移</span><strong>15x²y − 10xy²</strong>'+
      select('factorTransfer','最大共同因式',transfer,[[0,'選一個'],[1,'5'],[2,'5x'],[3,'5xy']])+
      '<p class="mvl-feedback" aria-live="polite">'+esc(transferFeedback)+'</p>'+
      (transfer===3?'<div class="mvl-equation"><strong>15x²y − 10xy² = 5xy(3x − 2y)</strong><p>回乘：5xy·3x − 5xy·2y = 15x²y − 10xy²。</p></div>':'')+
      '</div><details class="mvl-evidence"><summary>為什麼不是只背最大公因數？</summary><p>因式分解是分配律的反向操作。候選共同因式必須逐項相除得到整式，最後再乘回原式；三個步驟都能檢查。</p></details></section>';
  };

  const supports = (engine,model) => engine==='math-visual-area' || engine==='math-factor-model';
  const defaults = (engine,model) => engine==='math-visual-area'
    ? {a:4,b:2,formulaMode:0,prediction:0,transferA:5,transferB:1,transferPrediction:0}
    : {commonFactor:0,factorTransfer:0};
  const label = engine => engine==='math-visual-area' ? '面積公式探索臺' : '因式結構探索臺';
  const render = (lesson,state) => lesson.simulation.engine==='math-visual-area' ? renderArea(lesson,state) : renderFactor(lesson,state);
  window.MathVisualLabs={supports,defaults,label,render};
})();