from bs4 import BeautifulSoup
import requests
URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(URL)
hundred_movies_data = response.text

soup = BeautifulSoup(hundred_movies_data, 'html.parser')

movies_titles_tags = soup.find_all('h3', class_='title')
movies_titles = [title.getText() for title in movies_titles_tags]

with open('movies.txt', 'w') as file:
    movies_titles.reverse()
    for title in movies_titles:
        file.write(f'{title}\n')
        

