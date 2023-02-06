from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

html_data = response.text
soup = BeautifulSoup(html_data, 'html.parser')

titles = soup.find_all(name='h3', class_='title')
titles_list = []

for title in titles:
    titles_list.append(title.string)
titles_list.reverse()
# print(titles_list.reverse())

with open('text.txt', 'w', encoding="utf-8") as file:
    for title in titles_list:
        file.write(f"{title}\n")