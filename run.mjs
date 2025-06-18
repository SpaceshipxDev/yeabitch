import ExcelJS from "exceljs";
import { fileURLToPath } from "url";
import { dirname, resolve } from "path";

// 1️⃣  Define schema (column order) and fake header
const FIELDS = [
  "销售单号*", "客户名称*", "联系人", "联系方式", "客户原始单号",
  "要求交货日期", "交货方式", "包装要求", "结算方式", "价格单位", "订单备注",
  "产品编号", "产品名称*", "产品类型*", "单位*", "销售数量*", "加工方式",
  "销售单价", "产品备注", "加工", "工艺要求", "客户料号", "规格", "材料", "备注",
];
const ROW1 = ["#订单信息", ...Array(11).fill(""), "产品信息", ...Array(12).fill("")];

// 2️⃣  Your data (edit/add as needed)
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
  // Add more objects...
];

// 3️⃣  Create the workbook and worksheet
const workbook = new ExcelJS.Workbook();
const sheet = workbook.addWorksheet("ERP导入");

// --- Insert first header row (fake header) ---
sheet.addRow(ROW1);

// --- Insert real header row (column names) ---
sheet.addRow(FIELDS);

// --- Insert data rows ---
for (const rec of data) {
  // Sanity check: required fields
  for (const req of ["销售单号*", "客户名称*", "产品名称*", "产品类型*", "单位*", "销售数量*"]) {
    if (!rec[req]) throw new Error(`Missing required field: ${req}`);
  }
  sheet.addRow(FIELDS.map((f) => rec[f] ?? ""));
}

// --- Optionally: set column widths for readability ---
FIELDS.forEach((_, i) => sheet.getColumn(i + 1).width = 18);

// 4️⃣  Save the file
const __dirname = dirname(fileURLToPath(import.meta.url));
const outPath = resolve(__dirname, "erp_import_ready.xlsx");
await workbook.xlsx.writeFile(outPath);

console.log("✅  Excel file written:", outPath);