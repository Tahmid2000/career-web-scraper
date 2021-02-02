import requests
import bs4
import webbrowser
res = requests.get(
    'https://www.indeed.com/jobs?q=software+engineer+intern&l=Plano%2C+TX&sort=date')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('.jobsearch-SerpJobCard > .title > a')
companies = soup.select('.company')
print(len(companies))
print(len(links))
for comp, job in zip(companies, links):
    print(comp.text + ' ' + job['title'] +
          ' ' + 'https://indeed.com'+job['href'])
