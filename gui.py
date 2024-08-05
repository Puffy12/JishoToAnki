import customtkinter as ctk
from tkinter import filedialog, messagebox
from api_functions import process_file
import threading

MillSecond_clear_Delay = 7000

def select_input_file():
    filename = filedialog.askopenfilename(title="Select input file", filetypes=[("Text files", "*.txt")])
    input_entry.delete(0, ctk.END)
    input_entry.insert(0, filename)

def select_output_file():
    filename = filedialog.asksaveasfilename(title="Select output file", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    output_entry.delete(0, ctk.END)
    output_entry.insert(0, filename)

def update_progress_bar(progress):
    progress_bar.set(progress)
    progress_label.configure(text=f"Progress: {int(progress * 100)}%")

def translate():
    input_filename = input_entry.get()
    output_filename = output_entry.get()
    
    if not input_filename or not output_filename:
        messagebox.showwarning("Warning", "Please select both input and output files.")
        return

    def run_translation():
        process_file(input_filename, output_filename, update_progress_bar)
        messagebox.showinfo("Success", f"Translation completed and saved to {output_filename}")
        progress_bar.set(0)
        progress_label.configure(text=f"Progress: 0%")


    threading.Thread(target=run_translation).start()

def cancel():
    root.destroy()

# Create the main window
root = ctk.CTk()
root.title("Japanese Word Translator")
root.geometry("800x400")  #window size

# Create a frame that holds content
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)

# Input file selection
input_label = ctk.CTkLabel(content_frame, text="Input File:")
input_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
input_entry = ctk.CTkEntry(content_frame, width=400)
input_entry.grid(row=0, column=1, padx=10, pady=10)
input_button = ctk.CTkButton(content_frame, text="Browse Words File...", command=select_input_file)
input_button.grid(row=0, column=2, padx=10, pady=10)

# Output file selection
output_label = ctk.CTkLabel(content_frame, text="Output File:")
output_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
output_entry = ctk.CTkEntry(content_frame, width=400)
output_entry.grid(row=1, column=1, padx=10, pady=10)
output_button = ctk.CTkButton(content_frame, text="Browse Output File...", command=select_output_file)
output_button.grid(row=1, column=2, padx=10, pady=10)

# Translate and Cancel buttons
translate_button = ctk.CTkButton(content_frame, text="Translate", command=translate)
translate_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")
cancel_button = ctk.CTkButton(content_frame, text="Close", command=cancel, fg_color="red", text_color="white")
cancel_button.grid(row=2, column=2, padx=10, pady=10, sticky="w")

# Create progress bar
progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.grid(row=3, column=1, padx=10, pady=20, columnspan=2)
progress_bar.set(0)  # Initialize progress bar to 0

progress_label = ctk.CTkLabel(content_frame, text="Progress: 0%")
progress_label.grid(row=4, column=1, padx=10, pady=5, columnspan=2)

# Description label
description_label = ctk.CTkLabel(content_frame, text="The progress bar shows the completion status of the translation process.")
description_label.grid(row=5, column=1, padx=10, pady=10, columnspan=2)

root.mainloop()
