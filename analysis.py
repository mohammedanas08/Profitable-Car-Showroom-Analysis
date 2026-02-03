import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (tab-separated CSV)
df = pd.read_csv("data/car_sales.csv", sep="\t")

print("\nRaw Data Loaded:\n")
print(df)

# Remove completely empty rows
df = df.dropna(how="all")

# Ensure correct data types
df["Units_Sold"] = df["Units_Sold"].astype(int)
df["Profit_Per_Car"] = df["Profit_Per_Car"].astype(int)

# Calculate Monthly Profit
df["Monthly_Profit"] = df["Units_Sold"] * df["Profit_Per_Car"]

print("\nCleaned Data with Monthly Profit:\n")
print(df)

# Find the most profitable car model
most_profitable = df.loc[df["Monthly_Profit"].idxmax()]

print("\nMost Profitable Car Model:")
print(f"Model: {most_profitable['Model']}")
print(f"Monthly Profit: ₹{most_profitable['Monthly_Profit']:,}")

# -------------------------------
# BAR CHART: Monthly Profit
# -------------------------------
plt.figure(figsize=(8, 5))
plt.bar(df["Model"], df["Monthly_Profit"])
plt.title("Monthly Profit by Car Model")
plt.xlabel("Car Model")
plt.ylabel("Monthly Profit (₹)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# -------------------------------
# PIE CHART: Profit Share
# -------------------------------
plt.figure(figsize=(7, 7))
plt.pie(
    df["Monthly_Profit"],
    labels=df["Model"],
    autopct="%1.1f%%",
    startangle=140
)
plt.title("Share of Monthly Profit by Car Model")
plt.tight_layout()
plt.show()
