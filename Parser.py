import lxml
import re
import requests
from bs4 import BeautifulSoup

to_string = ''

max_page = 10
pages = []

for x in range(1, max_page + 1):
    pages.append(requests.get('https://auto.drom.ru/new/all/page' + (str(x))))

for r in pages:
    soup = BeautifulSoup(r.content, 'html.parser')

    obj = soup.findAll('div', attrs={'class': "b-advItem__header"})
    obj[0].findAll('div', attrs={'class': "b-advItem__title"})

    obj2 = [item.find('div', attrs={'class': "b-advItem__title"}).text.strip() for item in obj]

    to_string = to_string + "\n" + str(obj2)

    text1 = to_string.replace("[", "")
    text2 = text1.replace("]", "")
    lst = text2.split(", '")

    my_file = open('Car Price more 1500000.txt', 'w')

    for i in range(len(lst)):
        text_for_file = (lst[i] + "\n").replace("'", "")
        my_file.write(text_for_file)
    my_file.close()
