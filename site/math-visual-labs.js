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

  const quadraticRectSvg = (w,d,reveal) => {
    const scale=20, width=Math.max(60,w*scale), height=Math.max(52,(w+d)*scale*0.62), x=38,y=42;
    return '<svg viewBox="0 0 356 260" role="img" aria-label="寬 '+w+'、長 '+(w+d)+' 的長方形面積模型">'+
      '<rect x="'+x+'" y="'+y+'" width="'+Math.min(260,width)+'" height="'+Math.min(150,height)+'" class="mvl-q-rect"/>'+
      '<text x="'+(x+Math.min(260,width)/2)+'" y="28" class="mvl-dim">長 = w + '+d+'</text>'+
      '<text x="18" y="'+(y+Math.min(150,height)/2)+'" class="mvl-dim" transform="rotate(-90 18 '+(y+Math.min(150,height)/2)+')">寬 = w</text>'+
      (reveal?'<text x="'+(x+Math.min(260,width)/2)+'" y="'+(y+Math.min(150,height)/2)+'" class="mvl-region-label">面積 = w(w+'+d+')</text>':'<text x="178" y="130" class="mvl-question">先判斷這是乘積還是周長</text>')+
      '</svg>';
  };

  const renderQuadraticMeaning = (lesson,state) => {
    const mode=Number(state.quadMeaningMode||0);
    const classify=Number(state.quadClassify||0);
    const candidate=Number(state.quadCandidate??1);
    const contextPred=Number(state.quadContextPrediction||0);
    let body='';
    if(mode===0){
      const feedback=!classify
        ? '先化簡再分類；不要因為原式看見 x² 就直接下結論。'
        : classify===1
          ? '正確。2x²+3x=x²+7x−4 化簡為 x²−4x+4=0：只有一個未知數、最高次 2，而且有等號。'
          : '這一題化簡後仍保留 x² 項；請把所有項移到同一側再合併。';
      body='<div class="mvl-q-classify" role="img" aria-label="原方程式先移項化簡再判斷未知數種類、最高次與等號">'+
        '<div class="mvl-q-line"><span>原式</span><strong>2x² + 3x = x² + 7x − 4</strong></div>'+
        '<div class="mvl-q-arrow">先移項、合併同類項 ↓</div>'+
        (classify?'<div class="mvl-q-line is-result"><span>化簡</span><strong>x² − 4x + 4 = 0</strong></div>':'<div class="mvl-q-cover">答案先隱藏</div>')+
        '</div>'+
        select('quadClassify','化簡後是否為一元二次方程式？',classify,[[0,'先預測'],[1,'是'],[2,'不是']])+
        '<p class="mvl-feedback" aria-live="polite">'+esc(feedback)+'</p>'+
        (classify?'<div class="mvl-equation"><span>反例比較</span><strong>3x² + 2x² = 5x² → 0 = 0</strong><p>這個式子化簡後未知數消失，因此不能只靠「原本有 x²」判斷。</p></div>':'');
    } else if(mode===1){
      const left=candidate*candidate+3*candidate, right=10, pass=left===right;
      body='<div class="mvl-q-root-check" role="img" aria-label="候選 x 同時代入方程式左右兩側">'+
        '<div class="mvl-q-pan"><span>左側 x²+3x</span><strong>'+left+'</strong></div><b>'+(pass?'=':(left<right?'<':'>'))+'</b>'+
        '<div class="mvl-q-pan"><span>右側</span><strong>'+right+'</strong></div></div>'+
        range('quadCandidate','候選 x',candidate,-4,4)+
        '<p class="mvl-feedback" aria-live="polite">'+esc(pass?'x='+candidate+' 使左右兩側同為 10，所以這個候選值是解。這只是「驗證一個候選」，還不是求出全部根。':'x='+candidate+' 時左側 '+left+'、右側 10，不相等，所以這個候選值不是解。')+'</p>'+
        '<div class="mvl-equation"><span>判準</span><strong>同一個候選值必須讓原等式左右相等</strong></div>';
    } else {
      const x=5;
      const feedback=!contextPred
        ? '先把量義連起來：短邊 x、長邊 x+4、面積 45。'
        : contextPred===1
          ? '正確。面積是長×寬，所以是 x(x+4)=45；x>0 是情境範圍，不是拿來改寫等式。'
          : '你把面積誤當成長度相加。請回到長方形面積定義：長×寬。';
      body='<figure class="mvl-visual">'+quadraticRectSvg(x,4,contextPred>0)+'<figcaption>短邊 x，長邊 x+4，面積 45 平方公分。</figcaption></figure>'+
        select('quadContextPrediction','哪個式子保留情境量義？',contextPred,[[0,'先預測'],[1,'x(x+4)=45'],[2,'x+x+4=45'],[3,'x²+4=45']])+
        '<p class="mvl-feedback" aria-live="polite">'+esc(feedback)+'</p>'+
        (contextPred===1?'<div class="mvl-equation"><strong>x=5 時：5×9=45</strong><p>所以 5 是這個方程式的解；但本課只做候選驗證，不把「驗證一根」說成「求出全部根」。</p></div>':'');
    }
    const transfer=Number(state.quadMeaningTransfer||0);
    const transferFeedback=!transfer?'最後檢查一個易混淆題：含 x² 不代表化簡後一定仍是二次方程式。':transfer===2?'正確。3x²+2x²=5x² 化簡成 0=0，未知數消失。':'先把左右的 5x² 消掉，再看還剩什麼。';
    return '<section class="mvl mvl-quadratic-meaning" aria-label="一元二次方程式意義視覺實驗室">'+
      '<div class="mvl-task"><span class="mvl-step">1 一次只做一件事</span><strong>先化簡分類，再驗根，再建模</strong><p>本課不提前求全部根；先把「什麼叫二次方程式、什麼叫解」弄清楚。</p></div>'+
      select('quadMeaningMode','探索工作台',mode,[[0,'化簡後分類'],[1,'候選根左右代入'],[2,'面積情境列式']])+
      body+
      '<div class="mvl-transfer"><span class="mvl-step">2 遷移</span><strong>3x²+2x²=5x² 化簡後呢？</strong>'+
      select('quadMeaningTransfer','判斷',transfer,[[0,'先預測'],[1,'仍是一元二次方程式'],[2,'不是；化簡成 0=0']])+
      '<p class="mvl-feedback" aria-live="polite">'+esc(transferFeedback)+'</p></div></section>';
  };

  const renderQuadraticSolution = (lesson,state) => {
    const mode=Number(state.quadSolveMode||0);
    let body='';
    if(mode===0){
      const rootPred=Number(state.quadRootPrediction||0);
      const filter=Number(state.quadContextFilter||0);
      const feedback=!rootPred?'先預測：w²+5w−84=0 因式分解後會有幾個代數根？':rootPred===2?'正確。零乘積性質給出 w=-12 與 7；先完整保留兩根，再談情境。':'找兩數乘積 −84、和 +5：12 與 −7，因此兩個一次因式各給一根。';
      const filterFeedback=!filter?'代數根與實際尺寸要分兩欄。':filter===2?'正確。代數根仍是 {−12,7}；正寬度條件只讓實際寬度保留 7。':'負根不能從「代數根集合」刪掉；它只是不能代表正的實際寬度。';
      body='<figure class="mvl-visual">'+quadraticRectSvg(7,5,rootPred>0)+'<figcaption>木板面積 84，長比寬多 5：w(w+5)=84。</figcaption></figure>'+
        select('quadRootPrediction','因式分解後有幾個代數根？',rootPred,[[0,'先預測'],[1,'1 個'],[2,'2 個'],[3,'沒有實根']])+
        '<p class="mvl-feedback" aria-live="polite">'+esc(feedback)+'</p>'+
        (rootPred?'<div class="mvl-equation"><span>完整根集</span><strong>w²+5w−84=(w+12)(w−7)=0 → w∈{−12,7}</strong><p>兩個候選都先代回方程式；情境條件另外判斷。</p></div>':'')+
        select('quadContextFilter','正寬度情境如何處理？',filter,[[0,'先判斷'],[1,'把 −12 從代數根集合刪掉'],[2,'保留代數根 {−12,7}，實際寬度只取 7']])+
        '<p class="mvl-feedback" aria-live="polite">'+esc(filterFeedback)+'</p>'+
        (filter===2?'<div class="mvl-system-cards"><article class="mvl-system-card"><strong>代數根</strong><p>{−12, 7}</p></article><article class="mvl-system-card"><strong>可行尺寸</strong><p>寬 7、長 12；7×12=84</p></article></div>':'');
    } else if(mode===1){
      const add=Number(state.quadCompleteSquare||0);
      const feedback=!add?'x²+4x+1=0 → x²+4x=−1。要補成平方，兩側要怎麼做？':add===1?'正確。兩側同加 4 才保持等式等值：x²+4x+4=3 → (x+2)²=3。':'只補左側會改變解集合。任何等式變形都要同步維持兩側相等。';
      body='<div class="mvl-q-balance" role="img" aria-label="配方法在等式兩側同加四">'+
        '<div><span>左側</span><strong>x² + 4x</strong><em>'+(add?'+4':'+ ?')+'</em></div>'+
        '<b>=</b><div><span>右側</span><strong>−1</strong><em>'+(add?'+4':'+ ?')+'</em></div></div>'+
        select('quadCompleteSquare','要在哪裡加 4？',add,[[0,'先預測'],[1,'左右兩側都加 4'],[2,'只在左側加 4'],[3,'只在右側加 4']])+
        '<p class="mvl-feedback" aria-live="polite">'+esc(feedback)+'</p>'+
        (add===1?'<div class="mvl-equation"><strong>(x+2)²=3 → x=−2±√3</strong><p>「±」代表兩個實根；不可只取其中一支。</p></div>':'');
    } else if(mode===2){
      const delta=Number(state.quadDeltaPrediction||0);
      const feedback=!delta?'2x²+3x−2=0：a=2、b=3、c=−2。先算 Δ=b²−4ac。':delta===1?'正確。Δ=9−4·2·(−2)=25>0，所以有兩個相異實根。':'注意 c 是 −2；−4ac 會變成加 16。';
      body='<div class="mvl-q-coeff" role="img" aria-label="二次方程式係數卡 a 二 b 三 c 負二"><span>a<strong>2</strong></span><span>b<strong>3</strong></span><span>c<strong>−2</strong></span></div>'+
        select('quadDeltaPrediction','判別式 Δ 是多少？',delta,[[0,'先預測'],[1,'25'],[2,'−7'],[3,'7']])+
        '<p class="mvl-feedback" aria-live="polite">'+esc(feedback)+'</p>'+
        (delta===1?'<div class="mvl-equation"><span>公式解</span><strong>x=(-3±5)/4 → x=1/2 或 −2</strong><p>判別式先告訴你實根型態；公式仍要保留 b、c 原本的符號。</p></div>':'');
    } else {
      const transfer=Number(state.quadSolutionTransfer||0);
      const feedback=!transfer?'換一題 x²−x−12=0：哪種方法最直接？':transfer===1?'正確。找乘積 −12、和 −1 的 3 與 −4： (x−4)(x+3)=0，根為 4、−3。':'這題可整數因式分解，不必先用較長的公式法。';
      body='<div class="mvl-q-method-map"><article><strong>因式分解</strong><p>能快速找到整數因式時優先。</p></article><article><strong>配方法</strong><p>看見 x²+bx 時補 (b/2)²，兩側同步。</p></article><article><strong>公式解</strong><p>一般情況可用，先保留 a,b,c 符號與 Δ。</p></article></div>'+
        select('quadSolutionTransfer','x²−x−12=0 選哪個？',transfer,[[0,'先判斷'],[1,'因式分解'],[2,'配方法才允許'],[3,'只可公式解']])+
        '<p class="mvl-feedback" aria-live="polite">'+esc(feedback)+'</p>'+
        (transfer===1?'<div class="mvl-equation"><strong>(x−4)(x+3)=0 → x=4 或 −3</strong><p>兩根都要代回原式確認；若題目有情境，再另外做定義域篩選。</p></div>':'');
    }
    return '<section class="mvl mvl-quadratic-solution" aria-label="一元二次方程式解法與應用視覺工作台">'+
      '<div class="mvl-task"><span class="mvl-step">1 選一個解題工作</span><strong>建模、求根、驗根、情境篩選分開處理</strong><p>每一站只聚焦一種推理，避免把公式、圖形和情境條件全部塞在同一畫面。</p></div>'+
      select('quadSolveMode','解題工作台',mode,[[0,'矩形建模＋完整根集'],[1,'配方法：兩側同步'],[2,'判別式＋公式解'],[3,'方法選擇遷移']])+
      body+'</section>';
  };

  const renderQuadraticLab = (lesson,state) =>
    lesson.simulation.model==='a-8-6-quadratic-meaning-v1' ? renderQuadraticMeaning(lesson,state) : renderQuadraticSolution(lesson,state);

  const systemCard = (title,equation,value,target,shown) => {
    const pass=value===target;
    return '<article class="mvl-system-card"><b>'+esc(title)+'</b><strong>'+esc(equation)+'</strong>'+
      (shown?'<p class="mvl-system-result '+(pass?'is-pass':'is-fail')+'">'+(pass?'✓ 通過':'✗ 未通過')+'：左側 = '+value+'，右側 = '+target+'</p>':'<p class="mvl-system-result">先預測，計算暫時隱藏</p>')+
      '</article>';
  };

  const renderSystemMeaning = (lesson,state) => {
    const x=Math.max(0,Math.min(18,Number(state.systemX??10)));
    const y=18-x;
    const prediction=Number(state.meaningPrediction||0);
    const reveal=prediction>0;
    const first=x+y, second=2*x+y;
    const both=first===18 && second===30;
    const feedback=!prediction
      ? '先判斷候選 (10,8)：只通過一條式，能不能叫共同解？'
      : prediction===2
        ? '正確。10+8=18，但 2×10+8=28≠30；只通過第一張紀錄，還不是共同解。'
        : '再做第二次檢查。聯立方程式的「解」必須讓兩條等式同時成立。';
    const liveFeedback=reveal
      ? (both?'目前 ('+x+','+y+') 同時通過兩條限制，所以是共同解。':'目前 ('+x+','+y+') 只通過總杯數；冰塊條件得到 '+second+'，仍不是共同解。')
      : '預測後再調整果汁杯數，找出兩張工作單同時出現 ✓ 的位置。';
    const transfer=Number(state.systemMeaningTransfer||0);
    const transferFeedback=!transfer?'遷移到回收站：別忘了 x、y 的順序也屬於證據。':transfer===1?'正確。(21,4) 同時得到 25 件與 46 公斤，兩條限制都成立。':'再逐式代入：(21+4) 與 (2×21+4) 要分別核對。';
    return '<section class="mvl mvl-system-meaning" aria-label="聯立方程式共同解雙條件檢查模型">'+
      '<div class="mvl-task"><span class="mvl-step">1 先預測</span><strong>候選 (10,8) 是共同解嗎？</strong><p>一組數要通過兩張工作單，不能只看其中一張。</p></div>'+
      select('meaningPrediction','你的預測',prediction,[[0,'先選答案'],[1,'是，通過任一式即可'],[2,'不是，只通過第一式'],[3,'不是，只通過第二式']])+
      '<p class="mvl-feedback" aria-live="polite">'+esc(feedback)+'</p>'+
      '<div class="mvl-system-candidate" role="img" aria-label="候選有序數對 x 等於 '+x+'，y 等於 '+y+'，逐一檢查兩條限制"><div class="mvl-system-pair"><span>x 果汁</span><b>'+x+'</b><span>y 茶</span><b>'+y+'</b></div>'+
      '<div class="mvl-system-cards">'+
      systemCard('工作單 A：總杯數','x + y = 18',first,18,reveal)+
      systemCard('工作單 B：冰塊需求','2x + y = 30',second,30,reveal)+
      '</div></div>'+
      range('systemX','調整果汁 x（茶 y 自動維持總杯數 18）',x,0,18)+
      '<p class="mvl-feedback" aria-live="polite">'+esc(liveFeedback)+'</p>'+
      (reveal?'<div class="mvl-equation"><span>共同解判準</span><strong>兩張卡都 ✓ 才完成；目前 '+(both?'(12,6) 是共同解':'尚未同時成立')+'</strong></div>':'')+
      '<div class="mvl-transfer"><span class="mvl-step">2 遷移</span><strong>回收站：x+y=25，2x+y=46；(21,4) 呢？</strong>'+
      select('systemMeaningTransfer','判斷',transfer,[[0,'先預測'],[1,'同時通過兩式'],[2,'只通過第一式'],[3,'只通過第二式']])+
      '<p class="mvl-feedback" aria-live="polite">'+esc(transferFeedback)+'</p></div>'+
      '</section>';
  };

  const renderSystemElimination = (lesson,state) => {
    const method=Number(state.eliminationMethod||0);
    const back=Number(state.eliminationBack||0);
    const transfer=Number(state.eliminationTransfer||0);
    const methodFeedback=!method
      ? '先看 y 欄：兩式的 y 係數都是 1。哪個整行運算能最省步驟地消去 y？'
      : method===1
        ? '正確。第二式減第一式時，左邊每一項與右邊常數都必須一起相減。'
        : '這個方法不是不能做，但本題 y 係數已相同；直接整行相減更短，也更容易保留等式結構。';
    const backFeedback=!back
      ? (method===1?'得到 x=15 仍未完成；聯立解需要兩個未知數。':'先選消去策略。')
      : back===2
        ? '正確。15+y=35，所以 y=20；再把 (15,20) 同時送回兩條原式。'
        : '回代 x=15 到 x+y=35：y 應補足到 35。';
    const transferFeedback=!transfer
      ? '新題 x+y=40、3x+2y=100：先找能讓 y 係數互相抵消的整行操作。'
      : transfer===1
        ? '正確。第一式乘 −2 後與第二式相加：x=20，再回代 y=20；兩式都成立。'
        : '要消去 y，兩個 y 係數要成為相反數；把第一式整行乘 −2。';
    return '<section class="mvl mvl-system-elimination" aria-label="聯立方程式消去法整行運算模型">'+
      '<div class="mvl-task"><span class="mvl-step">1 看係數再選方法</span><strong>x+y=35；2x+y=50</strong><p>不是背固定順序，而是找哪一欄可以最直接消去。</p></div>'+
      '<div class="mvl-system-stack" role="img" aria-label="兩條方程式按 x、y、常數對齊">'+
      '<div><span>x</span><span>+</span><span>y</span><span>=</span><span>35</span></div>'+
      '<div><span>2x</span><span>+</span><span>y</span><span>=</span><span>50</span></div>'+
      (method===1?'<div class="mvl-system-operation"><span>相減</span><strong>x</strong><span>+</span><strong>0y</strong><span>=</span><strong>15</strong></div>':'<div class="mvl-system-operation is-hidden">先預測整行運算，再揭示結果</div>')+
      '</div>'+
      select('eliminationMethod','先預測最省步驟的方法',method,[[0,'先選方法'],[1,'第二式 − 第一式，消去 y'],[2,'先把兩式都乘 2'],[3,'只把左邊相減']])+
      '<p class="mvl-feedback" aria-live="polite">'+esc(methodFeedback)+'</p>'+
      (method===1?'<div class="mvl-equation"><span>整行證據</span><strong>(2x+y)−(x+y)=50−35 → x=15</strong><p>右側也要做 50−35；只動左邊會破壞等式。</p></div>':'')+
      select('eliminationBack','x=15 後，y 是多少？',back,[[0,'先回代'],[1,'15'],[2,'20'],[3,'35']])+
      '<p class="mvl-feedback" aria-live="polite">'+esc(backFeedback)+'</p>'+
      (back===2?'<div class="mvl-system-cards">'+systemCard('原式 A','x+y=35',15+20,35,true)+systemCard('原式 B','2x+y=50',2*15+20,50,true)+'</div>':'')+
      '<div class="mvl-transfer"><span class="mvl-step">2 遷移</span><strong>x+y=40；3x+2y=100</strong>'+
      select('eliminationTransfer','哪個操作先消去 y？',transfer,[[0,'先預測'],[1,'第一式×(−2)，再與第二式相加'],[2,'兩式直接相減'],[3,'只把 y 的係數改號']])+
      '<p class="mvl-feedback" aria-live="polite">'+esc(transferFeedback)+'</p></div>'+
      '</section>';
  };

  const renderSystemLab = (lesson,state) =>
    lesson.simulation.model==='a-7-4-system-meaning-v1' ? renderSystemMeaning(lesson,state) : renderSystemElimination(lesson,state);

  const polySubtractionVisual = reveal =>
    '<div class="mvl-poly-board mvl-poly-subtract" role="img" aria-label="五 x 平方減去括號二 x 平方減三 x 加一的逐項符號模型">'+
      '<div class="mvl-poly-expression"><span class="mvl-term">5x²</span><b>−</b><span class="mvl-bracket">'+
      '<span class="mvl-term">2x²</span><span class="mvl-term">−3x</span><span class="mvl-term">+1</span></span></div>'+
      '<div class="mvl-poly-arrow">括號前的 − 等於每一項都乘 −1 ↓</div>'+
      (reveal
        ? '<div class="mvl-poly-expression is-result"><span class="mvl-term">5x²</span><span class="mvl-term">−2x²</span><span class="mvl-term">+3x</span><span class="mvl-term">−1</span></div><p><strong>合併：</strong>3x² + 3x − 1</p>'
        : '<p class="mvl-poly-cover">先預測：括號打開時，哪幾項要變號？</p>')+
    '</div>';

  const polyMultiplicationVisual = reveal =>
    '<div class="mvl-poly-board mvl-poly-multiply" role="img" aria-label="二 x 減一乘 x 加三的四格乘積模型">'+
      '<div class="mvl-poly-grid">'+
        '<span></span><b>x</b><b>+3</b>'+
        '<b>2x</b><span>'+(reveal?'2x²':'？')+'</span><span>'+(reveal?'+6x':'？')+'</span>'+
        '<b>−1</b><span>'+(reveal?'−x':'？')+'</span><span>'+(reveal?'−3':'？')+'</span>'+
      '</div>'+
      (reveal
        ? '<p><strong>四格缺一不可：</strong>2x² + 6x − x − 3 = 2x² + 5x − 3</p>'
        : '<p class="mvl-poly-cover">先預測：兩個二項式總共要做幾次項對項乘法？</p>')+
    '</div>';

  const polyDivisionVisual = reveal =>
    '<div class="mvl-poly-board mvl-poly-divide" role="img" aria-label="二 x 平方加三 x 減六除以 x 加三的商與餘式重組模型">'+
      '<div class="mvl-division-row"><span class="mvl-division-part">2x² + 3x − 6</span><b>=</b>'+
      (reveal
        ? '<span class="mvl-division-part">(x+3)(2x−3)</span><b>+</b><span class="mvl-division-remainder">3</span>'
        : '<span class="mvl-division-part">除式 × 商</span><b>+</b><span class="mvl-division-remainder">？</span>')+
      '</div>'+
      (reveal
        ? '<p><strong>回乘：</strong>(x+3)(2x−3)+3 = 2x²+3x−6，所以餘式是 3。</p>'
        : '<p class="mvl-poly-cover">先預測餘式，再用「除式×商＋餘式」重組原式。</p>')+
    '</div>';

  const renderPolynomialOps = (lesson,state) => {
    const mode=Number(state.polyMode||0);
    const modeLabels=['括號減法','多項式乘法','多項式除法'];
    const predKey=mode===0?'subtractPrediction':mode===1?'multiplyPrediction':'dividePrediction';
    const prediction=Number(state[predKey]||0);
    const transfer=Number(state.polyTransfer||0);
    let visual='', predictionControl='', feedback='', evidence='';
    if(mode===0){
      const reveal=prediction>0;
      visual=polySubtractionVisual(reveal);
      predictionControl=select('subtractPrediction','先預測哪些項會變號',prediction,[[0,'先選答案'],[1,'括號內三項全部變號'],[2,'只有第一項變號'],[3,'全部維持原符號']]);
      feedback=!prediction?'先把「減去整個括號」想成「乘上 −1」。':prediction===1?'正確。−1 必須分配到括號內每一項；常數 +1 也會變成 −1。':'再看括號前的負號：它作用在整個括號，不只第一項。';
      evidence=reveal?'<div class="mvl-equation"><span>數值證據</span><strong>x=1：原式 5−(2−3+1)=5；整理式 3+3−1=5</strong></div>':'';
    } else if(mode===1){
      const reveal=prediction>0;
      visual=polyMultiplicationVisual(reveal);
      predictionControl=select('multiplyPrediction','先預測項對項乘法次數',prediction,[[0,'先選答案'],[1,'4 次'],[2,'2 次，只乘首尾'],[3,'3 次']]);
      feedback=!prediction?'先不要合併同類項；數一數左邊每一項要和右邊幾項相乘。':prediction===1?'正確。2×2 共四個乘積；先填滿四格，再把 6x 與 −x 合併。':'每個括號都有 2 項；左邊每一項都要乘到右邊 2 項，所以共有 4 格。';
      evidence=reveal?'<div class="mvl-equation"><span>等值檢查</span><strong>x=2：(4−1)(2+3)=15；2·4+5·2−3=15</strong></div>':'';
    } else {
      const reveal=prediction>0;
      visual=polyDivisionVisual(reveal);
      predictionControl=select('dividePrediction','先預測餘式',prediction,[[0,'先選答案'],[1,'0'],[2,'3'],[3,'−3']]);
      feedback=!prediction?'除法不是只找商；最後必須讓「除式×商＋餘式」完整回到被除式。':prediction===2?'正確。商 2x−3，餘式 3；回乘再加 3 才完整還原原式。':'把 (x+3)(2x−3) 展開：會得到 2x²+3x−9；還差多少才回到 −6？';
      evidence=reveal?'<div class="mvl-equation"><span>重組證據</span><strong>2x²+3x−6 = (x+3)(2x−3)+3</strong></div>':'';
    }
    const transferFeedback=!transfer?'最後換一個長方形情境，檢查你理解的是四格配對，不是記住原題。':transfer===1?'正確。x²−2x+5x−10 = x²+3x−10；x=3 時原乘積 8×1=8，展開式也等於 8。':'把四個乘積先寫完：x·x、x·(−2)、5·x、5·(−2)，再合併兩個一次項。';
    return '<section class="mvl mvl-poly" data-poly-modes="subtract multiply divide" aria-label="多項式四則運算視覺工作台">'+
      '<div class="mvl-task"><span class="mvl-step">1 選一種認知工作</span><strong>'+modeLabels[mode]+'</strong><p>一次只處理一種規則；先預測，再揭示中間結構。</p></div>'+
      select('polyMode','運算工作台',mode,[[0,'括號減法'],[1,'多項式乘法'],[2,'多項式除法']])+
      visual+
      '<div class="mvl-poly-controls">'+predictionControl+'<p class="mvl-feedback" aria-live="polite">'+esc(feedback)+'</p>'+evidence+'</div>'+
      '<div class="mvl-transfer"><span class="mvl-step">2 遷移</span><strong>長 (x+5)、寬 (x−2) 的長方形面積</strong>'+
      select('polyTransfer','展開後是哪一式？',transfer,[[0,'先預測'],[1,'x²+3x−10'],[2,'x²+7x−10'],[3,'x²+3x+10']])+
      '<p class="mvl-feedback" aria-live="polite">'+esc(transferFeedback)+'</p>'+
      (transfer===1?'<div class="mvl-equation"><strong>(x+5)(x−2)=x²+3x−10</strong><p>x=3：8×1=8；9+9−10=8。</p></div>':'')+
      '</div>'+
      '<details class="mvl-evidence"><summary>三種運算各要留下什麼證據？</summary><p>減法：每項變號紀錄。乘法：完整四格配對。除法：除式×商＋餘式能重組被除式。這三種證據不能互相替代。</p></details>'+
      '</section>';
  };

  const factorRow = (title,tokens,common) =>
    '<div class="mvl-factor-row"><strong>'+esc(title)+'</strong><div class="mvl-token-row">'+tokens.map((t,i)=>'<span class="mvl-token '+(common.includes(i)?'is-common':'')+'">'+esc(t)+'</span>').join("")+'</div></div>';

  const factorMeaningSvg = x => {
    const unit=28, ox=36, oy=42, xp=x*unit, five=5*unit, two=2*unit;
    const cell=(rx,ry,w,h,label,klass) =>
      '<rect x="'+rx+'" y="'+ry+'" width="'+w+'" height="'+h+'" class="'+klass+'"/>'+
      '<text x="'+(rx+w/2)+'" y="'+(ry+h/2)+'" class="mvl-region-label">'+label+'</text>';
    return '<svg viewBox="0 0 356 286" role="img" aria-label="x 加 2 乘 x 加 5 的四格面積模型，x 等於 '+x+'">'+
      cell(ox,oy,xp,xp,'x²','mvl-a2')+
      cell(ox+xp,oy,five,xp,'5x','mvl-ab')+
      cell(ox,oy+xp,xp,two,'2x','mvl-addback')+
      cell(ox+xp,oy+xp,five,two,'10','mvl-b2')+
      '<text x="'+(ox+(xp+five)/2)+'" y="24" class="mvl-dim">x + 5</text>'+
      '<text x="14" y="'+(oy+(xp+two)/2)+'" class="mvl-dim" transform="rotate(-90 14 '+(oy+(xp+two)/2)+')">x + 2</text>'+
      '<text x="178" y="270" class="mvl-dim">四格全部乘回，才算完整驗證</text>'+
      '</svg>';
  };

  const renderFactorMeaning = (lesson,state) => {
    const x=Math.max(1,Math.min(5,Number(state.factorMeaningX||2)));
    const candidate=Number(state.candidateFactor||0);
    const transfer=Number(state.factorMeaningTransfer||0);
    const candidates={
      1:{label:'(x+2)(x+5)',expanded:'x² + 7x + 10',ok:true},
      2:{label:'(x+1)(x+6)',expanded:'x² + 7x + 6',ok:false},
      3:{label:'(x+3)(x+4)',expanded:'x² + 7x + 12',ok:false}
    };
    const pick=candidates[candidate];
    const feedback=!pick
      ? '先預測哪一組因式與商式能完整乘回原多項式；不要只看中間項。'
      : pick.ok
        ? '成立。四個乘積 x²、5x、2x、10 全部對回原式，7x 來自兩個交叉區。'
        : '不成立。它雖然也得到 7x，但常數項不同；只核對部分係數不能證明是因式。';
    const transferFeedback=!transfer
      ? '換一個多項式：同時找「常數乘積」與「交叉和」兩個證據。'
      : transfer===1
        ? '正確：3×5=15，而且 3+5=8；完整乘回就是 x²+8x+15。'
        : '再乘回四格。常數乘積與兩個交叉項的和必須同時吻合。';
    return '<section class="mvl mvl-factor-meaning" aria-label="因式與商式完整乘回視覺模型">'+
      '<div class="mvl-task"><span class="mvl-step">1 先看乘法結構</span><strong>x² + 7x + 10 可以寫成哪兩個一次式相乘？</strong><p>因式不是看起來像就算；要能完整乘回。</p></div>'+
      '<div class="mvl-layout"><figure class="mvl-visual">'+factorMeaningSvg(x)+
      '<figcaption>x='+x+' 時，(x+2)(x+5)='+(x+2)*(x+5)+'；圖形仍由 x²、5x、2x、10 四區組成。</figcaption></figure>'+
      '<div class="mvl-panel">'+
      range('factorMeaningX','觀察 x',x,1,5)+
      select('candidateFactor','先預測候選乘積',candidate,[[0,'先選一組'],[1,'(x+2)(x+5)'],[2,'(x+1)(x+6)'],[3,'(x+3)(x+4)']])+
      '<p class="mvl-feedback" aria-live="polite">'+esc(feedback)+'</p>'+
      (pick?'<div class="mvl-equation"><span>完整乘回</span><strong>'+esc(pick.label)+' = '+esc(pick.expanded)+'</strong>'+
        (pick.ok?'<p>x·x + x·5 + 2·x + 2·5 = x² + 5x + 2x + 10。</p>':'<p>與 x² + 7x + 10 逐項比較，至少有一項不同，因此排除。</p>')+
      '</div>':'')+
      '</div></div>'+
      '<div class="mvl-transfer"><span class="mvl-step">2 遷移</span><strong>x² + 8x + 15</strong>'+
      select('factorMeaningTransfer','哪一組完整乘回？',transfer,[[0,'先預測'],[1,'(x+3)(x+5)'],[2,'(x+1)(x+15)'],[3,'(x+2)(x+6)']])+
      '<p class="mvl-feedback" aria-live="polite">'+esc(transferFeedback)+'</p>'+
      (transfer===1?'<div class="mvl-equation"><strong>(x+3)(x+5)=x²+8x+15</strong><p>交叉項 5x+3x=8x；常數 3×5=15。</p></div>':'')+
      '</div>'+
      '<details class="mvl-evidence"><summary>如何排除「看起來很像」的候選？</summary><p>完整乘回並逐項比較。單一代值不相等可否定候選；但單一代值剛好相等，仍不能取代恆等式的完整乘回證據。</p></details>'+
      '</section>';
  };

  const renderFactor = (lesson,state) => {
    const model=lesson.simulation.model;
    if(model==='a-8-4-factor-meaning-v1') return renderFactorMeaning(lesson,state);
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

  const supports = (engine,model) => engine==='math-visual-area' || engine==='math-factor-model' || engine==='math-polynomial-model' || engine==='math-system-model' || engine==='math-quadratic-model';
  const defaults = (engine,model) => engine==='math-visual-area'
    ? {a:4,b:2,formulaMode:0,prediction:0,transferA:5,transferB:1,transferPrediction:0}
    : engine==='math-polynomial-model'
      ? {polyMode:0,subtractPrediction:0,multiplyPrediction:0,dividePrediction:0,polyTransfer:0}
      : engine==='math-system-model'
        ? (model==='a-7-4-system-meaning-v1' ? {meaningPrediction:0,systemX:10,systemMeaningTransfer:0} : {eliminationMethod:0,eliminationBack:0,eliminationTransfer:0})
      : engine==='math-quadratic-model'
        ? (model==='a-8-6-quadratic-meaning-v1' ? {quadMeaningMode:0,quadClassify:0,quadCandidate:1,quadContextPrediction:0,quadMeaningTransfer:0} : {quadSolveMode:0,quadRootPrediction:0,quadContextFilter:0,quadCompleteSquare:0,quadDeltaPrediction:0,quadSolutionTransfer:0})
      : model==='a-8-4-factor-meaning-v1'
        ? {factorMeaningX:2,candidateFactor:0,factorMeaningTransfer:0}
        : {commonFactor:0,factorTransfer:0};
  const label = engine => engine==='math-visual-area' ? '面積公式探索臺' : engine==='math-polynomial-model' ? '多項式視覺工作台' : engine==='math-system-model' ? '聯立方程式雙條件工作台' : engine==='math-quadratic-model' ? '二次方程式視覺工作台' : '因式結構探索臺';
  const render = (lesson,state) => lesson.simulation.engine==='math-visual-area' ? renderArea(lesson,state) : lesson.simulation.engine==='math-polynomial-model' ? renderPolynomialOps(lesson,state) : lesson.simulation.engine==='math-system-model' ? renderSystemLab(lesson,state) : lesson.simulation.engine==='math-quadratic-model' ? renderQuadraticLab(lesson,state) : renderFactor(lesson,state);
  window.MathVisualLabs={supports,defaults,label,render};
})();