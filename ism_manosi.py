from bs4 import BeautifulSoup
import requests 
from latincrill import transliter


def ism_manosi_funksiyasi(ism):
    url = f"https://ismlar.com/uz/name/{ism}"
    response = requests.get(url=url)

    soup = BeautifulSoup(response.content, 'html5lib') 
    natija = soup.find("div", attrs={"class":"space-y-4"})
    try:
        natija = transliter(natija.p.text.strip())
    except:
        natija = False
    return natija

