from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import requests
import csv
import os

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=Graphics%20Cards'
print("Downloading Page")
uClient = uReq(my_url)
print("Downloaded")
page_html = uClient.read()
uClient.close()
print("Souping")
page_soup = soup(page_html, "html.parser")
print("Souped")
print("Opening file")
fni = input("Enter a new filename to write to: ")
filename = fni
open(filename, "x")
f = open(filename, "w")
print("Opened")
headers = "brand, product_name, shipping\n"

print("Writing Headers")
f.write(headers)
print("Wrote")
print("Grabbing Items")
containers = page_soup.findAll("div",{"class":"item-container"})
print("Grabbed")
lyn = input("Show # Of Items [Y/n]")
if lyn == "":
    print(len(containers))
elif lyn == "y":
    print(len(containers))
elif lyn == "n":
    pass
else:
     print("err: Incorrect Input")
container = containers[0]
for container in containers:
    brand = container.find("div","item-info").div.a.img["title"]
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
    shipping_container = container.findAll("li", {"class":"price-ship" })
    shipping = shipping_container[0].text.strip()

    f.write("\n" + "brand: " + brand + "\n" + "product: " + product_name + "\n" + "shipping: " + shipping + "\n" + "---------------")
os.system("mv " + filename + " ~/Scrapes")