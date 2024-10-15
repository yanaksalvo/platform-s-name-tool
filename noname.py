import tkinter as tk
import requests

def check_username():
    username = entry.get()
    results = {}
    platforms = {
        "Instagram": f"https://www.instagram.com/{username}/",
        "Facebook": f"https://www.facebook.com/{username}/",
        "Twitter": f"https://twitter.com/{username}",
        "YouTube": f"https://www.youtube.com/user/{username}",
        "Alan Adı (.com)": f"http://{username}.com"
    }

    for platform, url in platforms.items():
        try:
            response = requests.get(url)
            results[platform] = 'Kullanımda' if response.status_code == 200 else 'Kullanımda değil'
        except requests.exceptions.RequestException:
            results[platform] = 'Kullanımda değil'
    
    display_results(results)

def display_results(results):
    result_text.delete(1.0, tk.END)  
    for platform, status in results.items():
        result_text.insert(tk.END, f"{platform}: {status}\n")

root = tk.Tk()
root.title("Kullanıcı Adı Sorgulama")

label = tk.Label(root, text="Kullanıcı adını girin:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

check_button = tk.Button(root, text="Kontrol Et", command=check_username)
check_button.pack(pady=10)

result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=10)

root.mainloop()
