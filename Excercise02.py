import requests
import bs4

data = requests.get("https://lotto.area04.com/")
bs4.BeautifulSoup(data)