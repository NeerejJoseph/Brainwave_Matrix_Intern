import re
import urllib.parse
import tkinter as tk
from tkinter import messagebox

suspicious_keywords = [
    "login", "verify", "update", "secure", "account", "banking",
    "signin", "ebay", "paypal", "security", "webscr"
]

def is_suspicious(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc.lower()
    path = parsed_url.path.lower()

    if re.match(r'\d+\.\d+\.\d+\.\d+', domain):
        return True, "URL uses an IP address instead of a domain name."

    for keyword in suspicious_keywords:
        if keyword in domain or keyword in path:
            return True, f"Contains suspicious keyword: '{keyword}'"

    if '@' in url:
        return True, "URL contains '@' symbol, which may be used for redirection."

    if domain.count('-') > 3 or domain.count('.') > 4:
        return True, "URL structure looks suspicious (too many dots or hyphens)."

    return False, "URL appears safe."

def scan_url():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return

    suspicious, reason = is_suspicious(url)
    if suspicious:
        result_label.config(text=f"[ALERT] Suspicious URL:\n{reason}", fg="red")
    else:
        result_label.config(text=f"[OK] Safe URL:\n{reason}", fg="green")

root = tk.Tk()
root.title("Phishing Link Scanner")
root.geometry("450x250")
root.config(bg="#f7f7f7")

tk.Label(root, text="Enter URL to Scan", font=("Arial", 14), bg="#f7f7f7").pack(pady=10)

url_entry = tk.Entry(root, font=("Arial", 12), width=40)
url_entry.pack(pady=5)

tk.Button(root, text="Scan URL", command=scan_url, font=("Arial", 12), bg="#007acc", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=400, bg="#f7f7f7")
result_label.pack(pady=10)

root.mainloop()
