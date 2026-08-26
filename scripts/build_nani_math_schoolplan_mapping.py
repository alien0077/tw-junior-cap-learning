import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
url='https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf'
titles={'F-9-1':'二次函數的意義','F-9-2':'二次函數的圖形與極值','D-9-1':'統計數據的分布','D-9-2':'認識機率','D-9-3':'古典機率','S-9-12':'空間中的線與平面','S-9-13':'表面積與體積','S-9-1':'相似形','S-9-2':'三角形的相似性質','S-9-3':'平行線截比例線段','S-9-4':'相似直角三角形邊長比值的不變性','S-9-5':'圓弧長與扇形面積','S-9-6':'圓的幾何性質','S-9-7':'點、直線與圓的關係','S-9-8':'三角形的外心','S-9-9':'三角形的內心','S-9-10':'三角形的重心','S-9-11':'證明的意義'}
def entry(code):
    return {'chapterCode':code,'chapterLabel':titles[code],'knowledgeIds':[f'kg-math-content-{code.lower()}'],'relation':'primary','confidence':'medium','notes':'校方課程計畫明列南一版教材與課綱代碼；章節編排仍須與出版社正式目次交叉核驗。'}
m={'id':'mapset-math-nani-schoolplan-2026','subject':'math','publisher':'nani','academicYear':'115','source':{'type':'book-inspection','url':url,'locator':'桃園市永豐高中國中部數學領域課程計畫；南一版國中數學9上／9下教材段落與 S/F/D 課綱代碼','verifiedAt':'2026-08-26','verifiedBy':'Codex public-source verification','confidence':'medium','editionNote':'校方公開課程計畫作為交叉證據；不等同南一出版社官方章節目次。'},'mappingMethod':'school-curriculum-plan-to-official-curriculum-kg-conservative-cross-reference','volumes':[{'volume':'5','grade':'9','semester':'上','entries':[entry(c) for c in ['S-9-1','S-9-2','S-9-3','S-9-4','S-9-5','S-9-6','S-9-7','S-9-8','S-9-9','S-9-10','S-9-11']]},{'volume':'6','grade':'9','semester':'下','entries':[entry(c) for c in ['F-9-1','F-9-2','D-9-1','D-9-2','D-9-3','S-9-12','S-9-13']]}],'status':'verified','notes':'僅保存最小必要章節／課綱代碼與來源定位；未擷取教材內文。'}
(ROOT/'textbook-mapping/math/nani-schoolplan-2026.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n'); print('wrote',len(titles),'entries')
