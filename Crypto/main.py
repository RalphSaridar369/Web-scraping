import requests
from bs4 import BeautifulSoup

urlETH= requests.get('https://www.coindesk.com/price/ethereum')
pageETH =BeautifulSoup(urlETH.content,'html.parser')
ETHinfo=pageETH.find(class_="coin-info-list price-list")
ETHprice = ETHinfo.findAll(class_="coin-info-block")[0].find(class_="data-definition").find(class_="price-large").get_text()
ETHpct= ETHinfo.findAll(class_="coin-info-block")[1].find(class_="data-definition").find(class_="percent-change-medium").get_text()

if(ETHinfo.findAll(class_="coin-info-block")[1].find(class_="data-definition").find(class_="percent-change-medium").find(class_="chevron-arrow price-up")):
    ETHarrow="+ "

else:
    ETHarrow="- "

urlBTC=requests.get('https://www.coindesk.com/price/bitcoin')
pageBTC= BeautifulSoup(urlBTC.content,'html.parser')
BTCinfo=pageBTC.find(class_="coin-info-list price-list")
BTCprice= BTCinfo.findAll(class_="coin-info-block")[0].find(class_="data-definition").find(class_="price-large").get_text()
BTCpct= BTCinfo.findAll(class_="coin-info-block")[1].find(class_="data-definition").find(class_="percent-change-medium").get_text()

if(BTCinfo.findAll(class_="coin-info-block")[1].find(class_="data-definition").find(class_="percent-change-medium").find(class_="chevron-arrow price-up")):
    BTCarrow="+ "

else:
    BTCarrow="- "

urlLTC=requests.get('https://www.coindesk.com/price/litecoin')
pageLTC= BeautifulSoup(urlLTC.content,'html.parser')
LTCinfo=pageLTC.find(class_="coin-info-list price-list")
LTCprice= LTCinfo.findAll(class_="coin-info-block")[0].find(class_="data-definition").find(class_="price-large").get_text()
LTCpct= LTCinfo.findAll(class_="coin-info-block")[1].find(class_="data-definition").find(class_="percent-change-medium").get_text()

if(LTCinfo.findAll(class_="coin-info-block")[1].find(class_="data-definition").find(class_="percent-change-medium").find(class_="chevron-arrow price-up")):
    LTCarrow="+ "

else:
    LTCarrow="- "

urlADA=requests.get('https://www.coindesk.com/price/cardano')
pageADA= BeautifulSoup(urlADA.content,'html.parser')
ADAinfo=pageADA.find(class_="coin-info-list price-list")
ADAprice= ADAinfo.findAll(class_="coin-info-block")[0].find(class_="data-definition").find(class_="price-large").get_text()
ADApct= ADAinfo.findAll(class_="coin-info-block")[1].find(class_="data-definition").find(class_="percent-change-medium").get_text()

if(ADAinfo.findAll(class_="coin-info-block")[1].find(class_="data-definition").find(class_="percent-change-medium").find(class_="chevron-arrow price-up")):
    ADAarrow="+ "

else:
    ADAarrow="- "

print("Bitcoin:\n","Price: ",BTCprice,"\n","Percentage: ",BTCarrow,BTCpct,"\n")
print()
print("Litecoin:\n","Price: ",LTCprice,"\n","Percentage: ",LTCarrow,LTCpct,"\n")
print()
print("Cardano:\n","Price: ",ADAprice,"\n","Percentage: ",ADAarrow,ADApct,"\n")
print()
print("Ethereum:\n","Price: ",ETHprice,"\n","Percentage: ",ETHarrow,ETHpct,"\n")
print()
