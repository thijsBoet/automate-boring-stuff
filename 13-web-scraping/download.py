# requests 3rd party module for downloading files
import requests

# returns a response object
res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
# res.raise_for_status() == True for success | Raises exception for False
if res.status_code == 200:
    print(len(res.text))

downloadedFile = open('RomeoAnfJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
    downloadedFile.write(chunk)

downloadedFile.close()