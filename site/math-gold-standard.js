/* Phase-1 Math Gold Standard reference lessons.
   Unit-specific models wrap the existing MathVisualLabs dispatcher. */
(() => {
  const base = window.MathVisualLabs;
  if (!base) return;

  const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
  const selected=(a,b)=>String(a)===String(b)?" selected":"";
  const select=(key,label,value,options)=>
    '<label class="mgs-control"><span>'+esc(label)+'</span><select data-sim-control="'+esc(key)+'" aria-label="'+esc(label)+'">'+
    options.map(([v,t])=>'<option value="'+esc(v)+'"'+selected(value,v)+'>'+esc(t)+'</option>').join("")+'</select></label>';
  const range=(key,label,value,min,max,step=1)=>
    '<label class="mgs-control"><span>'+esc(label)+' <output>'+esc(value)+'</output></span><input data-sim-control="'+esc(key)+'" type="range" min="'+min+'" max="'+max+'" step="'+step+'" value="'+esc(value)+'" aria-label="'+esc(label)+'"></label>';

  const signedModels = new Set(["n-7-3-signed-operations-v1"]);
  const functionModels = new Set(["f-8-2-linear-parameter-v1"]);
  const geometryModels = new Set(["s-8-6-pythagorean-area-v1"]);
  const dataModels = new Set(["d-9-1-boxplot-iqr-v1"]);
  const probabilityModels = new Set(["d-9-2-relative-frequency-v1"]);
  const allModels = new Set([...signedModels,...functionModels,...geometryModels,...dataModels,...probabilityModels]);

  const numberX = value => 28 + ((value + 25) / 27) * 300;
  const signedLineSvg = reveal => {
    const start=-18.5, afterMultiply=-23.5, final=-22.75;
    const ticks=[-25,-20,-15,-10,-5,0];
    return '<svg class="mgs-signed-svg" viewBox="0 0 356 180" role="img" aria-label="負數混合運算數線：從負18.5先加負5，再因減去負0.75向右移0.75">'+
      '<line x1="28" y1="100" x2="328" y2="100" class="mgs-axis"/>'+
      ticks.map(v=>'<g><line x1="'+numberX(v)+'" y1="92" x2="'+numberX(v)+'" y2="108" class="mgs-tick"/><text x="'+numberX(v)+'" y="130" text-anchor="middle">'+v+'</text></g>').join("")+
      '<circle cx="'+numberX(start)+'" cy="100" r="7" class="mgs-point"/><text x="'+numberX(start)+'" y="76" text-anchor="middle">−18.5</text>'+
      (reveal?'<path d="M'+numberX(start)+' 94 Q'+((numberX(start)+numberX(afterMultiply))/2)+' 42 '+numberX(afterMultiply)+' 94" class="mgs-arrow"/>'+
      '<text x="'+((numberX(start)+numberX(afterMultiply))/2)+'" y="38" text-anchor="middle">加 −5</text>'+
      '<circle cx="'+numberX(afterMultiply)+'" cy="100" r="7" class="mgs-point"/>'+
      '<path d="M'+numberX(afterMultiply)+' 112 Q'+((numberX(afterMultiply)+numberX(final))/2)+' 154 '+numberX(final)+' 112" class="mgs-arrow mgs-arrow-secondary"/>'+
      '<text x="'+((numberX(afterMultiply)+numberX(final))/2)+'" y="166" text-anchor="middle">−(−0.75) = +0.75</text>'+
      '<circle cx="'+numberX(final)+'" cy="100" r="8" class="mgs-final"/><text x="'+numberX(final)+'" y="76" text-anchor="middle">−22.75</text>':'<text x="178" y="48" class="mgs-question" text-anchor="middle">先預測結果正負與第一個運算</text>')+
      '</svg>';
  };
  const renderSigned = state => {
    const prediction=Number(state.n73Prediction||0);
    const evidence=Number(state.n73Evidence||0);
    const transfer=Number(state.n73Transfer||0);
    const unlocked=prediction>0;
    const predictionFeedback=!prediction?"先看整個式子，不先計算：結果大致會落在正數還是負二十多？":prediction===1?"預測合理。先做乘法 4×(−1.25)，外層加減暫時不要動。":"再估一次：起點已是 −18.5，又要先加入 −5；最後只補回 +0.75，不可能變成正數。";
    const evidenceText=!evidence?"選一層證據，逐步確認你不是靠口訣。":evidence===1?"乘法子運算先完成：4×(−1.25)=−5，原式變成 −18.5+(−5)−(−0.75)。":evidence===2?"外層減去負數只影響最後一筆：−(−0.75)=+0.75；數線因此從 −23.5 向右移到 −22.75。":"精確回查：−18.5=−74/4、−5=−20/4、+0.75=+3/4，所以總和 −91/4=−22.75。";
    const transferFeedback=!transfer?"換成新式子，先做乘除再處理外層加減。":transfer===2?"正確：2×(−3)=−6，(−4)÷2=−2，所以 −6−(−6)−2=−2。":"把乘除子運算先各自算完：中間會出現『減去 −6』，不是直接把所有負號改正。";
    return '<section class="mgs mgs-signed" aria-label="負數混合運算 Visual-First 實驗室">'+
      '<div class="mgs-task"><span>1 預測</span><strong>−18.5 + 4×(−1.25) − (−0.75)</strong><p>先判斷量級與第一個運算，不先展開全部答案。</p></div>'+
      select("n73Prediction","結果大致落在哪裡？",prediction,[[0,"先預測"],[1,"負二十多"],[2,"接近 0"],[3,"正二十多"]])+
      '<p class="mgs-feedback" aria-live="polite">'+esc(predictionFeedback)+'</p>'+
      '<figure class="mgs-figure">'+signedLineSvg(unlocked)+'<figcaption>'+esc(unlocked?"數線只表達外層加減；乘法 4×(−1.25) 先在運算節點完成。":"預測提交前，移動方向與答案保持隱藏。")+'</figcaption></figure>'+
      (unlocked?'<div class="mgs-operation-tree" role="img" aria-label="運算順序樹"><div><b>先做</b><span>4×(−1.25)</span><strong>−5</strong></div><div><b>再做</b><span>−18.5+(−5)</span><strong>−23.5</strong></div><div><b>最後</b><span>−(−0.75)</span><strong>+0.75 → −22.75</strong></div></div>':'')+
      (unlocked?select("n73Evidence","查看哪一層證據？",evidence,[[0,"選證據"],[1,"乘法先做"],[2,"減去負數"],[3,"共同分母回查"]]):"")+
      '<p class="mgs-feedback" aria-live="polite">'+esc(unlocked?evidenceText:"先完成預測。")+'</p>'+
      '<div class="mgs-transfer"><span>2 遷移</span><strong>−6 − 2×(−3) + (−4)÷2</strong>'+
      select("n73Transfer","結果是多少？",transfer,[[0,"先預測"],[1,"2"],[2,"−2"],[3,"−24"]])+
      '<p class="mgs-feedback" aria-live="polite">'+esc(transferFeedback)+'</p></div></section>';
  };

  const graphPoint=(x,y)=>({x:42+x*34,y:238-y*0.95});
  const lineSegment=(m,b,klass)=> {
    const p1=graphPoint(0,b),p2=graphPoint(8,m*8+b);
    return '<line x1="'+p1.x+'" y1="'+p1.y+'" x2="'+p2.x+'" y2="'+p2.y+'" class="'+klass+'"/>';
  };
  const functionSvg=(mode,a,b,x)=>{
    const axes='<line x1="42" y1="20" x2="42" y2="242" class="mgs-axis"/><line x1="42" y1="238" x2="326" y2="238" class="mgs-axis"/>'+
      [0,2,4,6,8].map(v=>'<text x="'+graphPoint(v,0).x+'" y="257" text-anchor="middle">'+v+'</text>').join("")+
      [0,50,100,150,200].map(v=>'<text x="34" y="'+(graphPoint(0,v).y+4)+'" text-anchor="end">'+v+'</text>').join("");
    let lines="",label="";
    if(mode===0){
      lines=lineSegment(18,30,"mgs-line-base")+lineSegment(a,30,"mgs-line-current");
      label='固定 b=30；比較 a=18 與 a='+a;
    } else if(mode===1){
      lines=lineSegment(8,30,"mgs-line-base")+lineSegment(8,b,"mgs-line-current");
      label='固定 a=8；比較 b=30 與 b='+b;
    } else if(mode===2){
      lines=lineSegment(18,30,"mgs-line-base")+lineSegment(24,0,"mgs-line-current");
      const y1=18*x+30,y2=24*x,p=graphPoint(x,y1);
      lines+='<circle cx="'+p.x+'" cy="'+p.y+'" r="6" class="mgs-final"/><line x1="'+p.x+'" y1="238" x2="'+p.x+'" y2="'+p.y+'" class="mgs-guide"/>';
      label='x='+x+'：甲 '+y1+'；乙 '+y2+'；差 '+Math.abs(y1-y2);
    } else {
      const y=Math.max(0,-7*x+100),p=graphPoint(x,y);
      lines=lineSegment(-7,100,"mgs-line-current")+'<circle cx="'+p.x+'" cy="'+p.y+'" r="6" class="mgs-final"/>';
      label='水量 y=−7x+100；x='+x+' 時 y='+(-7*x+100);
    }
    return '<svg viewBox="0 0 356 270" role="img" aria-label="'+esc(label)+'">'+axes+lines+'<text x="178" y="16" text-anchor="middle">'+esc(label)+'</text></svg>';
  };
  const renderFunction = state => {
    const mode=Number(state.f82Mode||0),a=Number(state.f82A||8),b=Number(state.f82B||50),x=Number(state.f82X||5);
    const prediction=Number(state.f82Prediction||0),transfer=Number(state.f82Transfer||0);
    const modeTitle=["只改斜率 a","只改截距 b","找兩方案交點","負斜率情境"][mode];
    let feedback="",table="";
    if(mode===0){
      feedback=!prediction?"先預測：b 固定 30，只把 a 從 18 改小，哪個量一定不動？":prediction===1?"正確。x=0 時 y=b=30 不動；相鄰 x 每增加 1 的費用差由 18 改成 "+a+"。":"再看 x=0：不論 a 是多少，ax 都是 0，所以 y 軸截距仍是 30。";
      table='<table class="mgs-table"><caption>同一組 x，比較 a 的效果</caption><thead><tr><th>x</th><th>18x+30</th><th>'+a+'x+30</th></tr></thead><tbody>'+[0,2,4].map(v=>'<tr><td>'+v+'</td><td>'+(18*v+30)+'</td><td>'+(a*v+30)+'</td></tr>').join("")+'</tbody></table>';
    } else if(mode===1){
      feedback=!prediction?"先預測：a 固定 8，只把 b 從 30 改到 "+b+"，斜率會變嗎？":prediction===2?"正確。兩線每增加 1 單位 x 都增加 8；整條線只上下平移 "+(b-30)+"。":"固定 a=8 時變化率不變；b 只控制 x=0 的起點與整條線的垂直位置。";
      table='<table class="mgs-table"><caption>同一個 x，每個輸出都平移相同差</caption><thead><tr><th>x</th><th>8x+30</th><th>8x+'+b+'</th><th>差</th></tr></thead><tbody>'+[0,2,4].map(v=>'<tr><td>'+v+'</td><td>'+(8*v+30)+'</td><td>'+(8*v+b)+'</td><td>'+(b-30)+'</td></tr>').join("")+'</tbody></table>';
    } else if(mode===2){
      const y1=18*x+30,y2=24*x;
      feedback=x===5?"交點證據一致：x=5 時兩方案都是 120；圖、表與等式 18x+30=24x 指向同一結果。":"目前 x="+x+" 時兩方案差 "+Math.abs(y1-y2)+"；移動 x 尋找價差 0，再用等式求精確值。";
      table='<table class="mgs-table"><caption>交點不是「看起來靠近」，而是同一 x 的輸出相等</caption><tbody><tr><th>方案甲</th><td>'+y1+'</td></tr><tr><th>方案乙</th><td>'+y2+'</td></tr><tr><th>價差</th><td>'+Math.abs(y1-y2)+'</td></tr></tbody></table>';
    } else {
      const y=-7*x+100;
      feedback=y>=0?"負斜率表示向右時水量下降；x="+x+" 時仍有 "+y+" 單位水量。":"代數可算出負值，但水量情境不允許；模型有效範圍在水量降到 0 以前。";
      table='<div class="mgs-equation"><strong>y=−7x+100</strong><p>每增加 1 單位時間，水量減少 7；截距 100 是初始水量。</p></div>';
    }
    const transferFeedback=!transfer?"最後確認：a 與 b 分別控制哪種幾何特徵？":transfer===1?"正確。a 是固定變化率／斜率，b 是 x=0 的初始值／y 截距。":"把同一個 x 的輸出差與 x=0 的值分開看：前者揭示 a，後者直接讀出 b。";
    return '<section class="mgs mgs-function" aria-label="一次函數參數 Visual-First 控制台">'+
      '<div class="mgs-task"><span>1 預測再操作</span><strong>'+esc(modeTitle)+'</strong><p>一次只改一個參數，圖、表、方程式同步。</p></div>'+
      select("f82Mode","探索模式",mode,[[0,"只改 a"],[1,"只改 b"],[2,"兩方案交點"],[3,"負斜率情境"]])+
      (mode===0?select("f82Prediction","什麼一定保持不變？",prediction,[[0,"先預測"],[1,"y 截距 30"],[2,"每增加 1 的費用差"],[3,"整條線的位置"]])+range("f82A","新的 a",a,4,18,1):
       mode===1?select("f82Prediction","a 固定 8 時，b 改變會？",prediction,[[0,"先預測"],[1,"改變斜率"],[2,"保持斜率、整線平移"],[3,"只改一個點"]])+range("f82B","新的 b",b,20,60,5):
       range("f82X","觀察 x",x,0,mode===2?8:14,1))+
      '<div class="mgs-two-col"><figure class="mgs-figure">'+functionSvg(mode,a,b,x)+'<figcaption>同一組座標尺度，避免靠視覺錯覺比較。</figcaption></figure>'+table+'</div>'+
      '<p class="mgs-feedback" aria-live="polite">'+esc(feedback)+'</p>'+
      '<div class="mgs-transfer"><span>2 遷移</span><strong>a 控制固定變化率；b 控制初始值</strong>'+
      select("f82Transfer","正確對應是？",transfer,[[0,"先判斷"],[1,"a→斜率，b→y 截距"],[2,"a→y 截距，b→斜率"]])+
      '<p class="mgs-feedback" aria-live="polite">'+esc(transferFeedback)+'</p></div></section>';
  };

  const pythSvg=(a,b,reveal)=>{
    const c2=a*a+b*b,c=Math.sqrt(c2);
    const sx=40,sy=220,scale=18,ax=sx,ay=sy-b*scale,bx=sx,by=sy,cx=sx+a*scale,cy=sy;
    const sqA=Math.min(118,a*a*2),sqB=Math.min(118,b*b*1.55),sqC=Math.min(118,c2*1.0);
    return '<svg viewBox="0 0 356 300" role="img" aria-label="直角三角形兩股 '+a+'、'+b+'；兩股平方和 '+c2+'，斜邊 '+c.toFixed(2)+'">'+
      '<polygon points="'+ax+','+ay+' '+bx+','+by+' '+cx+','+cy+'" class="mgs-triangle"/>'+
      '<path d="M'+bx+' '+(by-18)+' L'+(bx+18)+' '+(by-18)+' L'+(bx+18)+' '+by+'" class="mgs-right-angle"/>'+
      '<text x="'+(sx-12)+'" y="'+((ay+by)/2)+'" text-anchor="end">b='+b+'</text><text x="'+((bx+cx)/2)+'" y="'+(by+22)+'" text-anchor="middle">a='+a+'</text>'+
      (reveal?'<g class="mgs-square-cards"><rect x="215" y="36" width="110" height="58" rx="8"/><text x="270" y="60" text-anchor="middle">a² = '+(a*a)+'</text><text x="270" y="80" text-anchor="middle">b² = '+(b*b)+'</text><rect x="215" y="112" width="110" height="58" rx="8"/><text x="270" y="136" text-anchor="middle">c² = '+c2+'</text><text x="270" y="156" text-anchor="middle">c = √'+c2+'</text><path d="M225 194 H315" class="mgs-arrow"/><text x="270" y="218" text-anchor="middle">'+(a*a)+' + '+(b*b)+' = '+c2+'</text></g>':'<text x="260" y="90" class="mgs-question" text-anchor="middle">先比較平方「面積」</text>')+
      '</svg>';
  };
  const renderPythagorean=state=>{
    const prediction=Number(state.s86Prediction||0),a=Number(state.s86A||6),b=Number(state.s86B||8),transfer=Number(state.s86Transfer||0);
    const c2=a*a+b*b,c=Math.sqrt(c2);
    const predictionFeedback=!prediction?"先確認直角：a、b 是兩股，c 是直角對面的斜邊。再預測 6、8 的斜邊。":prediction===1?"正確。6²+8²=36+64=100，因此斜邊是正平方根 10。":"不要直接做 6+8，也不要把平方和忘記開根號；關係是兩個正方形面積的和。";
    const transferFeedback=!transfer?"反向問題：斜邊 13、一股 5，另一股用平方差求。":transfer===2?"正確。h²=13²−5²=169−25=144，所以 h=12；代回 5²+12²=13²。":"不要用 13−5；未知的是邊長，但定理連結的是三邊的平方。";
    return '<section class="mgs mgs-pythagorean" aria-label="畢氏定理平方面積模型">'+
      '<div class="mgs-task"><span>1 預測</span><strong>兩股 6、8，斜邊是多少？</strong><p>先標直角與三邊角色，再看平方「面積」關係。</p></div>'+
      select("s86Prediction","你的預測",prediction,[[0,"先預測"],[1,"10"],[2,"14"],[3,"√14"]])+
      '<p class="mgs-feedback" aria-live="polite">'+esc(predictionFeedback)+'</p>'+
      '<figure class="mgs-figure">'+pythSvg(a,b,prediction>0)+'<figcaption>'+esc(prediction?"a²+b²=c²；長度取正平方根。":"平方和與斜邊答案暫時隱藏。")+'</figcaption></figure>'+
      (prediction?'<div class="mgs-two-controls">'+range("s86A","股 a",a,3,9,1)+range("s86B","股 b",b,3,10,1)+'</div><div class="mgs-equation"><strong>'+a+'² + '+b+'² = '+c2+' = c²</strong><p>c=√'+c2+' ≈ '+c.toFixed(2)+'；且 c &lt; a+b = '+(a+b)+'。</p></div>':'')+
      '<div class="mgs-transfer"><span>2 反向遷移</span><strong>斜邊 13、一股 5，另一股？</strong>'+
      select("s86Transfer","h 是多少？",transfer,[[0,"先預測"],[1,"8"],[2,"12"],[3,"18"]])+
      '<p class="mgs-feedback" aria-live="polite">'+esc(transferFeedback)+'</p></div></section>';
  };

  const boxX=v=>32+(v-15)/25*292;
  const boxPlot=(name,min,q1,med,q3,max,y)=>{
    return '<g aria-label="'+name+' 五數摘要 '+[min,q1,med,q3,max].join("、")+'">'+
      '<line x1="'+boxX(min)+'" y1="'+y+'" x2="'+boxX(max)+'" y2="'+y+'" class="mgs-box-line"/>'+
      '<line x1="'+boxX(min)+'" y1="'+(y-13)+'" x2="'+boxX(min)+'" y2="'+(y+13)+'" class="mgs-box-line"/>'+
      '<line x1="'+boxX(max)+'" y1="'+(y-13)+'" x2="'+boxX(max)+'" y2="'+(y+13)+'" class="mgs-box-line"/>'+
      '<rect x="'+boxX(q1)+'" y="'+(y-23)+'" width="'+(boxX(q3)-boxX(q1))+'" height="46" class="mgs-box"/>'+
      '<line x1="'+boxX(med)+'" y1="'+(y-23)+'" x2="'+boxX(med)+'" y2="'+(y+23)+'" class="mgs-median"/>'+
      '<text x="8" y="'+(y+5)+'">'+name+'</text></g>';
  };
  const renderBoxPlot=state=>{
    const prediction=Number(state.d91Prediction||0),maxA=Number(state.d91MaxA||35),q3A=Number(state.d91Q3A||26),transfer=Number(state.d91Transfer||0);
    const minA=18,q1A=22,medA=24,minB=20,q1B=23,medB=24,q3B=25,maxB=29;
    const rangeA=maxA-minA,iqrA=q3A-q1A,rangeB=maxB-minB,iqrB=q3B-q1B;
    const feedback=!prediction?"中位數固定 24；只把甲站最大值從 30 拉到 35。先預測哪個統計量改變。":prediction===1?"正確。最大值改變會拉長右鬚與全距；Q1、Q3 不動，所以 IQR 仍是 4，中位數也不動。":"把『鬚端點』和『盒子端點』分開：最大值屬於鬚，IQR 只看 Q1 到 Q3。";
    const transferFeedback=!transfer?"再改盒子本身：若甲站 Q3 從 26 到 28，哪個量一定改變？":transfer===2?"正確。Q3 改變會直接改 IQR=Q3−Q1；中位數仍可維持 24。":"IQR 的兩個端點是 Q1、Q3；只要其中一個改變，IQR 就會改變。";
    return '<section class="mgs mgs-boxplot" aria-label="盒狀圖五數摘要與散布量探索">'+
      '<div class="mgs-task"><span>1 預測</span><strong>只改最大值，IQR 會跟著改嗎？</strong><p>中位數相同不代表散布相同；先分清鬚、盒子與中線。</p></div>'+
      select("d91Prediction","最大值 30→35 時？",prediction,[[0,"先預測"],[1,"全距變、IQR 不變"],[2,"全距與 IQR 都變"],[3,"兩者都不變"]])+
      '<p class="mgs-feedback" aria-live="polite">'+esc(feedback)+'</p>'+
      '<figure class="mgs-figure"><svg viewBox="0 0 356 220" role="img" aria-label="甲乙兩站盒狀圖；甲站全距 '+rangeA+'，IQR '+iqrA+'；乙站全距 '+rangeB+'，IQR '+iqrB+'">'+
      '<line x1="32" y1="186" x2="324" y2="186" class="mgs-axis"/>'+[15,20,25,30,35,40].map(v=>'<text x="'+boxX(v)+'" y="207" text-anchor="middle">'+v+'</text>').join("")+
      boxPlot("甲",minA,q1A,medA,q3A,maxA,70)+boxPlot("乙",minB,q1B,medB,q3B,maxB,140)+'</svg><figcaption>盒子代表中間 50%；鬚延伸到兩端。</figcaption></figure>'+
      (prediction?'<div class="mgs-two-controls">'+range("d91MaxA","甲站最大值",maxA,30,38,1)+range("d91Q3A","甲站 Q3",q3A,25,29,1)+'</div>':'')+
      '<div class="mgs-stat-cards"><article><b>甲站</b><span>中位數 24</span><span>全距 '+rangeA+'</span><span>IQR '+iqrA+'</span></article><article><b>乙站</b><span>中位數 24</span><span>全距 '+rangeB+'</span><span>IQR '+iqrB+'</span></article></div>'+
      '<p class="mgs-feedback">IQR 較小只支持「中間 50% 較集中」；不能推成「所有資料都一樣」。</p>'+
      '<div class="mgs-transfer"><span>2 遷移</span><strong>Q3 26→28，哪個量直接改變？</strong>'+
      select("d91Transfer","判斷",transfer,[[0,"先預測"],[1,"只有中位數"],[2,"IQR"],[3,"最小值"]])+
      '<p class="mgs-feedback" aria-live="polite">'+esc(transferFeedback)+'</p></div></section>';
  };

  const freqData={10:[7,.70],20:[12,.60],50:[27,.54],100:[51,.51],200:[101,.505]};
  const freqX=n=>48+(Math.log10(n)-1)/(Math.log10(200)-1)*260;
  const freqY=f=>190-(f-.4)/.35*140;
  const freqSvg=trials=>{
    const points=Object.entries(freqData).map(([n,v])=>[Number(n),v[1]]);
    const poly=points.map(([n,f])=>freqX(n)+","+freqY(f)).join(" ");
    const current=freqData[trials]||freqData[10];
    return '<svg viewBox="0 0 356 230" role="img" aria-label="可重現試驗資料的正面相對頻率；目前 '+trials+' 次為 '+current[1]+'">'+
      '<line x1="42" y1="196" x2="326" y2="196" class="mgs-axis"/><line x1="42" y1="28" x2="42" y2="196" class="mgs-axis"/>'+
      '<line x1="42" y1="'+freqY(.5)+'" x2="326" y2="'+freqY(.5)+'" class="mgs-half-line"/><text x="318" y="'+(freqY(.5)-6)+'" text-anchor="end">理論 0.5</text>'+
      '<polyline points="'+poly+'" class="mgs-freq-line"/>'+
      points.map(([n,f])=>'<g><circle cx="'+freqX(n)+'" cy="'+freqY(f)+'" r="'+(n===trials?7:4)+'" class="'+(n===trials?"mgs-final":"mgs-point")+'"/><text x="'+freqX(n)+'" y="216" text-anchor="middle">'+n+'</text></g>').join("")+
      '<text x="12" y="'+(freqY(.7)+4)+'">.70</text><text x="12" y="'+(freqY(.5)+4)+'">.50</text>'+
      '</svg>';
  };
  const renderProbability=state=>{
    const prediction=Number(state.d92Prediction||0),trials=Number(state.d92Trials||10),transfer=Number(state.d92Transfer||0);
    const [heads,freq]=freqData[trials]||freqData[10];
    const feedback=!prediction?"10 次出現 7 次正面。先判斷：這能不能單獨證明硬幣不公平？":prediction===2?"正確。7/10 是這一批資料的相對頻率 0.70；樣本很短，仍可能由隨機波動造成。":"不要把一次短期結果當成理論機率。要比較更多次試驗，看相對頻率的長期趨勢。";
    const transferFeedback=!transfer?"等面積轉盤：理論紅色 1/4，但 200 次只出現 48 次紅色。如何解讀？":transfer===1?"正確。48/200=0.24，與 0.25 很接近但不必完全相等；下一次結果仍不被前面結果強迫。":"理論機率不是命令實驗結果必須剛好 50 次；隨機試驗容許波動。";
    return '<section class="mgs mgs-probability" aria-label="機率相對頻率重複試驗模型">'+
      '<div class="mgs-task"><span>1 預測</span><strong>10 次擲硬幣有 7 次正面＝一定不公平？</strong><p>先分開「理論機率」與「這一批實驗的相對頻率」。</p></div>'+
      select("d92Prediction","你的判斷",prediction,[[0,"先預測"],[1,"一定不公平"],[2,"不能只靠 10 次斷定"]])+
      '<p class="mgs-feedback" aria-live="polite">'+esc(feedback)+'</p>'+
      (prediction?select("d92Trials","查看可重現的累積試驗資料",trials,[[10,"10 次"],[20,"20 次"],[50,"50 次"],[100,"100 次"],[200,"200 次"]]):"")+
      '<div class="mgs-two-col"><figure class="mgs-figure">'+freqSvg(trials)+'<figcaption>橫軸是累積試驗次數；虛線是公平硬幣理論值 0.5。</figcaption></figure>'+
      '<div class="mgs-prob-card"><b>'+trials+' 次</b><strong>'+heads+' 次正面</strong><span>相對頻率 = '+heads+'/'+trials+' = '+freq.toFixed(3)+'</span><p>試驗次數增加時，這組資料逐漸靠近 0.5；「靠近」不等於每次都恰好一半。</p></div></div>'+
      '<div class="mgs-transfer"><span>2 遷移</span><strong>轉盤 P(紅)=1/4；200 次觀察 48 次紅色</strong>'+
      select("d92Transfer","最合理的結論？",transfer,[[0,"先判斷"],[1,"0.24 接近 0.25，屬合理波動"],[2,"必須剛好 50 次才公平"],[3,"下一次一定紅色"]])+
      '<p class="mgs-feedback" aria-live="polite">'+esc(transferFeedback)+'</p></div></section>';
  };

  const defaults={
    "n-7-3-signed-operations-v1":{n73Prediction:0,n73Evidence:0,n73Transfer:0},
    "f-8-2-linear-parameter-v1":{f82Mode:0,f82A:8,f82B:50,f82X:5,f82Prediction:0,f82Transfer:0},
    "s-8-6-pythagorean-area-v1":{s86Prediction:0,s86A:6,s86B:8,s86Transfer:0},
    "d-9-1-boxplot-iqr-v1":{d91Prediction:0,d91MaxA:35,d91Q3A:26,d91Transfer:0},
    "d-9-2-relative-frequency-v1":{d92Prediction:0,d92Trials:10,d92Transfer:0},
  };
  const labels={
    "n-7-3-signed-operations-v1":"帶號運算數線稽核臺",
    "f-8-2-linear-parameter-v1":"一次函數參數控制台",
    "s-8-6-pythagorean-area-v1":"畢氏平方關係實驗室",
    "d-9-1-boxplot-iqr-v1":"盒狀圖散布探索臺",
    "d-9-2-relative-frequency-v1":"相對頻率實驗室",
  };
  const renderers={
    "n-7-3-signed-operations-v1":renderSigned,
    "f-8-2-linear-parameter-v1":renderFunction,
    "s-8-6-pythagorean-area-v1":renderPythagorean,
    "d-9-1-boxplot-iqr-v1":renderBoxPlot,
    "d-9-2-relative-frequency-v1":renderProbability,
  };
  const goldRegistry = window.MathSemanticFamilies ||= {};
  const goldAdapter = model => (host) => {
    const defaultsForModel = {...defaults[model]};
    host.innerHTML = renderers[model](defaultsForModel);
    host.addEventListener("change", event => {
      const control = event.target.closest("[data-sim-control]");
      if (!control) return;
      const key = control.dataset.simControl;
      const raw = control.value;
      defaultsForModel[key] = raw === "" ? raw : Number.isNaN(Number(raw)) ? raw : Number(raw);
      host.innerHTML = renderers[model](defaultsForModel);
    });
    host.addEventListener("input", event => {
      const control = event.target.closest("[data-sim-control]");
      if (!control) return;
      const key = control.dataset.simControl;
      const raw = control.value;
      defaultsForModel[key] = raw === "" ? raw : Number.isNaN(Number(raw)) ? raw : Number(raw);
      host.innerHTML = renderers[model](defaultsForModel);
    });
  };
  for (const model of allModels) goldRegistry[model] = goldAdapter(model);
})();