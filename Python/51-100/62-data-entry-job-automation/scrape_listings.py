from bs4 import BeautifulSoup
import requests, re


class ScrapeListings:
    """Scrapes all the listings from the url of zillow. Data includes: Address, Rent and link of the property."""

    def __init__(self, url, headers) -> None:

        self.zillow_website_response = requests.get(url=url, headers=headers)
        self.zillow_website_response.raise_for_status()

        # getting the html of the page
        self.zillow_webpage = self.zillow_website_response.text

        # creating soup object
        self.zillow_soup = BeautifulSoup(self.zillow_webpage, "html.parser")

    def get_listings_data(self) -> list:
        """Returns a dictionary containing the address, rent and link of the property."""

        # getting all the addresses
        addresses_tag = self.zillow_soup.find_all(
            name="address", class_="list-card-addr"
        )
        address_list = [address_tag.text for address_tag in addresses_tag]

        # getting all the links
        links_tag = self.zillow_soup.find_all(name="a", class_="list-card-link list-card-link-top-margin")
        link_list = [link.get('href') if "zillow.com" in link else f"https://zillow.com{link.get('href')}" for link in links_tag]

        # getting the rent and converting it into integer
        rent_tags = self.zillow_soup.find_all(name="div", class_="list-card-price")
        rent_regex = re.compile(r"\d,\d+")
        rent_list = [rent_tag.text for rent_tag in rent_tags]
        rent_list = [int(rent_regex.search(rent_tag.text).group().replace(",","")) for rent_tag in rent_tags]
        
        # creating a list of dictionaries containing the address, rent and link of the property
        zillow_listings_data = []
        for property in range(len(address_list)):
            zillow_listings_data.append({"address": address_list[property], "rent": rent_list[property], "link": link_list[property]})

        # print(zillow_listings_data)

        return zillow_listings_data
