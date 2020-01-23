from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector(
    '.main > ul:nth-child(16) > li:nth-child(1) > a:nth-child(1)')
print(elem)
elem.click()

# --------------------------------------------------------------------------------------------------------
elems = browser.find_elements_by_css_selector('p')

google = webdriver.Firefox()
google.get('https://www.google.com')

searchElem = google.find_element_by_css_selector('.gLFyf')
searchElem.send_keys('python 3.9')
searchElem.submit()

# --------------------------------------------------------------------------------------------------------
wiki = webdriver.Firefox()
wiki.get('https://en.wikipedia.org/wiki/Main_Page')

wikiSearchElem = wiki.find_element_by_css_selector('#searchInput')
wikiSearchElem.send_keys('Guido van Rossum')
wikiSearchElem.submit()

summary = wikiSearchElem.find_element_by_css_selector('.mw-parser-output > p:nth-child(5)')
print(summary.text)

wikiSearchElem.back()
wikiSearchElem.forward()
wikiSearchElem.refresh()
wikiSearchElem.quit()
