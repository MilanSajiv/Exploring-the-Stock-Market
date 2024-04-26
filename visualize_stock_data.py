import yfinance as yf
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

def fetch_stock_data(symbol, start_date, end_date):
    try:
        # Fetch historical stock data using the Yahoo Finance API
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        return stock_data
    except Exception as e:
        messagebox.showerror("Error", str(e))

def plot_stock_data(stock_data):
    # Plotting the closing prices
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['Close'])
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock Price History')
    plt.grid(True)
    plt.show()

def show_graph():
    symbol = symbol_entry.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()

    # Fetch stock data
    stock_data = fetch_stock_data(symbol, start_date, end_date)

    # Plot stock data
    plot_stock_data(stock_data)

# Create GUI window
window = tk.Tk()
window.title("Stock Prediction")
window.geometry("400x200")

# Create input fields for symbol, start date, and end date
symbol_label = tk.Label(window, text="Stock Symbol:")
symbol_label.pack()
symbol_entry = tk.Entry(window)
symbol_entry.pack()

start_date_label = tk.Label(window, text="Start Date (YYYY-MM-DD):")
start_date_label.pack()
start_date_entry = tk.Entry(window)
start_date_entry.pack()

end_date_label = tk.Label(window, text="End Date (YYYY-MM-DD):")
end_date_label.pack()
end_date_entry = tk.Entry(window)
end_date_entry.pack()

# Create button to show graph
show_graph_button = tk.Button(window, text="Show Graph", command=show_graph)
show_graph_button.pack()

# Run the GUI
window.mainloop()