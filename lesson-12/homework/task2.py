from bs4 import BeautifulSoup
import sqlite3
import requests
import csv

connection = sqlite3.connect("jobs.db")
cursor = connection.cursor() 

create = """
    Create table jobs(Job_Title TEXT, Company_Name TEXT, Location TEXT, Job_Description TEXT, Application_Link TEXT)
"""

cursor.execute(create) 

url = "https://realpython.github.io/fake-jobs"
response = requests.get(url) 
soup = BeautifulSoup(response.text, "html.parser") 

job_title = [title.get_text(strip = True) for title in soup.find_all(class_ = "title is-5")] 
company_name = [name.get_text(strip = True) for name in soup.find_all(class_ = "subtitle is-6 company")] 
location = [address.get_text(strip = True) for address in soup.find_all(class_ = "location")] 
job_description = [content.find("p").get_text(strip=True) for content in soup.find_all("div", class_="content")]
application_link = [a["href"] for a in soup.find_all("a", class_ = "card-footer-item")] 

insert = """
    INSERT INTO jobs (Job_Title, Company_Name, Location, Job_Description, Application_Link) VALUES (?, ?, ?, ?, ?)
"""

update = """
    UPDATE jobs SET Job_Description = ?, Application_Link = ? WHERE Job_Title = ? AND Company_Name = ? AND Location = ?
"""

new_entries = 0
updated_entries = 0

for job, company, loc, desc, link in zip(job_title, company_name, location, job_description, application_link):
    cursor.execute("SELECT Job_Description, Application_Link FROM jobs WHERE Job_Title = ? AND Company_Name = ? AND Location = ?", (job, company, loc)) 
    existing = cursor.fetchone() 
    
    if existing is None:
        cursor.execute(insert, (job, company, loc, desc, link))
        new_entries += 1
    else:
        old_desc, old_link = existing
        if old_desc != desc or old_link != link:
            cursor.execute(update, (desc, link, job, company, loc))
            updated_entries += 1 

def export_jobs(filter_by: str, value: str, filename: str = "filtered_jobs.csv"):
    query = f"SELECT * FROM jobs WHERE {filter_by} = ?"
    cursor.execute(query, (value,))
    jobs = cursor.fetchall() 

    if not jobs:
        print(f"No jobs found for {filter_by} = {value}")
        return
    
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company Name", "Location", "Job Description", "Application Link"])
        writer.writerow(jobs) 

connection.commit()
connection.close() 