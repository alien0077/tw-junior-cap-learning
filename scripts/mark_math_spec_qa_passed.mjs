import { readdir, readFile, writeFile } from "node:fs/promises";

const root = new URL("../", import.meta.url);
const dir = new URL("implementation/unit-specs/math/", root);
const files = (await readdir(dir)).filter(name => name.endsWith(".yaml")).sort();
let changed = 0;
let alreadyPassed = 0;
let nonImplemented = 0;

for (const file of files) {
  const url = new URL(file, dir);
  const source = await readFile(url, "utf8");
  const implementationStatus = source.match(/^\s*implementationStatus:\s*([^\n#]+)/m)?.[1]?.trim().replace(/^['"]|['"]$/g, "");
  const qaStatus = source.match(/^\s*qaStatus:\s*([^\n#]+)/m)?.[1]?.trim().replace(/^['"]|['"]$/g, "");
  if (implementationStatus !== "implemented") {
    nonImplemented += 1;
    continue;
  }
  if (qaStatus === "passed") {
    alreadyPassed += 1;
    continue;
  }
  if (!qaStatus) throw new Error(`${file}: missing qaStatus`);
  const updated = source.replace(/^(\s*qaStatus:\s*)([^\n#]+)(.*)$/m, "$1passed$3");
  if (updated === source) throw new Error(`${file}: failed to update qaStatus`);
  await writeFile(url, updated, "utf8");
  changed += 1;
}

console.log(JSON.stringify({ files: files.length, changed, alreadyPassed, nonImplemented }));
