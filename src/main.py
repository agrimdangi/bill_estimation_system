```python
import pandas as pd
import os

# Create output folder
if not os.path.exists("output"):
    os.makedirs("output")

# Load product data
df = pd.read_excel("data/products.xlsx")

print("\n📌 Product Data:")
print(df)

# -------------------------------
# 🧮 CALCULATIONS
# -------------------------------

# Calculate total for each item
df["Total"] = df["Price"] * df["Quantity"]

# Calculate grand total
grand_total = df["Total"].sum()

# -------------------------------
# 🧾 DISPLAY BILL
# -------------------------------

print("\n🧾 BILL SUMMARY:")
for index, row in df.iterrows():
    print(f"{row['Product']} -> ₹{row['Total']}")

print(f"\n💰 Grand Total: ₹{grand_total}")

# -------------------------------
# 💾 SAVE BILL TO EXCEL
# -------------------------------

df.loc["Total"] = ["", "", "", grand_total]
df.to_excel("output/final_bill.xlsx", index=False)

print("\n✅ Bill saved as 'output/final_bill.xlsx'")
```
