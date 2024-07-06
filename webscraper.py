import os
import zipfile
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from scipy.io import loadmat
import pandas as pd

def get_files(dbs, base_url, download_path):
    """
    Download and unzip files from a website.

    :param files: List of file identifiers to be processed.
    :param base_url: The base URL to form the download links.
    :param download_path: Path to download the zipped files.
    """
    # Ensure the download directory exists
    os.makedirs(download_path, exist_ok=True)

    for db in dbs:
        response = requests.get(f'{base_url}{db}.html')
        if response.status_code != 200:
            print(f"Failed to retrieve {db}.html")
            continue

        webpage = response.text
        soup = BeautifulSoup(webpage, 'html.parser')

        urls = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.endswith('.zip'):
                full_url = urljoin(base_url, href)
                urls.append(full_url)

        for url in urls:
            try:
                print(f'Downloading from: {url}')
                r = requests.get(url)
                r.raise_for_status()

                filename = os.path.basename(url)
                db_dir = os.path.join(download_path, db)
                os.makedirs(db_dir, exist_ok=True)
                fnout = os.path.join(db_dir, filename)

                with open(fnout, 'wb') as f:
                    f.write(r.content)

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

def unzip_all_files(dirpath):
    for root, _, files in os.walk(dirpath):
        for fn in files:
            if not fn.startswith('.'):
                fpin = os.path.join(root, fn)
                fpout = root.replace('zip', 'mat')
                unzip(fpin, fpout)

def translate(mat_file, output_csv):
    """
    Translate a .mat file to a .csv file.

    :param mat_file: Path to the .mat file.
    :param output_csv: Path to the output .csv file.
    """
    print('Starting mat translate for', mat_file)
    mat = loadmat(mat_file)
    mat = {k: v for k, v in mat.items() if k[0] != '_'}

    data = {}
    for k, v in mat.items():
        if len(v) == 1:
            data[k] = v[0][0]
        elif all(len(v[x]) == 1 for x in range(len(v))):
            data[k] = [v[x][0] for x in range(len(v))]
        else:
            lists = v.transpose().tolist()
            for i, l in enumerate(lists):
                data[f'{k}{i}'] = l
    # for key,value in data.items():
          #print(key,len(value))

    df = pd.DataFrame(data)
    df.to_csv(output_csv, index=False)

def process_mat_files(extract_base_path):
    """
    Process all .mat files in the extracted directories and translate them to CSV.

    :param extract_base_path: Base path where the files were extracted.
    """

    for root, _, files in os.walk(extract_base_path):
        print(root)
        os.makedirs(root.replace('mat', 'csv'), exist_ok=True)
        for file in files:
            if not 'DB1'in root and not'DB2' in root:
                if file.endswith('.mat'):
                    mat_file_path = os.path.join(root, file)
                    csv_file_path = mat_file_path.replace('mat', 'csv')
                    translate(mat_file_path, csv_file_path)

def main():
    dbs = ['DB1', 'DB2', 'DB4']  # List of files to be processed
    base_url = 'https://ninapro.hevs.ch/instructions/'
    download_path = 'C:\\Users\\Aweso\\Downloads\\The folder\\Data\\'
  #  get_files(dbs, base_url, download_path)
    extract_base_path = download_path.replace('zip', 'mat')
    #unzip_all_files(download_path)

    process_mat_files(extract_base_path)

if __name__ == '__main__':
    main()
