from bs4 import BeautifulSoup
import requests

def extract_product_info(soup):
    product_info = {
        'Title': '',
        'Price': 'Unknown',
        'Rating': '',
        'Number of Reviews': '',
        'Availability': 'Not Available'
    }

    availability = soup.find("div", attrs={'id': 'availability'})
    product_info['Availability'] = availability.span.string.strip() if availability else "Not Available"

    if product_info['Availability'] != "Not Available":
        title = soup.find("span", attrs={"id": 'productTitle'})
        product_info['Title'] = title.string.strip() if title else ""

        price = soup.find("div", attrs={'id': 'qualifiedBuybox'}).find("span", attrs={"class": "a-offscreen"})
        product_info['Price'] = price.string.strip() if price else "Unknown"

        review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'})
        product_info['Number of Reviews'] = review_count.string.strip() if review_count else ""

        rating = soup.find("span", attrs={'class': 'a-icon-alt'}) or soup.find("i", attrs={
            'class': 'a-icon a-icon-star a-star-4-5'})
        product_info['Rating'] = rating.string.strip() if rating else ""

    return product_info


if __name__ == '__main__':
    # Headers for request
    HEADERS = {'User-Agent': 'Your-User-Agent', 'Accept-Language': 'en-US'}

    # The webpage URL
    URL = "https://www.amazon.com/s?k=esp32&crid=15JP267RFG79X&sprefix=esp3%2Caps%2C168&ref=nb_sb_noss_2"

    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")

    # Fetch links as List of Tag Objects
    links = soup.find_all("a", attrs={'class': 'a-link-normal s-no-outline'})

    # Loop for extracting product details from each link
    for link in links[:5]:
        new_webpage = requests.get("https://www.amazon.com" + link.get('href'), headers=HEADERS)
        new_soup = BeautifulSoup(new_webpage.content, "lxml")
        product_info = extract_product_info(new_soup)

        if product_info['Availability'] == "In Stock":
            # Print product information
            print("\n".join([f"{key}: {value}" for key, value in product_info.items()]))
            print()
