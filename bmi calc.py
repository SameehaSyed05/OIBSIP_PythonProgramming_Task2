import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt

bmi_history = []

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            raise ValueError("Values must be positive")
        bmi = round(weight / (height ** 2), 2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
        result_label.config(text=f"BMI: {bmi} ({category})")
        bmi_history.append((weight, height, bmi, category))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height.")

def show_history():
    if not bmi_history:
        messagebox.showinfo("No Data", "No BMI history available yet.")
        return
    history_window = tk.Toplevel(root)
    history_window.title("BMI History")
    tree = ttk.Treeview(history_window, columns=("Weight", "Height", "BMI", "Category"), show="headings")
    tree.heading("Weight", text="Weight (kg)")
    tree.heading("Height", text="Height (m)")
    tree.heading("BMI", text="BMI")
    tree.heading("Category", text="Category")
    tree.pack(fill=tk.BOTH, expand=True)
    for entry in bmi_history:
        tree.insert("", tk.END, values=entry)

def plot_history():
    if not bmi_history:
        messagebox.showinfo("No Data", "No BMI history available yet.")
        return
    bmis = [entry[2] for entry in bmi_history]
    plt.figure(figsize=(7, 4))
    plt.plot(range(1, len(bmis) + 1), bmis, marker="o", color="blue", label="BMI Progress")
    plt.axhline(18.5, color="green", linestyle="--", label="Lower Normal")
    plt.axhline(24.9, color="green", linestyle="--", label="Upper Normal")
    plt.title("BMI History Trend")
    plt.xlabel("Entry Number")
    plt.ylabel("BMI")
    plt.legend()
    plt.grid(True)
    plt.show()

root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("400x300")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

title_label = tk.Label(frame, text="BMI Calculator", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(frame, text="Weight (kg):", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
weight_entry = tk.Entry(frame, width=10, font=("Arial", 12))
weight_entry.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Height (m):", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
height_entry = tk.Entry(frame, width=10, font=("Arial", 12))
height_entry.grid(row=2, column=1, pady=5)

calc_button = tk.Button(frame, text="Calculate BMI", command=calculate_bmi, font=("Arial", 12), bg="lightblue")
calc_button.grid(row=3, column=0, columnspan=2, pady=10)

history_button = tk.Button(frame, text="View History", command=show_history, font=("Arial", 12), bg="lightgreen")
history_button.grid(row=4, column=0, pady=5)

plot_button = tk.Button(frame, text="Show Graph", command=plot_history, font=("Arial", 12), bg="orange")
plot_button.grid(row=4, column=1, pady=5)

result_label = tk.Label(frame, text="Enter values and click Calculate", font=("Arial", 12), fg="blue")
result_label.grid(row=5, column=0, columnspan=2, pady=15)

root.mainloop()
