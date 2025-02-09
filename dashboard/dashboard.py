import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

data_folder = Path("..", "data")

if not data_folder.exists():
    st.error(f"Folder {data_folder} tidak ditemukan. Pastikan folder tersebut ada.")
    st.stop()

try:
    orders = pd.read_csv(data_folder / "orders_dataset.csv")
    order_items = pd.read_csv(data_folder / "order_items_dataset.csv")
    products = pd.read_csv(data_folder / "products_dataset.csv")
    order_reviews = pd.read_csv(data_folder / "order_reviews_dataset.csv")
except FileNotFoundError as e:
    st.error(f"File tidak ditemukan: {e}")
    st.stop()

def clean_products(products):
    products["product_category_name"] = products["product_category_name"].fillna("Unknown")
    return products

def clean_orders(orders):
    orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])
    return orders

products = clean_products(products)
orders = clean_orders(orders)

st.title("📊 E-commerce Data Dashboard")

st.subheader("📅 Filter by Date")
min_date = orders["order_purchase_timestamp"].min().date()
max_date = orders["order_purchase_timestamp"].max().date()

start_date = st.date_input("Start Date", min_date, min_value=min_date, max_value=max_date)
end_date = st.date_input("End Date", max_date, min_value=min_date, max_value=max_date)

filtered_orders = orders[
    (orders["order_purchase_timestamp"].dt.date >= start_date) & 
    (orders["order_purchase_timestamp"].dt.date <= end_date)
].copy() 

st.subheader("🛒 Filter by Category")
all_categories = products["product_category_name"].unique()
selected_categories = st.multiselect("Select Categories", all_categories, default=all_categories)

st.subheader("🏆 Produk Paling Laris")

order_items_products = order_items.merge(products, on="product_id", how="left")

filtered_order_items_products = order_items_products[order_items_products["product_category_name"].isin(selected_categories)]

top_products = filtered_order_items_products["product_category_name"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=top_products.values, y=top_products.index, ax=ax)
plt.xlabel("Jumlah Produk Terjual")
plt.ylabel("Nama Produk")
plt.title("Top 10 Produk Paling Laris")
st.pyplot(fig)

st.subheader("📆 Tren Pesanan per Bulan")

filtered_orders["order_month"] = filtered_orders["order_purchase_timestamp"].dt.to_period("M").astype(str)
monthly_orders = filtered_orders["order_month"].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x=monthly_orders.index, y=monthly_orders.values, marker="o", linestyle="-", color="blue", ax=ax)
plt.xlabel("Bulan")
plt.ylabel("Jumlah Pesanan")
plt.title("Tren Pesanan per Bulan")
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("⭐ Distribusi Skor Review")

fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(order_reviews['review_score'], bins=5, kde=True, color="blue", ax=ax)
plt.title("Distribusi Skor Review")
plt.xlabel("Skor Review")
plt.ylabel("Jumlah Pesanan")
st.pyplot(fig)
