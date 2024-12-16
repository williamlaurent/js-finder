# paypal.me/@williamlawww
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_js_files(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the page {url}. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    script_tags = soup.find_all('script')

    js_files = [urljoin(url, tag.get('src')) for tag in script_tags if tag.get('src') and tag.get('src').endswith('.js')]

    return js_files

def process_urls_from_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        urls = infile.readlines()

    all_js_files = []
    for url in urls:
        url = url.strip()
        print(f"Processing URL: {url}")
        js_files = fetch_js_files(url)
        all_js_files.extend(js_files)

    with open(output_file, 'w') as file:
        for js_file in all_js_files:
            file.write(f"{js_file}\n")

    print(f"Found {len(all_js_files)} JavaScript files in total.")

if __name__ == "__main__":
    input_file = 'list.txt'
    output_file = 'result.txt'
    process_urls_from_file(input_file, output_file)
