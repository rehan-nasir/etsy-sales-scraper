from bs4 import BeautifulSoup
import requests
import concurrent.futures
import re
import time

# Multithreading parsing for faster output, processes requests in parallel.


def get_listing_info(url):
    main_url = url
    id_array = []
    listing_url = "https://www.etsy.com/ca/listing/"
    response = requests.get(main_url)
    soup = BeautifulSoup(response.text, "lxml")
    listings = soup.find_all("a")
    for tag in listings:
        if tag.has_attr("data-listing-id"):
            id_array.append(tag["data-listing-id"])

    def get_item_info(listing_id):
        item = listing_url + listing_id
        r = requests.get(item)
        s = BeautifulSoup(r.text, "lxml")
        num_of_sales = ""
        seller = ""
        regex = re.compile(r'\bsales\b')
        span_tag = s.find('span', class_='wt-text-caption', text=regex)
        if span_tag is not None:
            num_of_sales = span_tag.getText().strip()
        link_tag = s.find('link', attrs={'rel': 'alternate', 'type': 'application/rss+xml'})
        if link_tag is not None:
            title_attr = link_tag.get('title')
            match = re.search(r'Shop RSS for (\w+) on Etsy', title_attr)
            seller = match.group(1)
        return "Seller: " + seller + "\n" + num_of_sales + "\n" + item + "\n----------------------------"

    results = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in id_array:
            results.append(executor.submit(get_item_info, i))

    for result in results:
        print(result.result())


def main():
    # The function below will print all info about all the sellers that appear on the home page. (Works on any Etsy URL)
    # get_listing_info("https://www.etsy.com/ca/")


if __name__ == '__main__':
    main()

#End of file
