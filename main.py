import tkinter as tk
from tkinter import ttk, messagebox
from stock_algorithms import max_profit_divide_and_conquer, top_k_profitable_stocks, dijkstra_shortest_path

stocks = {}  # Store stock_name: price

# ------------------------------
# GUI Functions
# ------------------------------
def add_stock():
    name = name_entry.get().strip()
    try:
        price = float(price_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid price.")
        return
    
    if not name:
        messagebox.showwarning("Missing Name", "Please enter a stock name.")
        return

    stocks[name] = price
    update_stock_list()
    name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

def update_stock_list():
    listbox.delete(0, tk.END)
    for s, p in stocks.items():
        listbox.insert(tk.END, f"{s}: ₹{p}")

def analyze_stocks():
    if not stocks:
        messagebox.showwarning("No Data", "Add some stocks first.")
        return

    # Divide & Conquer - max profit from price list
    prices = list(stocks.values())
    max_profit = max_profit_divide_and_conquer(prices)

    # Heap - Top 3 stocks
    top3 = top_k_profitable_stocks(stocks, 3)

    # Dijkstra - simulate simple graph
    graph = {
        'Day1': {'Day2': 5, 'Day3': 3},
        'Day2': {'Day3': 2, 'Day4': 6},
        'Day3': {'Day4': 7, 'Day5': 4},
        'Day4': {'Day5': 2},
        'Day5': {}
    }
    shortest_path = dijkstra_shortest_path(graph, 'Day1')

    # Show results
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "=== STOCK ANALYSIS RESULTS ===\n\n")
    result_text.insert(tk.END, f"💰 Max Profit (Divide & Conquer): {max_profit}\n\n")

    result_text.insert(tk.END, "🔥 Top 3 Profitable Stocks (Heap):\n")
    for n, v in top3:
        result_text.insert(tk.END, f"   {n}: ₹{v}\n")

    result_text.insert(tk.END, "\n🧭 Shortest Price Path (Dijkstra):\n")
    for node, dist in shortest_path.items():
        result_text.insert(tk.END, f"   {node}: {dist}\n")

# ------------------------------
# Main GUI
# ------------------------------
root = tk.Tk()
root.title("Smart Stock Analyzer (DAA Project)")
root.geometry("700x600")
root.config(bg="#f0f4f7")

title_label = tk.Label(root, text="📊 Smart Stock Analyzer", font=("Arial", 20, "bold"), bg="#f0f4f7")
title_label.pack(pady=10)

# Input Frame
frame = tk.Frame(root, bg="#f0f4f7")
frame.pack(pady=10)

tk.Label(frame, text="Stock Name:", bg="#f0f4f7").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Price (₹):", bg="#f0f4f7").grid(row=0, column=2, padx=5, pady=5)
price_entry = tk.Entry(frame)
price_entry.grid(row=0, column=3, padx=5, pady=5)

add_btn = tk.Button(frame, text="Add Stock", bg="#4CAF50", fg="white", command=add_stock)
add_btn.grid(row=0, column=4, padx=10)

# Stock List
tk.Label(root, text="📦 All Stocks", font=("Arial", 14, "bold"), bg="#f0f4f7").pack()
listbox = tk.Listbox(root, width=60, height=8)
listbox.pack(pady=10)

# Analyze Button
analyze_btn = tk.Button(root, text="Analyze Stocks", font=("Arial", 14, "bold"), bg="#2196F3", fg="white", command=analyze_stocks)
analyze_btn.pack(pady=10)

# Results
tk.Label(root, text="📈 Analysis Result", font=("Arial", 14, "bold"), bg="#f0f4f7").pack()
result_text = tk.Text(root, width=80, height=15, wrap=tk.WORD)
result_text.pack(padx=10, pady=10)

root.mainloop()
