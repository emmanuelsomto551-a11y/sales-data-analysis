import pandas as pd
df = pd.read_csv("sales_5000.csv")
#phase 2

clean_df = df.copy()
clean_df.columns = clean_df.columns.str.strip().str.lower()
text_columns = [
    "product",
    "region",
    "customer_id",
    "payment_method",
    "status"
]

for col in text_columns:
    clean_df[col] = clean_df[col].astype("string").str.strip().str.title()
clean_df["region"] = clean_df["region"].replace({
    "Noth": "North",
    "Northh": "North",
    "Sout": "South",
    "Eastern": "East"
})
clean_df["payment_method"] = clean_df["payment_method"].replace({
    "Pos": "POS"
})
clean_df["status"] = clean_df["status"].replace({
    "Complete": "Completed",
    "Return": "Returned"
})
clean_df["order_date"] = pd.to_datetime(
    clean_df["order_date"],
    errors="coerce"
)
clean_df["qty"] = clean_df["qty"].replace({
    "two": "2",
    "five": "5"
})

clean_df["qty"] = (
    clean_df["qty"]
    .astype("string")
    .str.extract(r"(\d+)", expand=False)
)

clean_df["qty"] = pd.to_numeric(
    clean_df["qty"],
    errors="coerce"
)
clean_df.loc[clean_df["qty"] <= 0, "qty"] = pd.NA
clean_df["price"] = pd.to_numeric(
    clean_df["price"],
    errors="coerce"
)
clean_df.loc[clean_df["price"] <= 0, "price"] = pd.NA
categorical_columns = [
    "product",
    "region",
    "customer_id",
    "payment_method",
    "status"
]

for col in categorical_columns:
    clean_df[col] = clean_df[col].fillna("Unknown")
clean_df = clean_df.drop_duplicates()

# Create total sales
clean_df["total_sales"] = clean_df["qty"] * clean_df["price"]
clean_df["year"] = clean_df["order_date"].dt.year
clean_df["month"] = clean_df["order_date"].dt.month
clean_df["month_name"] = clean_df["order_date"].dt.month_name()

# PHASE 3

total_sales = clean_df["total_sales"].sum()
total_sales

average_sales = clean_df["total_sales"].mean()
average_sales

total_quantity = clean_df["qty"].sum()
total_quantity

product_sales = (
    clean_df.groupby("product")["total_sales"]
    .sum()
    .sort_values(ascending=False)
)
product_sales

clean_df["total_sales"].sum()

regional_sales = (
    clean_df.groupby("region")["total_sales"]
    .sum()
    .sort_values(ascending=False)
)
regional_sales

product_quantity = (
    clean_df.groupby("product")["qty"]
    .sum()
    .sort_values(ascending=False)
)
product_quantity

regional_percentage = (
    regional_sales / regional_sales.sum() * 100
).round(2)
regional_percentage

monthly_sales = (
    clean_df.groupby("month_name")["total_sales"]
    .sum()
)
monthly_sales

payment_counts = clean_df["payment_method"].value_counts()
payment_counts

payment_percentage = (
    clean_df["payment_method"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)
payment_percentage

status_counts = clean_df["status"].value_counts()
status_counts

status_percentage = (
    clean_df["status"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)
status_percentage

regional_quantity = (
    clean_df.groupby("region")["qty"]
    .sum()
    .sort_values(ascending=False)
)
regional_quantity

customer_sales = (
    clean_df.groupby("customer_id")["total_sales"]
    .sum()
    .sort_values(ascending=False)
)


customer_orders = (
    clean_df.groupby("customer_id")["order_id"]
    .count()
    .sort_values(ascending=False)
)
customer_orders.head(10)

average_product_price = (
    clean_df.groupby("product")["price"]
    .mean()
    .sort_values(ascending=False)
)
average_product_price

region_product_sales = pd.pivot_table(
    clean_df,
    values="total_sales",
    index="region",
    columns="product",
    aggfunc="sum",
    fill_value=0
)
region_product_sales

status_sales = (
    clean_df.groupby("status")["total_sales"]
    .sum()
    .sort_values(ascending=False)
)
status_sales





































































