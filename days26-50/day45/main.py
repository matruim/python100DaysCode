from bs4 import BeautifulSoup
import requests

#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
#
# print(soup.a)
#
# all_anchor_tags = soup.findAll(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)


# res = requests.get("https://news.ycombinator.com/news")
# soup = BeautifulSoup(res.text, "html.parser")
# all_anchor_tags = soup.select(".titleline > a")
# all_scores = [int(score.getText().split()[0]) for score in soup.select(".score")]
# print(all_anchor_tags)
# print(all_scores)
# max_score_index = all_scores.index(max(all_scores))
# print(all_scores[max_score_index], all_anchor_tags[max_score_index].getText(), all_anchor_tags[max_score_index].get('href'))


res = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(res.text, "html.parser")
gallery = soup.find(class_="gallery")
titles = [title.getText() for title in gallery.select(".title")]
titles.reverse()
with open("movies.txt", mode="w") as file:
    for title in titles:
        file.write(f"{title}\n")
