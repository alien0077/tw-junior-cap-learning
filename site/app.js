const names={chinese:"國文",english:"英文",math:"數學",science:"自然",social:"社會"},$=id=>document.getElementById(id),S={index:null,subject:"all",query:"",page:1},PAGE=24;
const h=x=>String(x??"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
async function json(url){const r=await fetch(url);if(!r.ok)throw new Error(url+" ("+r.status+")");return r.json()}
function all(){const q=S.query.trim().toLocaleLowerCase();return S.index.lessons.filter(x=>(S.subject==="all"||x.subject===S.subject)&&(!q||[x.title,x.summary,...x.knowledgeIds].join(" ").toLocaleLowerCase().includes(q)))}
function content(){const a=all(),n=Math.max(1,Math.ceil(a.length/PAGE));S.page=Math.min(S.page,n);const page=a.slice((S.page-1)*PAGE,S.page*PAGE);$("contentGrid").innerHTML=page.length?page.map(x=>'<article class="card"><span class="tag">'+h(names[x.subject])+' · 教材</span><h3>'+h(x.title)+'</h3><p>'+h(x.summary)+'</p><small>'+x.questionPaths.length+' 題練習 · KG：'+h(x.knowledgeIds.join("、"))+'</small><button data-id="'+h(x.id)+'">閱讀教材與練習</button></article>').join(""):'<article class="card"><p>沒有符合條件的教材。</p></article>';$("resultCount").textContent="符合 "+a.length+" 筆，第 "+S.page+"/"+n+" 頁";$("previousPage").disabled=S.page===1;$("nextPage").disabled=S.page===n}
function mappings(){$("mappingGrid").innerHTML=S.index.mappings.map(x=>'<article class="card"><span class="tag">'+h(names[x.subject])+" · "+h(x.publisher)+'</span><h3>'+h(x.academicYear)+' 學年度版本對照</h3><p>'+x.volumeCount+" 冊 · "+x.entryCount+' 個章節／單元</p><small>證據：'+h(x.source.type)+"；信心："+h(x.source.confidence)+'</small><p><a href="'+h(x.source.url)+'" target="_blank" rel="noreferrer">查看公開來源 ↗</a></p></article>').join("");$("mappingCount").textContent="顯示 "+S.index.mappings.length+" 組"}
function stats(){const c=S.index.project.dataCounts;$("statNodes").textContent=Number(c.knowledgeNodes||0).toLocaleString();$("statLessons").textContent=Number(S.index.project.activeLessons||0).toLocaleString();$("statQuestions").textContent=Number(S.index.project.activeQuestions||0).toLocaleString();$("statMappings").textContent=Number(c.textbookChapterEntries||0).toLocaleString()}
function question(q,i){const choices=(q.options||[]).map(o=>"<li><strong>"+h(o.id)+".</strong> "+h(o.text)+"</li>").join("");return '<details class="question"><summary>第 '+i+" 題："+h(q.prompt)+"</summary>"+(choices?"<ol>"+choices+"</ol>":"")+"<p><strong>答案：</strong>"+h(q.answer.value)+"</p><p>"+h(q.answer.explanation)+"</p></details>"}
async function open(id){const item=S.index.lessons.find(x=>x.id===id),panel=$("detailPanel");if(!item)return;panel.hidden=false;panel.innerHTML='<article class="card"><p>正在載入教材與練習題…</p></article>';panel.scrollIntoView({behavior:"smooth",block:"start"});try{const a=await Promise.all([json(S.index.sourceBase+item.path),...item.questionPaths.map(path=>json(S.index.sourceBase+path))]),lesson=a[0],qs=a.slice(1),sections=lesson.content.sections.map(x=>"<section><h3>"+h(x.heading)+"</h3><p>"+h(x.body)+"</p></section>").join(""),points=(lesson.studyHighlights||[]).map(x=>"<li>"+h(x)+"</li>").join("");panel.innerHTML='<article class="card detail"><button data-close>關閉</button><span class="tag">'+h(names[lesson.subject])+' · 原創教材</span><h2>'+h(lesson.title)+"</h2><p>"+h(lesson.content.summary)+"</p>"+sections+(points?'<section class="highlights"><h3>學霸筆記</h3><ul>'+points+"</ul></section>":"")+'<section><h3>練習題（'+qs.length+" 題）</h3>"+qs.map(question).join("")+'</section><p><a href="'+h(S.index.sourceBase+item.path)+'" target="_blank" rel="noreferrer">查看這筆 JSON 資料 ↗</a></p></article>'}catch(e){panel.innerHTML='<article class="card error"><p>教材資料載入失敗：'+h(e.message)+"</p></article>"}}
async function start(){try{S.index=await json("./data-index.json");if(S.index.version!==2||!S.index.sourceRevision||S.index.sourceRevision==="main")throw new Error("資料索引不是固定版本，已拒絕載入");stats();content();mappings();$("status").textContent="資料載入完成 · "+S.index.project.updatedAt+" · 固定版本 "+S.index.sourceRevision.slice(0,12)}catch(e){$("status").textContent="資料載入失敗";$("status").classList.add("error");$("contentGrid").innerHTML='<article class="card error"><p>'+h(e.message)+"</p></article>"}}
$("subject").addEventListener("change",e=>{S.subject=e.target.value;S.page=1;content()});$("search").addEventListener("input",e=>{S.query=e.target.value;S.page=1;content()});$("previousPage").addEventListener("click",()=>{S.page--;content()});$("nextPage").addEventListener("click",()=>{S.page++;content()});$("contentGrid").addEventListener("click",e=>{const b=e.target.closest("[data-id]");if(b)open(b.dataset.id)});$("detailPanel").addEventListener("click",e=>{if(e.target.matches("[data-close]")){$("detailPanel").hidden=true;$("detailPanel").innerHTML=""}});start();

function fullTeaching(lesson){
  if(!lesson.teaching)return lesson.content.sections.map(section=>`<section><h3>${h(section.heading)}</h3><p>${h(section.body)}</p></section>`).join("");
  const body=lesson.teaching.body.map(block=>`<section class="lesson-block phase-${h(block.phase)}"><p class="phase-label">${h(block.phase.replace(/-/g," "))}</p><h3>${h(block.heading)}</h3><p>${h(block.body)}</p></section>`).join("");
  const summary=lesson.teaching.summary.map(point=>`<li>${h(point)}</li>`).join("");
  const exitCheck=lesson.teaching.exitCheck.map((item,index)=>`<li><strong>${index+1}.</strong> ${h(item.prompt)}<br><span>${h(item.expectedEvidence)}</span></li>`).join("");
  return `${body}<section class="highlights"><h3>摘要重點</h3><ul>${summary}</ul></section><section class="exit-check"><h3>離堂自我檢核</h3><ol>${exitCheck}</ol></section>`;
}

function fullActivity(lesson){
  const interactive=lesson.interactive;if(!interactive?.steps?.length)return "";
  const variables=(interactive.variables||[]).map(item=>`<li><strong>${h(item.symbol)}</strong>：${h(item.meaning)}</li>`).join("");
  const steps=interactive.steps.map((step,index)=>`<section class="activity-step"><h4>步驟 ${index+1}</h4><p>${h(step.prompt)}</p><div class="activity-options">${step.options.map((option,optionIndex)=>`<button data-activity-answer="${h(step.answer)}" data-choice="${String.fromCharCode(65+optionIndex)}" data-feedback="${h(step.feedback)}">${String.fromCharCode(65+optionIndex)}. ${h(option)}</button>`).join("")}</div><output class="feedback" aria-live="polite"></output></section>`).join("");
  return `<section class="activity"><p class="phase-label">互動活動</p><h3>${h(interactive.goal)}</h3>${interactive.scenario?`<p>${h(interactive.scenario)}</p>`:""}${variables?`<ul>${variables}</ul>`:""}${steps}</section>`;
}

function research(lesson){
  if(!lesson.publisherResearch?.length)return "";
  const sources=lesson.publisherResearch.map(item=>`<li><a href="${h(item.sourceUrl)}" target="_blank" rel="noreferrer">${h(item.publisher)}：${h(item.chapterLocator)} ↗</a><br><span>${h(item.outcome)}</span></li>`).join("");
  return `<details class="research"><summary>出版社教材研究來源（不重製教材）</summary><ul>${sources}</ul></details>`;
}

function gradeActivity(button){
  const step=button.closest(".activity-step"),correct=button.dataset.choice===button.dataset.activityAnswer;
  step.querySelectorAll("button").forEach(candidate=>{candidate.disabled=true;candidate.classList.toggle("correct",candidate.dataset.choice===candidate.dataset.activityAnswer);candidate.classList.toggle("wrong",candidate===button&&!correct)});
  step.querySelector(".feedback").textContent=`${correct?"答對了。":"再看一次。"} ${button.dataset.feedback}`;
}

async function openFull(id){
  const item=S.index.lessons.find(candidate=>candidate.id===id),panel=$("detailPanel");if(!item)return;
  panel.hidden=false;panel.innerHTML='<article class="card"><p>正在載入教材與練習題…</p></article>';panel.scrollIntoView({behavior:"smooth",block:"start"});
  try{const loaded=await Promise.all([json(S.index.sourceBase+item.path),...item.questionPaths.map(path=>json(S.index.sourceBase+path))]),lesson=loaded[0],questions=loaded.slice(1),points=(lesson.studyHighlights||[]).map(point=>`<li>${h(point)}</li>`).join(""),lead=lesson.teaching?"":`<p class="lesson-lede">${h(lesson.content.summary)}</p>`;
    panel.innerHTML=`<article class="card detail"><button data-close>關閉</button><span class="tag">${h(names[lesson.subject])} · ${lesson.authoringStandard==="full-lesson-v1"?"完整自編教材":"原創教材"}</span><h2>${h(lesson.title)}</h2>${fullTeaching(lesson)}${fullActivity(lesson)}${research(lesson)}${points?`<section class="highlights"><h3>學霸筆記</h3><ul>${points}</ul></section>`:""}<section><h3>練習題（${questions.length} 題）</h3>${questions.map((questionItem,index)=>question(questionItem,index+1)).join("")}</section><p><a href="${h(S.index.sourceBase+item.path)}" target="_blank" rel="noreferrer">查看這筆 JSON 資料 ↗</a></p></article>`;
  }catch(error){panel.innerHTML=`<article class="card error"><p>教材資料載入失敗：${h(error.message)}</p></article>`}
}

// The legacy bubble listener remains registered above; redirect it so full lessons
// cannot be overwritten by the outline renderer after the capture listener runs.
open=openFull;

$("contentGrid").addEventListener("click",event=>{const button=event.target.closest("[data-id]");if(!button)return;event.stopImmediatePropagation();openFull(button.dataset.id)},true);
$("detailPanel").addEventListener("click",event=>{if(event.target.matches("[data-activity-answer]"))gradeActivity(event.target)});
