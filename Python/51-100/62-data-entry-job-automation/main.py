# Data Entry Job Automation using BeautifulSoup and Selenium

from scrape_listings import ScrapeListings
from data_entry import DataEntry


def main():
    """Main function"""

    # searches for atleast 1 bedroom, upto 3K rent in New York City
    ZILLOW_URL = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22usersSearchTerm%22%3A%22New+York%2C+NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.40265463281249%2C%22east%22%3A-73.55670736718749%2C%22south%22%3A40.427642315836174%2C%22north%22%3A40.966969231026304%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22savedSearchEnrollmentId%22%3A%22X1-SSxdkzqgx4sdzu0000000000_7j3qe%22%7D"

    # google form url for data entry
    FORM_URL = "https://forms.gle/1eWkh1jx6XzXJhj7A"
    
    
    # You can see your browser headers by going to this website: http://myhttpheader.com/
    # headers are provided to avoid captcha
    headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    }

    zillow_data = ScrapeListings(url=ZILLOW_URL, headers=headers)

    # getting a list of dictionaries containing the address, rent and link of the property 
    zillow_listings = zillow_data.get_listings_data()
    
    # data entry
    data_entry_automation = DataEntry(url=FORM_URL, headers=headers)
    data_entry_automation.submit_data(zillow_listings)


if __name__ == "__main__":
    main()
