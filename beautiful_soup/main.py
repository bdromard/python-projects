from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
yc_titles_tags = soup.select('span.titleline a[rel="noreferrer"]')
yc_span_scores = soup.select('span.subline span.score')

# Creatings lists of all articles, links and number of upvotes on main page
articles_titles = []
articles_links = []
for tag in yc_titles_tags:
    article_title = tag.getText()
    article_link = tag.get('href')
    articles_titles.append(article_title)
    articles_links.append(article_link)

articles_upvotes = [int(score.getText().split()[0]) for score in yc_span_scores]
most_upvoted_article_index = articles_upvotes.index(max(articles_upvotes))

# Printing out the highest upvoted article, with link and number of upvotes
print(articles_titles[most_upvoted_article_index])
print(articles_links[most_upvoted_article_index])
print(articles_upvotes[most_upvoted_article_index])

# Parsing website.html
#with open("./website.html", "r") as website:
#    contents = website.read()
#   
#soup = BeautifulSoup(contents, 'html_parser')   
