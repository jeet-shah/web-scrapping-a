from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

starturl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("C:/Users/neels/Downloads/chromedriver_win32/chromedriver")
browser.get(starturl)
time.sleep(10)
def scrape():
    headers = ["NAME","LIGHT-YEARS FROM EARTH","PLANET MASS","STELLAR MAGNITUDE","DISCOVERY DATE"]
    planetdata = []
    for i in range(0,438):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ultag in soup.find_all("ul",attrs={"class","exoplanet"}):
            litag = ultag.find_all("li")
            templist = []
            for index,li_tag in enumerate(litag):
                if index == 0:
                    templist.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        templist.append(li_tag.contents[0])
                    except:
                        templist.append("")
            planetdata.append(templist)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("planet.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetdata)
scrape()