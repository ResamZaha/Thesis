import requests
from bs4 import BeautifulSoup
import os

def download_links_from_webpage(url):
    # Sending a GET request to the webpage
    response = requests.get(url)
    
    # Checking if the request was successful (status code 200)
    if response.status_code == 200:
        # Parsing the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Finding all anchor tags (links) in the webpage
        links = soup.find_all('a')
        
        # Creating a directory to save the downloaded files
        if not os.path.exists('downloaded_links'):
            os.makedirs('downloaded_links')
        
        # Iterating through each link
        for link in links:
            href = link.get('href')
            if href and href.startswith('https://phl.carto.com/api/v2/sql'):
                
                # Extracting filename from the URL
                filename : str = link.text.strip()
                if(filename == ""):
                    continue
                if(filename.find("CSV")):
                    filename = filename + ".csv"
                else:
                    filename = filename + ".zip"
                
                print(f"Downloading: {filename}")

                # Downloading the content of the link
                link_response = requests.get(href)
                if link_response.status_code == 200:
                    # Saving the content to a file in the 'downloaded_links' directory
                    with open(os.path.join('downloaded_links', filename), 'wb') as f:
                        f.write(link_response.content)
                    print(f"Downloaded: {filename}")
                else:
                    print(f"Failed to download: {href}")
            else:
                print(f"Not a valid link: {href}")
    else:
        print("Failed to retrieve webpage")

# Example usage:
webpage_url = "https://opendataphilly.org/datasets/crime-incidents/"
download_links_from_webpage(webpage_url)
