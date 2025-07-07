import requests
from bs4 import BeautifulSoup
import csv

url = 'http://books.toscrape.com/catalogue/page-1.html'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

with open('Level 2/books.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price'])
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text.strip()
        writer.writerow([title, price])

print("Data scraped and saved to books.csv")