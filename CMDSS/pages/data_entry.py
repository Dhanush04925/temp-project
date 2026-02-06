import streamlit as st
from pymongo import MongoClient

st.title("📥 Automated Data Entry")
st.write("Add new menu items or inventory records to MongoDB Cloud.")

with st.form("inventory_update"):
    item_name = st.text_input("Item Name (e.g., Samosa)")
    stock_qty = st.number_input("Stock Quantity", min_value=0)
    price = st.number_input("Unit Price", min_value=0.0)
    
    if st.form_submit_button("Sync to Cloud"):
        client = MongoClient(st.secrets["mongo"]["uri"])
        client.CanteenDB.inventory.insert_one({
            "item": item_name,
            "quantity": stock_qty,
            "price": price
        })
        st.success(f"Successfully pushed {item_name} to MongoDB!")