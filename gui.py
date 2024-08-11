import customtkinter as ctk
from tkinter import filedialog, messagebox
from api_functions import process_file
import threading

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

def update_checking_label(word):
    checking_label.configure(text=f"Checking: {word}")
    checking_label.update()

def clear_checking_label():
    checking_label.configure(text="")
    checking_label.update()

def translate():
    input_filename = input_entry.get()
    output_filename = output_entry.get()
    
    if not input_filename or not output_filename:
        messagebox.showwarning("Warning", "Please select both input and output files.")
        return

    def run_translation():
        process_file(input_filename, output_filename, update_progress_bar, update_checking_label, clear_checking_label)
        messagebox.showinfo("Success", f"Translation completed and saved to {output_filename}")
        progress_bar.set(0)
        progress_label.configure(text=f"Progress: 0%")
    
    threading.Thread(target=run_translation).start()

def cancel():
    root.destroy()

# Create root window
root = ctk.CTk()

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")
root.title("Mass Japanese Translator")  # 大量日本語翻訳
root.geometry("800x600")  # Adjust size as needed
root.iconbitmap("icon.ico")  # Set the icon for the window

# Create a frame that holds content
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

# Usage Instructions Label
usage_text = ("This app translates lists of Japanese words from text files using the Jisho API. To use it, "
              "ensure that the words in your file are separated by commas, as demonstrated in the `Example_Words.txt` file.")
usage_label = ctk.CTkLabel(content_frame, text=usage_text, wraplength=750)
usage_label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

# Input file selection
input_label = ctk.CTkLabel(content_frame, text="Input File:")
input_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
input_entry = ctk.CTkEntry(content_frame, width=400)
input_entry.grid(row=1, column=1, padx=10, pady=10)
input_button = ctk.CTkButton(content_frame, text="Browse Words File...", command=select_input_file)
input_button.grid(row=1, column=2, padx=10, pady=10)

# Output file selection
output_label = ctk.CTkLabel(content_frame, text="Output File:")
output_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
output_entry = ctk.CTkEntry(content_frame, width=400)
output_entry.grid(row=2, column=1, padx=10, pady=10)
output_button = ctk.CTkButton(content_frame, text="Browse Output File...", command=select_output_file)
output_button.grid(row=2, column=2, padx=10, pady=10)

# Translate and Cancel buttons
translate_button = ctk.CTkButton(content_frame, text="Translate", command=translate)
translate_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")
cancel_button = ctk.CTkButton(content_frame, text="Close", command=cancel, fg_color="red", text_color="white")
cancel_button.grid(row=3, column=2, padx=10, pady=10, sticky="w")

# Configure the grid to center elements in the content frame
content_frame.grid_columnconfigure(0, weight=1)
content_frame.grid_columnconfigure(1, weight=1)
content_frame.grid_columnconfigure(2, weight=1)

# Checking Label
checking_label = ctk.CTkLabel(content_frame, text="")
checking_label.grid(row=4, column=0, padx=10, pady=5, columnspan=3, sticky="nsew")

# Create progress bar with reduced width
progress_bar = ctk.CTkProgressBar(content_frame, width=200)  # Reduced width to half
progress_bar.grid(row=5, column=0, padx=10, pady=20, columnspan=3, sticky="nsew")
progress_bar.set(0)  # Initialize progress bar to 0

# Progress Label
progress_label = ctk.CTkLabel(content_frame, text="Progress: 0%")
progress_label.grid(row=6, column=0, padx=10, pady=5, columnspan=3, sticky="nsew")


# Description Label with Text Wrapping
description_text = ("The app formats the translations with definitions and readings, creating a file that is ready for quick "
                    "import into Anki. This process streamlines studying and memorizing Japanese vocabulary, making your "
                    "language learning more efficient and organized.")
description_label = ctk.CTkLabel(content_frame, text=description_text, wraplength=750)
description_label.grid(row=7, column=0, padx=10, pady=10, columnspan=3)

# Start the app
root.mainloop()
