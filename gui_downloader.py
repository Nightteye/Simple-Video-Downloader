import customtkinter as ctk
import yt_dlp
import os
import threading
from urllib.parse import urlparse

# --- CONFIGURATION ---
BASE_FOLDER = r"Your\Desired\Path\Here" 
# ---------------------

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class VideoDownloaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("🚀 Ultimate Downloader")
        self.geometry("600x450")
        self.resizable(False, False)

        # Title Label
        self.label_title = ctk.CTkLabel(self, text="Universal Video Downloader", font=("Roboto Medium", 24))
        self.label_title.pack(pady=20)

        # URL Entry Field
        self.entry_url = ctk.CTkEntry(self, placeholder_text="Paste your link here...", width=450, height=40)
        self.entry_url.pack(pady=10)

        # Download Button
        self.btn_download = ctk.CTkButton(self, text="Download Video", command=self.start_download_thread, width=200, height=40, font=("Roboto Medium", 14))
        self.btn_download.pack(pady=20)

        # Progress Bar (Indeterminate mostly, as yt-dlp progress is hard to sync perfectly in simple GUIs)
        self.progress_bar = ctk.CTkProgressBar(self, width=450)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=10)

        # Status Label
        self.label_status = ctk.CTkLabel(self, text="Ready", text_color="gray", font=("Roboto", 12))
        self.label_status.pack(pady=10)

        # Info Box (Console Output area)
        self.textbox_log = ctk.CTkTextbox(self, width=500, height=120)
        self.textbox_log.pack(pady=10)
        self.textbox_log.insert("0.0", "--- Log initialized ---\n")
        self.textbox_log.configure(state="disabled") # Make read-only

    def log(self, message):
        """Adds message to the text box"""
        self.textbox_log.configure(state="normal")
        self.textbox_log.insert("end", message + "\n")
        self.textbox_log.see("end")
        self.textbox_log.configure(state="disabled")

    def get_domain_name(self, url):
        try:
            parsed = urlparse(url)
            domain = parsed.netloc
            if domain.startswith("www."): domain = domain[4:]
            name = domain.split('.')[0]
            return name.capitalize()
        except:
            return "Misc"

    def start_download_thread(self):
        """Starts download in a separate thread to keep GUI responsive"""
        url = self.entry_url.get().strip()
        if not url:
            self.label_status.configure(text="❌ Please enter a URL!", text_color="red")
            return

        self.btn_download.configure(state="disabled")
        self.progress_bar.start() # Starts animation
        self.label_status.configure(text="⏳ Initialization...", text_color="orange")
        
        # Run download in background thread
        threading.Thread(target=self.download_video, args=(url,), daemon=True).start()

    def download_video(self, url):
        site_name = self.get_domain_name(url)
        
        if site_name.lower() in ['youtu', 'youtube']:
            site_name = "YouTube"
            use_cookies = False
        else:
            use_cookies = True

        target_path = os.path.join(BASE_FOLDER, site_name)
        
        self.log(f"Detected: {site_name}")
        self.log(f"Saving to: {target_path}")

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'paths': {'home': target_path},
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': True,
            'no_warnings': True,
            'concurrent_fragment_downloads': 8,
        }

        if site_name == "Instagram":
            ydl_opts['outtmpl'] = '%(uploader)s - %(id)s.%(ext)s'
        
        if use_cookies:
            ydl_opts['cookies_from_browser'] = 'brave'

        try:
            self.label_status.configure(text=f"⬇️ Downloading from {site_name}...", text_color="#3B8ED0") # Blue
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            self.log(f"SUCCESS: Saved to {site_name} folder.")
            self.label_status.configure(text="✅ Download Complete!", text_color="green")
            
        except Exception as e:
            self.log(f"ERROR: {e}")
            self.label_status.configure(text="❌ Error occurred", text_color="red")
        
        finally:
            self.progress_bar.stop()
            self.progress_bar.set(1) # Fill bar
            self.btn_download.configure(state="normal")

if __name__ == "__main__":
    app = VideoDownloaderApp()
    app.mainloop()