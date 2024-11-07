import tkinter as tk
from tkinter import messagebox
import os
import subprocess

# Function to save the text content to a file
def save_thoughts(event=None):
    thought_text = text_area.get("1.0", tk.END).strip()
    
    if thought_text.lower() == "fetch":
        open_thoughts_file()
    elif thought_text:
        # Create a directory for the thoughts if it doesn't exist
        if not os.path.exists("thoughts"):
            os.makedirs("thoughts")
        
        # Save the thoughts to a file with a timestamp or other unique identifier
        with open(os.path.join("thoughts", "thoughts.txt"), "a") as file:
            file.write(thought_text + "\n\n")
        
        # Clear the text area after saving
        text_area.delete("1.0", tk.END)
        messagebox.showinfo("Saved", "Your thoughts have been saved!")
    else:
        messagebox.showwarning("Empty Input", "Please write something before saving.")

# Function to open the file containing the saved thoughts
def open_thoughts_file():
    file_path = os.path.join("thoughts", "thoughts.txt")
    if os.path.exists(file_path):
        if os.name == 'nt':  # For Windows
            os.startfile(file_path)
        elif os.name == 'posix':  # For macOS and Linux
            subprocess.call(('open', file_path))
    else:
        messagebox.showwarning("File Not Found", "No thoughts have been saved yet.")

# Function to quit the app
def quit_app(event=None):
    root.quit()

# Set up the main window
root = tk.Tk()
root.title("Thoughts Journal")
root.geometry("400x250")
root.configure(bg="#2b2b2b")

# Make the app responsive
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Label for title
title_label = tk.Label(root, text="Write Your Thoughts", font=("Arial", 14, "bold"), fg="white", bg="#2b2b2b")
title_label.pack(pady=(10, 5))

# Text area for writing thoughts
text_area = tk.Text(root, wrap="word", font=("Arial", 12), fg="white", bg="#1e1e1e", insertbackground="white", height=10)
text_area.pack(padx=20, pady=(0, 10), fill="both", expand=True)
text_area.focus_set()  

save_button = tk.Button(root, text="Save Thoughts", command=save_thoughts, font=("Arial", 12), bg="#444444", fg="white", activebackground="#555555", activeforeground="white")
save_button.pack(pady=(5, 15))

root.bind("<Return>", save_thoughts)       # Enter to save or fetch
root.bind("<Control-q>", quit_app)         # Ctrl+Q to quit

root.mainloop()
