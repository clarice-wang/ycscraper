import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_company_details(yc_url):
    response = requests.get(yc_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract website
    website_tag = soup.find('a', class_='mb-2 whitespace-nowrap md:mb-0')
    website = website_tag.find('div', class_='inline-block group-hover:underline').text.strip() if website_tag else None
    
    # Extract full description
    description_tag = soup.find('div', class_='prose max-w-full')
    full_description = description_tag.get_text(separator=' ', strip=True) if description_tag else None
    
    # Extract founder names
    founder_tags = soup.find_all('h3', class_='text-lg font-bold')
    founders = ', '.join(tag.text.strip() for tag in founder_tags)
    
    # Extract LinkedIn profiles
    linkedin_tags = soup.find_all('a', class_='inline-block h-5 w-5 bg-contain bg-image-linkedin')
    linkedin_profiles = ', '.join(tag['href'] for tag in linkedin_tags)
    
    return website, full_description, founders, linkedin_profiles

def scrape_website(file_path):
    # Read the HTML file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Find all the company info divs on the page
    company_elements = soup.find_all('a', class_='_company_86jzd_338')
    print(len(company_elements))

    # Extract the company details from the elements and store them in a list of tuples
    data = []
    base_url = "https://www.ycombinator.com"
    for company in company_elements:
        name = company.find('span', class_='_coName_86jzd_453').text.strip()
        description = company.find('span', class_='_coDescription_86jzd_478').text.strip()
        yc_url = base_url + company['href']

        # Fetch the company details by visiting the yc_url
        website, full_description, founders, linkedin_profiles = get_company_details(yc_url)
        
        # Find all industry tags and join them into a comma-separated string
        industry_tags = company.find_all('a', class_='_tagLink_86jzd_1023')
        industries = ', '.join(tag.text.strip() for tag in industry_tags)
        
        data.append((name, description, website, yc_url, industries, full_description, founders, linkedin_profiles))

    return data

def write_to_csv(data, filename):
    df = pd.DataFrame(data, columns=['Company Name', 'Description', 'Company Website', 'YC Website', 'Industries', 'Full Description', 'Founders', 'LinkedIn Profiles'])
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    file_path = "yc24.html"
    data = scrape_website(file_path)
    write_to_csv(data, 'yc_batch24.csv')