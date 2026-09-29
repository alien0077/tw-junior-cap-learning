import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const lesson = JSON.parse(readFileSync(new URL('../../lessons/math/lesson-math-content-s-9-13.json', import.meta.url), 'utf8'));
const sections = lesson.content.sections;
const joined = sections.map(({ heading, body }) => `${heading}\n${body}`).join('\n');

assert.equal(lesson.id, 'lesson-math-content-s-9-13');
assert.equal(sections.length, 6, '學生頁應呈現完整、單元專屬的六段教材，不可只剩三句摘要');
assert.deepEqual(lesson.teaching.body.map(({ heading, body }) => ({ heading, body })), sections, '教學原稿與融合正文必須一致，避免學生頁重複顯示兩套內容');
assert.ok(sections.every(({ body }) => body.length >= 150), '每段可見正文須包含可教學的解釋或推理');
assert.match(joined, /平方單位/);
assert.match(joined, /立方單位/);
assert.match(joined, /8×15÷2＝60/);
assert.match(joined, /3×\(8＋15＋17\)＝120/);
assert.match(joined, /60×3＝180/);
assert.match(joined, /8π×7÷2＝28π/);
assert.match(joined, /44π/);
assert.doesNotMatch(joined, /3×4÷2|3-4-5|5-12-13|柱高.*10 公分/);
assert.match(joined, /4×（6×5÷2）＝60/);
assert.match(joined, /96 平方公分/);
assert.match(joined, /沒有底板/);
assert.ok(joined.indexOf('正角錐：底面加上逐片三角形側面') < joined.indexOf('圓錐：扇形的弧長要接回底圓'), '可讀來源啟發的課程順序應由多邊形面逐片計算，推進到扇形弧長接合底圓');
assert.doesNotMatch(joined, /圓錐體積公式|正角錐體積公式/);
assert.ok(lesson.studyReferences.includes('https://www.ehanlin.com.tw/app/keyword/%E5%9C%8B%E4%B8%AD/%E6%95%B8%E5%AD%B8/%E8%A7%92%E6%9F%B1.html'));
assert.ok(lesson.studyReferences.includes('https://www.ehanlin.com.tw/app/keyword/%E5%9C%8B%E4%B8%AD/%E6%95%B8%E5%AD%B8/%E5%9C%93%E9%8C%90.html'));
assert.ok(lesson.studyReferences.some((url) => url.includes('digitalmaster.knsh.com.tw')));
assert.equal(lesson.interactive.steps[0].answer, 'B', '柱長變化題的答案需符合逐面與體積計算');
assert.equal(lesson.interactive.steps[3].answer, 'B', '7-24-25遷移題答案需符合表面積280與體積168');
assert.equal(lesson.simulation.prismModel.baseTriangle.hypotenuse, 17);
assert.ok(lesson.fusionRecord.llmSynthesisNote.includes('多邊形面到曲面展開'));
assert.equal(lesson.reviewStatus, 'draft', '自動化與版本研究草稿不得升級為內容審查通過');

console.log('PASS S-9-13 visible lesson scope, worked calculations, misconception repair, transfer, and draft gate');
