import requests
import tkinter as tk


def get_history(event):
    date = date_entry.get()

    # Make a request to the Numbers API
    response = requests.get(f'http://numbersapi.com/{date}/date')

    if response.status_code == 200:
        fact = response.text
    else:
        fact = "Ошибка: неверный формат даты."

    fact_text.config(state=tk.NORMAL)
    fact_text.delete('1.0', tk.END)
    fact_text.insert(tk.END, fact)
    fact_text.config(state=tk.DISABLED)


# Create the main window
window = tk.Tk()
window.title("Этот день в истории")

# Create a label and entry for the date
date_label = tk.Label(window, text="Введите дату (MM/ДД):")
date_label.pack()
date_entry = tk.Entry(window)
date_entry.pack()

# Create a button to fetch the history fact
fetch_button = tk.Button(window, text="Факт из истории")
fetch_button.pack()
fetch_button.bind('<Button-1>', get_history)

# Create a text widget to display the history fact
fact_text = tk.Text(window, width=50, height=10)
fact_text.pack()
fact_text.config(state=tk.DISABLED)

# Run the main loop
window.mainloop()