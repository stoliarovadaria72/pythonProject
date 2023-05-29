import requests
import tkinter as tk


def get_history(event):
    date = date_entry.get()

   
    response = requests.get(f'http://numbersapi.com/{date}/date')

    if response.status_code == 200:
        fact = response.text
    else:
        fact = "Ошибка: неверный формат даты."

    fact_text.config(state=tk.NORMAL)
    fact_text.delete('1.0', tk.END)
    fact_text.insert(tk.END, fact)
    fact_text.config(state=tk.DISABLED)



window = tk.Tk()
window.title("Этот день в истории")


date_label = tk.Label(window, text="Введите дату (MM/ДД):")
date_label.pack()
date_entry = tk.Entry(window)
date_entry.pack()


fetch_button = tk.Button(window, text="Факт из истории")
fetch_button.pack()
fetch_button.bind('<Button-1>', get_history)


fact_text = tk.Text(window, width=50, height=10)
fact_text.pack()
fact_text.config(state=tk.DISABLED)


window.mainloop()
