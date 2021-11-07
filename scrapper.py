#Pabanjyoti, 2021

import os                           #for interacting with the system
import datetime                     #for renaming the newspaper 
import requests                     #for fetching the source-html and downloading
from bs4 import BeautifulSoup       #for scrapping

os.system("title Dainik Asam Scrapper")
os.system('cls' if os.name == 'nt' else 'clear')
print('\n\n███████╗ ██████╗██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ \n'
'██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗\n'
'███████╗██║     ██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝\n'
'╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗\n'
'███████║╚██████╗██║  ██║██║  ██║██║     ██║     ███████╗██║  ██║\n'
'╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝\n'
'░ ░▒  ░   ░ ▒ ░ ░ ░░   ░ ▒░  ░ by ░▒ ░ ▒░ ░ ▒ ▒░   ░ ▒░  ░ ▒ ▒░ \n'
'░  ░  ░   ▒ ░ ░   ┌─┐┌─┐┌┐ ┌─┐┌┐┌ ┬┬ ┬┌─┐┌┬┐┬ ▒ ░ ░ ▒  ░ ░ ░ ▒  \n'
'     ░    ░       ├─┘├─┤├┴┐├─┤│││ │└┬┘│ │ │ │░ ░           ░ ░  \n'
'░ ░▒  ░ ░ ▒ ░░ ░░ ┴  ┴ ┴└─┘┴ ┴┘└┘└┘ ┴ └─┘ ┴ ┴   ░ ▒ ▒░   ░ ▒ ▒░ \n'
'\nScrapping links, please wait...\n\n')

#fetches today's date
today = datetime.datetime.today().strftime ('%d-%b-%Y')

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

    #downloads the pdf and rename them according to the newspaper name
    if link == arr[0]:
        print('\nDownloading latest edition of Dainik Asam:')
        fname = f'Dainik_Asam_{today}.pdf'
        r = requests.get(pdfLink)
        open(fname , 'wb').write(r.content)
        print('done')
    else:
        print('\n\nDownloading latest edition of Assam Tribune:')
        fname = f'Assam_Tribune_{today}.pdf'
        r = requests.get(pdfLink)
        open(fname , 'wb').write(r.content)
        print('done')
