import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.worldweatheronline.com/beirut-weather/beyrouth/lb.aspx')
soup =  BeautifulSoup(url.content ,'html.parser')
humidity = soup.find(class_="row p-3 bg-light")
humidity_1= humidity.find(class_="col-lg-8 border rounded border").find(class_="col-12 pt-3 pb-3 border-bottom")
print(humidity_1 ,"\n\n\n")
toPrint = humidity_1.find('h5').get_text()
print(toPrint)