
from bs4 import BeautifulSoup
import requests

fnout ='' # making this a global variable
def get_files():
    #files = ['DB1', 'DB2', 'DB4','DB7']

    # loop to make urls
    # loop over urls

    response = requests.get('https://ninapro.hevs.ch/instructions/DB1.html')
    webpage = response.text
    soup = BeautifulSoup(webpage, 'html.parser')
    soup.find_all('a')
    urls = []
    for link in soup.find_all('a'):
        s = link.get('href')
        type(s)
        if(s.endswith('.zip')):
            s = s[3:]
            hold =  'https://ninapro.hevs.ch/'  + s
            urls.append(hold)

    for url in urls:
        # https://ninapro.hevs.ch/files/DB1/Preprocessed/s1.zip
        print(url)
        r = requests.get(url)
        urlparts = url.split('/')
        fnout = 'C://mydata/' + urlparts[-2] + '/' + urlparts[-1]
        with open(fnout, 'wb') as f:
            f.write(r.content)

def unzip():
    import zipfile
    with zipfile.ZipFile(fnout, 'r') as zip_ref:
        zip_ref.extractall() # new name with .mat

def translate():
    from scipy.io import loadmat
    import pandas as pd
    mat = loadmat('filename') # .mat filename
    mat = {k :v for k, v in mat.items() if k[0] != '_'}
    data = pd.DataFrame({k: pd.Series(v[0]) for k, v in mat.items()})
    data.to_csv('') # create csv filename

def preprocessing():
    # load and process csv
    pass

def main():
    # get_files()



if __name__ == '__main__':
    main()
