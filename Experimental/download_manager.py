import os
from pytube import YouTube as YouTube_PyTube

class DownloadManager:
    def download_video(self):
        url = self.entry_url.get()
        download_format = self.format_var.get()
        resolution = self.Resolution_var.get()

        self.progress_label.pack(pady="10p 5p")
        self.progress_bar.pack(pady="10p 5p")
        self.status_label.pack(pady="10p 5p")

        try:
            if download_format == "MP3":
                video = YouTube_PyTube(url, on_progress_callback=self.on_progress)
                title = video.title

                os.path.join("downloads", f"{title}.mp3")
                stream = video.streams.filter(only_audio=True).first()
                out_file = stream.download(output_path="downloads")

                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)

                self.status_label.configure(text="Mp3 Download Successful", text_color="white", fg_color="green")

            else:
                video = YouTube_PyTube(url, on_progress_callback=self.on_progress)
                title = video.title

                stream = video.streams.filter(res=resolution).first()
                os.path.join("downloads", f"{title}.mp4")
                stream.download(output_path="downloads")

                self.status_label.configure(text="Mp4 Download Successful", text_color="white", fg_color="green")

            self.root.after(self.MillSecond_clear_Delay, self.clear_status_label)

        except Exception as e:
            self.status_label.configure(text=f"Error: {str(e)}", text_color="white", fg_color="red")
            self.root.after(self.MillSecond_clear_Delay, self.clear_status_label)

    def clear_status_label(self):
        self.status_label.configure(text="")
        self.progress_bar.set(0)
        self.progress_label.configure(text="0%")

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = bytes_downloaded / total_size * 100

        self.progress_label.configure(text=str(round(percentage, 2)) + "%")
        self.progress_label.update()

        self.progress_bar.set(float(percentage / 100))

    def delete_downloads(self):
        download_folder = "downloads"
        for file_name in os.listdir(download_folder):
            file_path = os.path.join(download_folder, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")

        self.status_label.configure(text="All Downloadeds Deleted Successfully", text_color="white", fg_color="red")
        self.root.after(self.MillSecond_clear_Delay, self.clear_status_label)
