import tkinter as tk
import re

def check_strength(password):
    strength_points = 0

    if len(password) >= 8:
        strength_points += 1
    else:
        return "Too short"

    if re.search(r'[A-Z]', password):
        strength_points += 1
    if re.search(r'[a-z]', password):
        strength_points += 1
    if re.search(r'\d', password):
        strength_points += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_points += 1

    if strength_points <= 2:
        return "Weak"
    elif strength_points == 3 or strength_points == 4:
        return "Moderate"
    else:
        return "Strong"

def evaluate_password():
    pwd = password_entry.get()
    strength = check_strength(pwd)
    result_label.config(text=f"Password Strength: {strength}")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")
root.resizable(False, False)

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
password_entry = tk.Entry(root, width=30, show='*', font=("Arial", 12))
password_entry.pack()

tk.Button(root, text="Check Strength", command=evaluate_password, font=("Arial", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
