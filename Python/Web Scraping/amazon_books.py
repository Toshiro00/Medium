from bs4 import BeautifulSoup
import cloudscraper
import pandas as pd

book_urls = set()

url = 'https://www.amazon.com/gp/bestsellers/books/468204?ref_=Oct_d_obs_S&pd_rd_w=U7n8R&pf_rd_p=9aa64228-a828-4242-9935-e693c0cc3357&pf_rd_r=H1CMSKC4J6AM3K6D2WWH&pd_rd_r=842725d8-a360-4c73-bb92-aff14c5d0add&pd_rd_wg=pX4ql'

scraper = cloudscraper.create_scraper(
    browser = {
        'browser': 'chrome',
        'platform': 'windows',
        'desktop': True
    }
)

# Get HTML as text
text = scraper.get(url).text

# Parse it with Soup 😋
soup = BeautifulSoup(text, 'html.parser')

# Find first div in page.
books = soup.find('div', {'id': 'a-page'})

# Find div for individual book.
books = books.find_all('div', {'id': 'gridItemRoot'})

# Iterate over books and find div inside individual book
for book in books:
    data = book.findAll('div')

    # Book Links ## If you use 'href' it will return just links
    # So you can use a['href'] as simple.
    a = data[0].find_all('a', href=True)

    # Book names, prices, etc. but useless for now.
    # We can extract it from visiting links very easily
    span = data[0].find_all('span')

    # Iterate over all links (a) and extract 'href' inside
    for i in a:
        # We dont want useless links so you need to check your output everytime.
        # Removed product reviews links. They already inside in the book page.

        if 'product' not in i['href'] and '/e/' not in i['href']:
            # Add to set because there can be multiple links.
            # And add amazon url head of 'href'
            book_urls.add('https://www.amazon.com' + i['href'])

# Create DataFrame for extract whatever format you want.
books_df = pd.DataFrame(book_urls, columns=['URLs'])
books_df.to_csv('amazon_books.csv')

for book_url in books_df['URLs'].values[:1]:
    
    url = book_url
    text = scraper.get(url).text
    soup = BeautifulSoup(text, 'html.parser')
    book_page = soup.find('div', {'id': 'a-page'})
    title = book_page.findAll('span', {'id': 'productTitle'})
    price = book_page.findAll('span', {'id': 'newBuyBoxPrice'})
    print('Title : \t', title[0].getText())
    print('Price : \t', price[0].getText())
