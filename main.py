import sqlite3
import tkinter as tk
import os

connection = sqlite3.connect("wiki_DB_sl3")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS links (word TEXT, url TEXT)")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def search(event):
    val = entry.get()

    word = val.strip().replace(" ", "_")
    link = "https://uk.wikipedia.org/wiki/" + word

    cursor.execute("INSERT INTO links (word, url) VALUES (?, ?);", (word, link))
    connection.commit()

    cursor.execute("SELECT word FROM links")
    rows = cursor.fetchall()

    clear_console()

    history = ""
    for i, row in enumerate(rows, start=1):
        history += f"{i}({row[0]}); "

    print(history.strip())
    print(link)

    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Wiki")
root.geometry("400x400")

entry = tk.Entry(root, font=("Arial", 18))
entry.pack(expand=True)

entry.bind("<Return>", search)

root.mainloop()
connection.close()