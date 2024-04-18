import requests
from bs4 import BeautifulSoup as bs

with open('E:\Pandas\Web Scrapping\sample.html','r') as f:
    html_docs = f.read()

soup = bs(html_docs,'html.parser')

# print(soup.prettify())
# print(soup.title.string)
# print(soup.div)

# print(soup.find_all('div')[1])
# print(soup.find_all('a')[0].text)

# print(soup.select('div.arjun'))
# print(soup.select('span#temp'))
# print(soup.span.get('class'))

# print(soup.find(id='temp'))
# print(soup.find(class_='arjun'))


# print(soup.find(class_='container').children)

# # for i in soup.find(class_='container').children:
# #     print(i)

# for i in soup.find(class_='child').parents:
#     print(i)

cont = soup.find(class_='container')
print(cont)
cont.name = 'span'
cont['class'] = 'first second third'
print(cont)