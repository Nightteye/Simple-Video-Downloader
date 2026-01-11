# 🚀 Ultimate Universal Video Downloader

A modern, GUI-based video downloader built with Python. It automatically detects links from YouTube, Instagram, and other websites, downloads the highest quality video/audio available, and sorts them into organized folders.

![App Screenshot](https://via.placeholder.com/800x400?text=App+Screenshot+Placeholder) 
*(Add a screenshot of your GUI here by replacing the link above)*

## ✨ Features

* **Modern GUI:** Clean, dark-mode interface built with `CustomTkinter`.
* **Smart Auto-Sorting:** Automatically detects the platform (YouTube, Instagram, TikTok, etc.) and saves videos into dedicated folders.
* **Highest Quality:** Forces 1080p/4K downloads by merging video+audio streams using FFmpeg.
* **Instagram Support:** Downloads Reels and Posts using browser cookies (Bypass login restrictions).
* **Cloudflare Bypass:** Uses `curl_cffi` to impersonate real browsers, allowing downloads from protected sites.
* **Multi-threaded:** Downloads run in the background without freezing the application.

## 🛠️ Prerequisites

Before running the application, ensure you have the following installed:

1.  **Python 3.8+**
2.  **FFmpeg:** Required for merging high-quality audio and video.
    * *Windows:* [Download Here](https://www.gyan.dev/ffmpeg/builds/) (Add to System PATH or place `ffmpeg.exe` in the project folder).
    * *Mac:* `brew install ffmpeg`
    * *Linux:* `sudo apt install ffmpeg`

## 📦 Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/yourusername/universal-downloader.git](https://github.com/yourusername/universal-downloader.git)
    cd universal-downloader
    ```

2.  **Install Python Dependencies**
    ```bash
    pip install yt-dlp customtkinter pillow curl_cffi
    ```

## ⚙️ Configuration

Open `gui_downloader.py` and update the download path to your preferred location:

```python
# Line 8
BASE_FOLDER = r"C:\Users\YourName\Downloads"
