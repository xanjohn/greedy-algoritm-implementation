import streamlit as st

def cargo_ship_greedy_by_profit(capacity, items):
    items_sorted = sorted(items, key=lambda x: x[1], reverse=True)  # sort items by profit in descending order
    knapsack = []
    knapsack_capacity = 0
    profit = 0
    for item in items_sorted:
        if knapsack_capacity + item[2] <= capacity:  # check if adding item to knapsack exceeds capacity
            knapsack.append(item[0])
            knapsack_capacity += item[2]
            profit += item[1]

    return knapsack, profit

st.title("APLIKASI KAPAL KARGO")

n = st.number_input("Banyaknya Barang: ", min_value=1, step=1, value=1)

items = []
for i in range(n):
    name = st.text_input(f"Nama Barang {i + 1}: ")
    profit = st.number_input(f"Harga Barang {i + 1}: ", min_value=0, step=1, value=0)
    weight = st.number_input(f"Berat Barang {i + 1}: ", min_value=0, step=1, value=0)
    items.append((name, profit, weight))

capacity = st.number_input("Kapasitas Kapal Kargo: ", min_value=1, step=1, value=1)

if st.button("Hitung"):
    knapsack, profit = cargo_ship_greedy_by_profit(capacity, items)
    st.write(f"Barang Yang Akan Diangkut: {knapsack}")
    st.write(f"Total Harga: {profit}")
