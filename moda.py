
from turtle import pd
from types import NoneType
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import csv
import pandas as pd

url = "https://www.modaselvim.com/outwear?ps=10"
client = urlopen(url)

html = client.read()



client.close()

soup= bs(html,"html.parser")
products = soup.find_all("div", {"class": "yeni-border-liste col col-12 altProductBar tooltipWrapper whiteBg"})
len(products)

bs.prettify(products[0])



f = open("C:/Users/nasy1/Desktop/moda.csv", "w", encoding='utf-8')
header="p_name\t\t\t\t\t\t\t\tp_price\t\t\t\t\t\tp_image\n"
f.write(header)

for product in products :
           jtitle = product.find_all("a",{"class":"productDescription detailLink"})
           p_name=jtitle[0].text.strip()
           
           cname = product.find_all("span" ,{"class":"product-price text-line"})
           price=float(cname[0].text.strip())
           discount=price*(11/100)
           m_price=price-discount
           r_price=round(m_price,2)
           p_price=str(r_price)
           
           
           
        
           jtype = product.find_all("img",{"class":"active"})
           p_image = jtype[0]["src"]
           
           #print(p_name)
           #print(p_price)
           #print(p_image)
           #print()

           f.write(p_name +"\t\t\t" + p_price + "\t\t\t"+p_image + "\n")
f.close()
pd.read_csv("C:/Users/nasy1/Desktop/moda.csv")


