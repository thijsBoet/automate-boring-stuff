# need 3rd party module beautiful soup for web scraping HTML and XML files
import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('a-size-base a-color-price a-color-price')
    return elems[0].text.strip()

getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922')