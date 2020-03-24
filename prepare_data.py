import requests
import zipfile
import os

shots_1_path = 'http://peter-tanner.com/moneypuck/downloads/shots_2007-2018.zip'
shots_2_path = 'http://peter-tanner.com/moneypuck/downloads/shots_2019.zip'
os.chdir('data/raw')

with open('shots_2007-2018.zip','wb') as f:
    r = requests.get(shots_1_path, allow_redirects=True)
    f.write(r.content)

with open('shots_2019.zip','wb') as f:
    r = requests.get(shots_2_path, allow_redirects=True)
    f.write(r.content)

with zipfile.ZipFile('shots_2007-2018.zip','r') as zip_ref:
    zip_ref.extractall('../processed/')

with zipfile.ZipFile('shots_2019.zip','r') as zip_ref:
    zip_ref.extractall('../processed/')
