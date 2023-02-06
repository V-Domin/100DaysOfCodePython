from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')

html_data = response.text
soup = BeautifulSoup(html_data, 'html.parser')

articles = soup.find_all(name='span', class_='titleline')
links = soup.select('.titleline a')

articles_text = []
articles_link = [link.get('href') for link in links]
new_article_links = []

for link in articles_link:
    if link.startswith("from"):
        pass
    else:
        new_article_links.append(link)

for article in articles:
    article_text = article.getText()
    articles_text.append(article_text)

article_upvotes = [int(score.getText().split()[0]) for score in soup.select('.score')]


high_votes = max(article_upvotes)
index_high_votes = article_upvotes.index(high_votes) + 1




print(articles_text[index_high_votes])
print(new_article_links[index_high_votes])
# print(high_votes)
