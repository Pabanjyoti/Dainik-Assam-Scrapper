#Pabanjyoti, 2021

from bs4 import BeautifulSoup       #for scrapping
import requests                     #for fetching the source-html
import os                           #for interacting with the system
import webbrowser                   #for opening the download links

os.system("title Dainik Asam Scrapper")
os.system('cls' if os.name == 'nt' else 'clear')
print('\nScrapping links, please wait...\n')

#two urls for both papers
arr = ['https://dainikasam.assamtribune.com', 'https://epaper.assamtribune.com']

for link in arr:

    #fetches source of the webpage from links of the above array
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')

    #get session id
    sessionId = soup.find("div", {"id":"content"})['data-query-sessionid']

    #get link for today's paper
    paperLink = link + soup.find("a", {"class":"head-anchor"})['href']

    #extract paper code for today's paper
    paperCode = paperLink.split("/")[-1]

    #construct link for api-call 
    pdfLink = link + '/content/servlet/RDESController?command=rdm.ServletDownloadEPaper&epaperId=' + paperCode + '&pageNo=all'

    #open download link in the default web-browser
    webbrowser.open_new_tab(pdfLink)
