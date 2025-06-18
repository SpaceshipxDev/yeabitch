import pandas as pd
import io

# ==============================================================================
# 1. DEFINE THE EXACT HEADER STRUCTURE FROM YOUR EXAMPLE
# ==============================================================================

# This is the first merged header line from your example
merged_header_line = "订单信息,,,,,,,,,,产品信息,,,,,,,,,,,,,,"

# These are the column headers from the second line of your example
# Note: I've removed the '*' characters as they are not part of the data
column_headers = [
    "销售单号","客户名称","联系人","联系方式","客户原始单号","要求交货日期","交货方式","包装要求","结算方式","价格单位","订单备注",
    "产品编号","产品名称","产品类型","单位","销售数量","加工方式","销售单价","产品备注","加工","工艺要求","客户料号","规格","材料","备注"
]

# ==============================================================================
# 2. PROCESS THE USER INPUT TEXT BASED ON YOUR EXPLICIT RULES
# ==============================================================================

# Original User Input Text:
# "cuban-chain-01, cuban chain, 6mm wide, sterling silver, anodized rhodium finish, need 7 of this 
# company name: Apple Inc"

# Apply the explicit rules to the input text:
sales_order_id = "BJD-20250618151413"        # Rule: Always set to this exact value.
customer_name = "Apple Inc"                  # Extracted from "company name: Apple Inc"
product_name = "cuban chain"                 # Extracted from input.
product_id = "cuban chain-20250618151413"    # Rule: <产品名称>-<timestamp>
quantity = "7"                               # Extracted from "need 7 of this".
unit = "件"                                  # Rule: Always "件".
specifications = "6mm wide, anodized rhodium finish" # Extracted from input.
material = "sterling silver"                 # Extracted from input.

# ==============================================================================
# 3. CONSTRUCT THE DATA ROW
# ==============================================================================

# This list matches the order of the column_headers.
# Fields are left empty "" unless a value was extracted or specified by a rule.
data_row = [
    sales_order_id,          # 销售单号
    customer_name,           # 客户名称
    "",                      # 联系人
    "",                      # 联系方式
    "",                      # 客户原始单号
    "",                      # 要求交货日期
    "",                      # 交货方式
    "",                      # 包装要求
    "",                      # 结算方式
    "",                      # 价格单位
    "",                      # 订单备注
    product_id,              # 产品编号
    product_name,            # 产品名称
    "",                      # 产品类型
    unit,                    # 单位
    quantity,                # 销售数量
    "",                      # 加工方式
    "",                      # 销售单价
    "",                      # 产品备注
    "",                      # 加工
    "",                      # 工艺要求
    "",                      # 客户料号
    specifications,          # 规格
    material,                # 材料
    ""                       # 备注
]

# ==============================================================================
# 4. CREATE PANDAS DATAFRAME AND GENERATE THE CSV FILE
# ==============================================================================

# Create the DataFrame with our single row of data
df = pd.DataFrame([data_row], columns=column_headers)

# Define the output filename
output_filename = 'order_output.csv'

# To create the two-line header, we write the first line manually,
# then we use pandas to write the second header and the data.
try:
    # Open the file for writing, using 'utf-8-sig' for Excel compatibility
    with open(output_filename, 'w', encoding='utf-8-sig', newline='') as f:
        # Manually write the first, merged header line
        f.write(merged_header_line + '\n')
        
        # Use pandas to_csv to write the column headers and the data row
        # We set `header=True` to include the column names from the DataFrame.
        df.to_csv(f, index=False, header=True)
        
    print(f"Successfully generated CSV file: {output_filename}")
    print("\n--- File Content Preview ---")
    with open(output_filename, 'r', encoding='utf-8-sig') as f:
        print(f.read())

except Exception as e:
    print(f"An error occurred while writing the file: {e}")