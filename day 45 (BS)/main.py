from bs4 import BeautifulSoup

with open('website.html', 'r') as file:
    data = file.read()

soup = BeautifulSoup(data, 'html.parser')

# all_a = soup.find_all(name='a')
# print(all_a)
#
# for tag in all_a:
#     print(tag.get('href'))

#
# name = soup.find_all(name='h3')
#
# for tag in name:
#     print(tag.string)
# heading = soup.find(name="h3", class_='heading')
# print(heading)


name = soup.select_one('#name')
print(name)

heading = soup.select(".heading")
print(heading)