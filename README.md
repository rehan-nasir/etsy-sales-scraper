## Etsy Sales Scraper

This Python script scrapes the Etsy website for information about sellers and their products. The script uses the `requests` and `BeautifulSoup` libraries to parse HTML data and extract relevant information. It also utilizes the `concurrent.futures` library to process requests in parallel for faster output.

This script functions properly as of February 2023.

### Usage

To parse a page, input a url as a string into `get_listing_info()`. Run the program, and it will display information about all the listings on that page, such as:
- Seller name
- The number of sales the seller has made.
- The link to the listing

Here is an example:
```
url = "https://www.etsy.com/"
get_listing_info(url)
```

To parse multiple URLs, you can create a list of URLs and call the `get_listing_info()` function for each URL in the list. It is advised to add a delay between each function call to avoid overloading the server with requests. 
Here is an example:
```
urls = ["https://www.etsy.com/ca/","https://www.etsy.com/ca/c/home-and-living","https://www.etsy.com/ca/c/clothing-and-shoes"]

for url in urls:
    get_listing_info(url)
    time.sleep(10)
```
This will call the `get_listing_info()` function for each URL in the list, with a delay of 10 seconds between each call.

### Output
The `get_listing_info()` function returns information about each seller in the following format:
```
Seller: [seller name]
[number of sales]
[listing URL]
----------------------------
```
