import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# File save mode
def save_to_file(bmi, status, calc_type, gender):
    with open("bmi_records.txt", "a") as file:
        file.write(f"Gender: {gender}, Type: {calc_type}, BMI: {bmi:.2f}, Status: {status}\n")

# BMI status
def get_bmi_status(bmi):
    if bmi <= 18.5: return "Underweight"
    elif bmi <= 25: return "Normal"
    elif bmi <= 30: return "Overweight"
    else: return "Obese"

# Graph display
def show_graph():
    try:
        with open("bmi_records.txt", "r") as file:
            lines = file.readlines()
            bmis = [float(line.split("BMI: ")[1].split(",")[0]) for line in lines]
            plt.plot(bmis, marker='o', color='green')
            plt.title("BMI History")
            plt.ylabel("BMI Value")
            plt.show()
    except:
        messagebox.showwarning("Warning", "No records found to plot!")

# --- Metric Calculator ---
def open_metric_calc():
    win = tk.Toplevel(root)
    win.title("Metric BMI")
    win.geometry("300x400")
    win.configure(bg="#f8f9fa")

    tk.Label(win, text="Gender (Male/Female):", bg="#f8f9fa").pack(pady=5)
    e_g = tk.Entry(win)
    e_g.pack()
    tk.Label(win, text="Weight (kg):", bg="#f8f9fa").pack(pady=5)
    e_w = tk.Entry(win)
    e_w.pack()
    tk.Label(win, text="Height (m):", bg="#f8f9fa").pack(pady=5)
    e_h = tk.Entry(win)
    e_h.pack()

    def calc():
        try:
            bmi = float(e_w.get()) / (float(e_h.get()) ** 2)
            status = get_bmi_status(bmi)
            save_to_file(bmi, status, "Metric", e_g.get())
            messagebox.showinfo("Result", f"BMI: {bmi:.2f}\nStatus: {status}")
        except:
            messagebox.showerror("Error", "Invalid Input")

    tk.Button(win, text="Calculate", command=calc, bg="#4CAF50", fg="white", width=15).pack(pady=5)
    tk.Button(win, text="Close", command=win.destroy, bg="#555555", fg="white", width=15).pack(pady=5)

# --- Imperial Calculator ---
def open_imperial_calc():
    win = tk.Toplevel(root)
    win.title("Imperial BMI")
    win.geometry("300x450")
    win.configure(bg="#f8f9fa")

    tk.Label(win, text="Gender (Male/Female):", bg="#f8f9fa").pack(pady=5)
    e_g = tk.Entry(win)
    e_g.pack()
    tk.Label(win, text="Weight (kg):", bg="#f8f9fa").pack(pady=5)
    e_w = tk.Entry(win)
    e_w.pack()
    tk.Label(win, text="Feet:", bg="#f8f9fa").pack(pady=5)
    e_f = tk.Entry(win)
    e_f.pack()
    tk.Label(win, text="Inches:", bg="#f8f9fa").pack(pady=5)
    e_i = tk.Entry(win)
    e_i.pack()

    def calc():
        try:
            meters = ((float(e_f.get()) * 12) + float(e_i.get())) * 0.0254
            bmi = float(e_w.get()) / (meters ** 2)
            status = get_bmi_status(bmi)
            save_to_file(bmi, status, "Imperial", e_g.get())
            messagebox.showinfo("Result", f"BMI: {bmi:.2f}\nStatus: {status}")
        except:
            messagebox.showerror("Error", "Invalid Input")

    tk.Button(win, text="Calculate", command=calc, bg="#4CAF50", fg="white", width=15).pack(pady=5)
    tk.Button(win, text="Close", command=win.destroy, bg="#555555", fg="white", width=15).pack(pady=5)

# --- Main Menu ---
root = tk.Tk()
root.title("BMI Hub")
root.geometry("300x350")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Select Option", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=20)
tk.Button(root, text="Metric (kg/m)", command=open_metric_calc, width=20, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(root, text="Imperial (ft/in)", command=open_imperial_calc, width=20, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(root, text="View Graph", command=show_graph, width=20, bg="#FF9800", fg="white").pack(pady=5)
tk.Button(root, text="Exit", command=root.destroy, width=20, bg="black", fg="white").pack(pady=20)

root.mainloop()