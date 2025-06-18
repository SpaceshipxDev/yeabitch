// run.mjs
import { writeFile } from "fs/promises";
import { fileURLToPath } from "url";
import { dirname, resolve } from "path";

// ---------- 1️⃣ Schema setup ----------
const FIELDS = [
  "销售单号*", "客户名称*", "联系人", "联系方式", "客户原始单号",
  "要求交货日期", "交货方式", "包装要求", "结算方式", "价格单位", "订单备注",
  "产品编号", "产品名称*", "产品类型*", "单位*", "销售数量*", "加工方式",
  "销售单价", "产品备注", "加工", "工艺要求", "客户料号", "规格", "材料", "备注",
];

const ROW1 = ["#订单信息", ...Array(11).fill(""), "产品信息", ...Array(12).fill("")];

// ---------- 2️⃣ CSV escape helper ----------
const esc = (val = "") => {
  const s = String(val ?? "");
  return s.includes('"') || s.includes(",") || s.includes("\n")
    ? `"${s.replace(/"/g, '""')}"`
    : s;
};

const rowToCsv = (arr) => arr.map(esc).join(",");

// ---------- 3️⃣ Main function ----------
function makeErpCsv(records) {
  const lines = [];
  lines.push(rowToCsv(ROW1));
  lines.push(rowToCsv(FIELDS));
  for (const rec of records) {
    // optional: sanity check for required fields
    for (const req of ["销售单号*", "客户名称*", "产品名称*", "产品类型*", "单位*", "销售数量*"]) {
      if (!rec[req]) throw new Error(`Missing required field: ${req}`);
    }
    lines.push(rowToCsv(FIELDS.map((f) => rec[f] ?? "")));
  }
  return lines.join("\r\n");
}

// ---------- 4️⃣ Example data ----------
const data = [
  {
    "销售单号*": "BJD-20250618151413",
    "客户名称*": "Apple Inc",
    "产品编号": "cuban chain-20250618151413",
    "产品名称*": "cuban chain",
    "产品类型*": "成品",
    "单位*": "件",
    "销售数量*": 7,
    "规格": "6mm wide anodized rhodium finish",
    "材料": "sterling silver",
  },
  // Add more objects as needed
];

// ---------- 5️⃣ Output ----------
const __dirname = dirname(fileURLToPath(import.meta.url));
const outPath = resolve(__dirname, "erp_import_ready.csv");

const csv = makeErpCsv(data);

await writeFile(outPath, csv, { encoding: "utf8" });

console.log("✅  CSV written:", outPath);