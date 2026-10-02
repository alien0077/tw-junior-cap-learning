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
})();