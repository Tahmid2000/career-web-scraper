import requests
import bs4
import webbrowser
import http.cookiejar
import mechanicalsoup


def indeedScraper():
    res = requests.get(
        'https://www.indeed.com/jobs?q=software+engineer+intern&l=')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.jobsearch-SerpJobCard > .title > a')
    companies = soup.select('.company')
    locations = soup.select('.location')
    for comp, job, location in zip(companies, links, locations):
        print(comp.text.strip('\t\r\n') + '--' + job['title'] +
              '--' + 'https://indeed.com'+job['href'] + '--' + location.text)


def linkedinScraper():
    res = requests.get(
        'https://www.linkedin.com/jobs/search?keywords=software%2Bengineer%2Bintern&location=United%2BStates&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.result-card__full-card-link')
    titles = soup.select(
        '.result-card__full-card-link > .screen-reader-text')
    companies = soup.select(
        '.job-result-card__subtitle-link')
    locations = soup.select(
        '.job-result-card__location')
    for title, job, comp, location in zip(titles, links, companies, locations):
        print(comp.text.strip('\t\r\n') + '--' +
              title.text.strip('\t\r\n') + '--' + job['href'] + '--' + location.text)


def zipRecruiterScraper():
    res = requests.get(
        'https://www.ziprecruiter.com/Jobs/Software-Engineer-Intern/--in-Texas')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    links = soup.select(
        '.job_link')
    titles = soup.select('.title')
    companies = soup.select('.company_name')
    locations = soup.select('.company_location')
    for title, job, comp, location in zip(titles, links, companies, locations):
        if 'Software' in title.text:
            print(comp.text.strip() + '--' +
                  title.text.strip('\t\r\n') + '--' + job['href'] + '--' + location.text.strip())


if __name__ == "__main__":
    indeedScraper()
    print('\n')
    linkedinScraper()
    print('\n')
    zipRecruiterScraper()
