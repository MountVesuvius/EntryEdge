import json, requests
from bs4 import BeautifulSoup
from multiprocessing.pool import ThreadPool as Pool

jobTypes = {
    'GRAD' : "graduate-jobs",
    'INTERN' : "internships",
    'CASUAL' : "casual-jobs",
    'PART' : "part-time-student-jobs",
    'ENTRY' : "entry-level-jobs"
}

BASE_URL = "https://au.gradconnection.com/"
URL = "https://au.gradconnection.com/internships/computer-science?page="

# PATTY = "https://au.gradconnection.com/guided-search/graduate-jobs/"
# response = requests.get(PATTY)

# soup = None
# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')

# links = soup.find_all('div', class_='discipline-group')

# table = {}
# for link in links:
#     a = link.find('a')
#     if a:
#         key = link.text.split('(')[0].strip(' ')
#         table[key] =  a['href'].strip('/').split('/')[-1]

# with open('discipline.json', 'w') as f:
#     json.dump(table, f, indent=4)

def scrape_page(url):
    response = requests.get(url)
    jobPostings = []

    soup = None
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

    # Stop blank pages crashing everything
    try:
        print("Scraping: ", url)
        sections = soup.find_all('section', class_="full-row")
    except AttributeError as e:
        print('No Content found')
        return None

    for section in sections:
        try:
            title = section.find('a', class_="box-header-title")
            company = section.find('div', class_="box-employer-name")
            description = section.find('p', class_="box-description-para")
            compLogo = section.find('img')
            if title:
                jobPostings.append({
                    'title': title.text,
                    'company': company.text,
                    'companyImg': compLogo['src'],
                    'description': description.text,
                    'jobLink': BASE_URL + title['href'][1:]
                })
        except AttributeError as e:
            continue

    print('Completed Scrape')
    return jobPostings

def scrape_pages_concurrently(urls):
    num_threads = 5

    with Pool(num_threads) as pool:
        results = pool.map(scrape_page, urls)
        
    # Flatten the list of lists.
    return [job for sublist in results for job in sublist]

with open('discipline.json', 'r') as f:
    areas = json.load(f)

table = {}
for area in areas:
    urls = []
    for job in jobTypes:
        urls.append(BASE_URL + jobTypes[job] + '/' + areas[area])
    content = scrape_pages_concurrently(urls)
    table[area] = content

with open('output.json', 'w') as f:
    json.dump(table, f, indent=4)