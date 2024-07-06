import pandas as pd
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv(r"C:\Users\HP\Desktop\kartik\Dataset .csv")

# Analyze the relationship between price range and online delivery
price_range_online_delivery = data.groupby('Price range')['Has Online delivery'].value_counts(normalize=True).unstack() * 100

# Analyze the relationship between price range and table booking
price_range_table_booking = data.groupby('Price range')['Has Table booking'].value_counts(normalize=True).unstack() * 100

# Function to create a window for price range vs. online delivery
def price_range_online_delivery_window():
    window = tk.Toplevel(root)
    window.title("Price Range vs. Online Delivery")
    window.geometry("800x600")

    fig, ax = plt.subplots(figsize=(8, 6))
    price_range_online_delivery.plot(kind='bar', stacked=True, color=sns.color_palette("husl", 2), ax=ax)
    ax.set_xlabel('Price Range')
    ax.set_ylabel('Percentage of Restaurants')
    ax.set_title('Price Range vs. Online Delivery')
    ax.legend(title='Has Online Delivery')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Function to create a window for price range vs. table booking
def price_range_table_booking_window():
    window = tk.Toplevel(root)
    window.title("Price Range vs. Table Booking")
    window.geometry("800x600")

    fig, ax = plt.subplots(figsize=(8, 6))
    price_range_table_booking.plot(kind='bar', stacked=True, color=sns.color_palette("husl", 2), ax=ax)
    ax.set_xlabel('Price Range')
    ax.set_ylabel('Percentage of Restaurants')
    ax.set_title('Price Range vs. Table Booking')
    ax.legend(title='Has Table Booking')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Create the main window
root = tk.Tk()
root.title("Restaurant Data Analysis")
root.geometry("400x300")

# Apply a theme
style = ttk.Style(root)
style.theme_use('clam')

# Set up font and colors
root.option_add("*Font", "Helvetica 12")
style.configure("TButton", padding=6, relief="flat", background="#ccc")
style.map("TButton", background=[('active', '#0052cc')], foreground=[('active', 'white')])

# Create a frame
frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

# Title label
title_label = ttk.Label(frame, text="Restaurant Data Analysis", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Create buttons to open each graph window
ttk.Button(frame, text="Price Range vs. Online Delivery", command=price_range_online_delivery_window).pack(padx=10, pady=10)
ttk.Button(frame, text="Price Range vs. Table Booking", command=price_range_table_booking_window).pack(padx=10, pady=10)

# Start the main event loop
root.mainloop()
