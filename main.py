"""
make_erp_csv.py
Convert a list of JSON-style records → ERP-ready CSV
"""

import csv
from pathlib import Path
from typing import List, Dict

# 1️⃣  Fixed schema = column order in the second header row
FIELDS: List[str] = [
    "销售单号*", "客户名称*", "联系人", "联系方式", "客户原始单号",
    "要求交货日期", "交货方式", "包装要求", "结算方式", "价格单位", "订单备注",
    "产品编号", "产品名称*", "产品类型*", "单位*", "销售数量*", "加工方式",
    "销售单价", "产品备注", "加工", "工艺要求", "客户料号", "规格", "材料", "备注",
]

# 2️⃣  Header row 1 (split between order + product info)
ROW1 = ["#订单信息"] + [""] * 11 + ["产品信息"] + [""] * 12

# 3️⃣  Your data, e.g. loaded from a JSON file / API
DATA: List[Dict[str, str]] = [
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
        # any field you omit will be left blank automatically
    },
    # add more dicts as needed…
]

def write_erp_csv(rows: List[Dict[str, str]], out_path: Path = Path("erp_import_ready.csv")):
    """
    Convert list[dict] -> ERP CSV. Missing keys become empty strings.
    """
    with out_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(ROW1)        # header row 1
        w.writerow(FIELDS)      # header row 2
        for record in rows:
            # Ensure each row has 25 columns in the required order
            w.writerow([record.get(col, "") for col in FIELDS])
    print(f"✅  Saved {out_path.resolve()}")

if __name__ == "__main__":
    write_erp_csv(DATA)