from bs4 import BeautifulSoup
import requests 

def getListingFromUrl(url):
    listing = {}
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()
    
