import os
import zipfile
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from scipy.io import loadmat
import pandas as pd

def get_files(files, base_url, download_path, extract_base_path):
    """
    Download and unzip files from a website.

    :param files: List of file identifiers to be processed.
    :param base_url: The base URL to form the download links.
    :param download_path: Path to download the zipped files.
    :param extract_base_path: Path to extract the unzipped files.
    """
    # Ensure the download directory exists
    os.makedirs(download_path, exist_ok=True)

    for file in files:
        response = requests.get(f'{base_url}{file}.html')
        if response.status_code != 200:
            print(f"Failed to retrieve {file}.html")
            continue

        webpage = response.text
        soup = BeautifulSoup(webpage, 'html.parser')

        urls = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.endswith('.zip'):
                full_url = urljoin(base_url, href)
                urls.append(full_url)

        for url in urls[:1]:  # Downloading the first file for demonstration
            try:
                print(f'Downloading from: {url}')
                r = requests.get(url)
                r.raise_for_status()

                filename = os.path.basename(url)
                fnout = os.path.join(download_path, filename)
                extract_path = os.path.join(extract_base_path, file)

                # Ensure the extract directory exists
                os.makedirs(extract_path, exist_ok=True)

                with open(fnout, 'wb') as f:
                    f.write(r.content)
                unzip(fnout, extract_path)

            except requests.exceptions.RequestException as e:
                print(f"Error downloading {url}: {e}")

def unzip(fnout, extract_path):
    """
    Unzip a file to a specified directory.

    :param fnout: Path to the zipped file.
    :param extract_path: Path to extract the unzipped files.
    """
    try:
        with zipfile.ZipFile(fnout, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
            print(f'Extracted to {extract_path}')
    except zipfile.BadZipFile:
        print(f"Failed to unzip {fnout}. It may be corrupted.")

def translate(mat_file, output_csv):
    """
    Translate a .mat file to a .csv file.

    :param mat_file: Path to the .mat file.
    :param output_csv: Path to the output .csv file.
    """
    mat = loadmat(mat_file)
    mat = {k: v for k, v in mat.items() if k[0] != '_'}
    data = pd.DataFrame({k: pd.Series(v[0]) for k, v in mat.items()})
    data.to_csv(output_csv, index=False)
    print(f'Translated {mat_file} to {output_csv}')

def process_mat_files(extract_base_path, output_csv_dir):
    """
    Process all .mat files in the extracted directories and translate them to CSV.

    :param extract_base_path: Base path where the files were extracted.
    :param output_csv_dir: Directory to save the translated CSV files.
    """
    # Ensure the output directory exists
    os.makedirs(output_csv_dir, exist_ok=True)

    for root, _, files in os.walk(extract_base_path):
        for file in files:
            if file.endswith('.mat'):
                mat_file_path = os.path.join(root, file)
                csv_file_path = os.path.join(output_csv_dir, f"{os.path.splitext(file)[0]}.csv")
                translate(mat_file_path, csv_file_path)

def main():
    files = ['DB1']  # List of files to be processed
    base_url = 'https://ninapro.hevs.ch/instructions/'
    download_path = 'C:\\Users\\Aweso\\Downloads\\The folder\\Data\\zipped'
    extract_base_path = 'C:\\Users\\Aweso\\Downloads\\The folder\\Data\\Open'
    output_csv_dir = 'C:\\Users\\Aweso\\Downloads\\The folder\\Data\\CSV'

    get_files(files, base_url, download_path, extract_base_path)
    process_mat_files(extract_base_path, output_csv_dir)

if __name__ == '__main__':
    main()
