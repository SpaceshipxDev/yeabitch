import csv
from pathlib import Path

# ---------- 1️⃣  Build the two header rows ----------
# Row 1 has 25 columns: "#订单信息" + 11 blanks + "产品信息" + 12 blanks
header_row_1 = ["#订单信息"] + [""] * 11 + ["产品信息"] + [""] * 12

# Row 2: copy **exactly** from the template (asterisks mark required fields)
header_row_2 = [
    "销售单号*", "客户名称*", "联系人", "联系方式", "客户原始单号",
    "要求交货日期", "交货方式", "包装要求", "结算方式", "价格单位", "订单备注",
    "产品编号", "产品名称*", "产品类型*", "单位*", "销售数量*", "加工方式",
    "销售单价", "产品备注", "加工", "工艺要求", "客户料号", "规格", "材料", "备注",
]

# ---------- 2️⃣  Add your data rows ----------
# Each row must also have 25 columns, in the same order as header_row_2
rows = [
    [
        "BJD-20250618151413",  # 销售单号*
        "Apple Inc",           # 客户名称*
        "", "", "", "",        # 联系人, 联系方式, 客户原始单号, 要求交货日期, 交货方式
        "", "", "", "",        # 包装要求, 结算方式, 价格单位, 订单备注
        "cuban chain-20250618151413",   # 产品编号
        "cuban chain",         # 产品名称*
        "成品",                # 产品类型*
        "件",                  # 单位*
        7,                     # 销售数量*
        "", "", "",            # 加工方式, 销售单价, 产品备注
        "", "",                # 加工, 工艺要求
        "",                    # 客户料号
        "6mm wide anodized rhodium finish",  # 规格
        "sterling silver",     # 材料
        "",                    # 备注
    ],
    # ⇧⇧  Add more rows as needed, always keeping 25 columns ⇧⇧
]

# ---------- 3️⃣  Write the CSV ----------
out_file = Path("erp_import_ready.csv")
with out_file.open("w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header_row_1)
    writer.writerow(header_row_2)
    writer.writerows(rows)

print(f"Saved → {out_file.resolve()}")