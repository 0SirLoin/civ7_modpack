import json
import os
import requests
import zipfile
import patoolib
import shutil
from urllib.parse import unquote

# Load JSON from links.json
json_file = "links.json"
with open(json_file, "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract CivFanatics Download URLs
civfanatics_download_urls = []
for site in data["sites"]:
    if site["name"] == "CivFanatics":
        civfanatics_download_urls = [link.rstrip("/") + "/download" for link in site["links"]]

# Get the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define extraction folder
mods_folder = os.path.join(script_dir, "mods")

# Ensure extraction folder exists
if os.path.exists(mods_folder):
    shutil.rmtree(mods_folder)
os.makedirs(mods_folder, exist_ok=True)

# Function to extract compressed files
def extract_archive(file_path):
    extract_to = os.path.join(mods_folder, os.path.splitext(os.path.basename(file_path))[0])
    os.makedirs(extract_to, exist_ok=True)

    file_ext = file_path.lower().split(".")[-1]
    if file_ext == "zip":
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(extract_to)
    elif file_ext in ["rar", "7z"]:
        patoolib.extract_archive(file_path, outdir=extract_to)
    else:
        print(f"Unsupported file format: {file_path}")
        return

    print(f"Extracted to: {extract_to}")

# Function to download and process archives
def download_and_extract(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        content_disposition = response.headers.get("Content-Disposition")
        if content_disposition and "filename=" in content_disposition:
            filename = content_disposition.split("filename=")[1].strip('"')
        else:
            filename = "downloaded_file.zip"

        filename = unquote(filename)  # Decode URL-encoded characters
        file_path = os.path.join(mods_folder, filename)

        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Downloaded: {file_path}")
        extract_archive(file_path)
    else:
        print(f"Failed to download {url}. Status Code: {response.status_code}")

# Process each CivFanatics download link
for download_url in civfanatics_download_urls:
    download_and_extract(download_url)
