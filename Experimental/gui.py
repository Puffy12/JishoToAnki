

import customtkinter as ctk
from tkinter import ttk
import download_manager as dm

root = ctk.CTk()

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

root.title("Youtuber Downloader")
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

url_label = ctk.CTkLabel(content_frame, text="Enter the Youtube URL : ")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady="10p 5p")
entry_url.pack(pady="10p 5p")

download_button = ctk.CTkButton(content_frame, text="Download", command=dm.DownloadManager().download_video)
download_button.pack(pady="10p 5p")

Resolutions = ["1080p", "720p", "360p", "240p"]
Resolution_var = ctk.StringVar()
Resolution_Combobox = ttk.Combobox(content_frame, values=Resolutions, textvariable=Resolution_var)
Resolution_Combobox.pack(pady="10p 5p")
Resolution_Combobox.set("720p")

progress_label = ctk.CTkLabel(content_frame, text="0%")
progress_label.pack(pady="10p 5p")

progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0)

status_label = ctk.CTkLabel(content_frame, text="")

format_label = ctk.CTkLabel(content_frame, text="Choose Download Format:")
format_label.pack(pady="10p 5p")

format_var = ctk.StringVar()
format_radio_mp3 = ctk.CTkRadioButton(content_frame, text="MP3", variable=format_var, value="MP3")
format_radio_mp3.pack(pady="5p")
format_radio_mp4 = ctk.CTkRadioButton(content_frame, text="MP4", variable=format_var, value="MP4")
format_radio_mp4.pack(pady="5p")

format_var.set("MP4")

delete_button = ctk.CTkButton(content_frame, text="Delete All Files", bg_color="red", command=dm.DownloadManager().delete_downloads)
delete_button.pack(side="bottom", anchor="se", pady=5, padx=5)

root.mainloop()
