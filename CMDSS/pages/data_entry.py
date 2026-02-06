import streamlit as st
from pymongo import MongoClient
from datetime import datetime

st.title("📥 Automated Data Entry")
st.write("Add new inventory records to MongoDB Cloud.")

# Protect page
if "owner_id" not in st.session_state:
    st.error("Please login first")
    st.stop()

with st.form("inventory_update"):
    item_name = st.text_input("Item Name (e.g., Samosa)")
    stock_qty = st.number_input("Stock Quantity", min_value=0)
    price = st.number_input("Unit Price", min_value=0.0)

    if st.form_submit_button("Sync to Cloud"):

        client = MongoClient(st.secrets["MONGO_URI"])
        db = client[st.secrets["DB_NAME"]]

        db.inventory.insert_one({
            "owner_id": st.session_state["owner_id"],
            "item": item_name,
            "quantity": int(stock_qty),
            "price": float(price),
            "date": datetime.now()
        })

        st.success(f"Successfully pushed {item_name} to MongoDB!")
