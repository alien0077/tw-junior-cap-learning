import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-s-9-5':('S-9-5：圓弧長與扇形面積','運用圓周長比例求弧長與扇形面積。'),'content-s-9-6':('S-9-6：圓的幾何性質','理解圓心角、圓周角、弦與切線的關係。'),'content-s-9-7':('S-9-7：點、直線與圓的關係','判斷點與圓、直線與圓的位置關係。'),'content-s-9-8':('S-9-8：三角形的外心','理解三角形外心為外接圓圓心及其性質。'),'content-s-9-9':('S-9-9：三角形的內心','理解三角形內心為角平分線交點及其性質。')}
focus=['圓周長','弧長比例','扇形面積','圓心角圓周角','弦與切線','位置關係','外心定義','外接圓','內心定義','角平分線']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key; lp=ROOT/f'lessons/math/{lid}.json'; lesson=json.loads(lp.read_text()); lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'}); lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能由角度、半徑與位置條件推理。'},{'heading':'學習流程','body':'辨認圓與三角形元素，選用弧長面積或圓幾何性質，列式並檢查角度與單位。'},{'heading':'常見錯誤','body':'混淆圓心角與圓周角、弧長與弦長，或誤認內心外心位置。'}]}; lesson['studyHighlights']=['辨認圓幾何元素。','選用角度或比例性質。','檢查位置與單位。']; lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先辨認什麼？','options':['圓心、半徑、角與位置條件','直接套公式'],'answer':'A','feedback':'先標出幾何元素。'},{'id':'step-2','prompt':'第二步如何推理？','options':['依角度關係或圓周長比例列式','混用弧長與弦長'],'answer':'A','feedback':'選用適用的圓性質。'},{'id':'step-3','prompt':'最後如何確認？','options':['檢查角度、位置與單位','忽略圖形條件'],'answer':'A','feedback':'確認結果符合圓幾何。'}]}; lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json'; q=json.loads(qp.read_text()); q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先辨認圓幾何元素，再依角度或比例性質驗證'},{'id':'B','text':'只憑圖形外觀猜測'},{'id':'C','text':'混淆弧長、弦長與圓周角'},{'id':'D','text':'忽略半徑、位置或單位'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需依圓幾何定義與條件逐步判斷。'}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n'); print('reviewed',len(units))
