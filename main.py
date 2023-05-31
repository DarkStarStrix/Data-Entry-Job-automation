# data entry job application using beautifulsoup4 and selenium
import csv
import time
from datetime import datetime

import ver as ver
from bs4 import BeautifulSoup
from selenium import webdriver

find_element_by_xpath = webdriver.find_element_by_xpath
location = webdriver.location
Keys = webdriver.Keys
driver = webdriver.Chrome()
driver.get = webdriver.get
driver.page_source = webdriver.page_source
soup = BeautifulSoup(driver.page_source, "html.parser")
cards = soup.find_all("div", "job search-SerpJobCard")

# open the browser
driver = webdriver.Chrome()
driver.get()
driver.page_source = webdriver.page_source
soup = BeautifulSoup(driver.page_source, "html.parser")

# find the search bar and enter the job title
search = driver.find_element_by_xpath('//*[@id="text-input-what"]')
search.send_keys("data entry")
search.send_keys(Keys.RETURN)
time.sleep(2)

# find the location bar and enter the location
# find the search button and click it
# find the job title, company name, location, and salary
card = cards[0]
atag = card.h2.a
job_title = atag.get("title")
job_url = "https://www.indeed.com" + atag.get("href")
company = card.find("span", "company").text.strip()
job_location = card.find("div", "recJobLoc").get("data-rc-loc")
job_summary = card.find("div", "summary").text.strip()
post_date = card.find("span", "date").text.strip()
today = datetime.today().strftime("%Y-%m-%d")
try:
    job_salary = card.find("span", "salaryText").text.strip()
except AttributeError:
    job_salary = ""

record = (job_title, company, job_location, post_date, today, job_summary, job_salary, job_url)
print(record)

# store the job data in a data structure
records = []
url = "https://www.indeed.com" + soup.find("a", {"aria-label": "Next"}).get("href")


# extract the job data
def get_record(card):
    """Extract job data from a single record"""
    atag = card.h2.a
    job_title = atag.get("title")
    job_url = "https://www.indeed.com" + atag.get("href")
    company = card.find("span", "company").text.strip()
    job_location = card.find("div", "recJobLoc").get("data-rc-loc")
    job_summary = card.find("div", "summary").text.strip()
    post_date = card.find("span", "date").text.strip()
    today = datetime.today().strftime("%Y-%m-%d")
    try:
        job_salary = card.find("span", "salaryText").text.strip()
    except AttributeError:
        job_salary = ""

    record = (job_title, company, job_location, post_date, today, job_summary, job_salary, job_url)

    return record


while True:
    driver.get()
    soup = BeautifulSoup(driver.page_source, "html.parser")
    cards = soup.find_all("div", "job search-SerpJobCard")

    for card in cards:
        get_record(card)
        records.append(record)

    try:
        url = "https://www.indeed.com" + soup.find("a", {"aria-label": "Next"}).get("href")
    except AttributeError:
        break

# save the job data
with open("results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["JobTitle", "Company", "Location", "PostDate", "ExtractDate", "Summary", "Salary", "JobUrl"])
    writer.writerows(records)
    ver.get()
time.sleep(2)

# find the search bar and enter the job title
search = driver.find_element_by_xpath('//*[@id="text-input-what"]')
search.send_keys("data entry")
search.send_keys(Keys.RETURN)
time.sleep(2)


# find the location bar and enter the location
# find the search button and click it
# find the job title, company name, location, and salary


def get_url(position, location):
    """Generate an url from position and location"""
    template = "https://www.indeed.com/jobs?q={}&l={}"
    url = template.format(position, location)
    return url


url = get_url("data entry", "new york")
print(url)


# extract the job data
# loop through each page


def get_record(card):
    """Extract job data from a single record"""
    atag = card.h2.a
    job_title = atag.get("title")
    job_url = "https://www.indeed.com" + atag.get("href")
    company = card.find("span", "company").text.strip()
    job_location = card.find("div", "recJobLoc").get("data-rc-loc")
    job_summary = card.find("div", "summary").text.strip()
    post_date = card.find("span", "date").text.strip()
    today = datetime.today().strftime("%Y-%m-%d")
    try:
        job_salary = card.find("span", "salaryText").text.strip()
    except AttributeError:
        job_salary = ""

    record = (job_title, company, job_location, post_date, today, job_summary, job_salary, job_url)

    return record


# store the job data in a data structure


def main(position, location):
    """Run the main program routine"""
    records = []
    url = get_url(position, location)

    # extract the job data
    while True:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        cards = soup.find_all("div", "job search-SerpJobCard")

        for card in cards:
            record = get_record(card)
            records.append(record)

        try:
            url = "https://www.indeed.com" + soup.find("a", {"aria-label": "Next"}).get("href")
        except AttributeError:
            break

    # save the job data
    with open("results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["JobTitle", "Company", "Location", "PostDate", "ExtractDate", "Summary", "Salary", "JobUrl"]
        )
        writer.writerows(records)

    return records


# run the main program routine
main("data entry", "new york")

# close the browser
driver.close()

# use the data structure to analyze the data
job_title = []
company = []
location = []
post_date = []
extract_date = []
summary = []
salary = []
job_url = []

job_title.append(record[0])
company.append(record[1])

job_title = [record[0] for record in records]
company = [record[1] for record in records]
location = [record[2] for record in records]
post_date = [record[3] for record in records]
extract_date = [record[4] for record in records]
summary = [record[5] for record in records]
salary = [record[6] for record in records]
job_url = [record[7] for record in records]

# store the results in a csv file
# open the csv file
with open("results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(
        ["JobTitle", "Company", "Location", "PostDate", "ExtractDate", "Summary", "Salary", "JobUrl"]
    )
    writer.writerows(records)
