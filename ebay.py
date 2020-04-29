
# TODO
# 1. Make a request to the ebay.com and get a page
# 2. Collect data from each detail page
# 3. Collect all links to detail pages of each product
# 4. Write scraped data to a csv file

import requests
from bs4 import BeautifulSoup


def get_page(url):
    response = requests.get(url)

    if not response.ok:
        print('Server Responded: ', response.status_codes)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
        return soup


def main():
    url = "https://www.ebay.com/itm/New-Longines-Master-Collection-Automatic-40mm-White-Mens-Watch-L2-909-4-78-3/383525040495?hash=item594bdfb16f:g:vdIAAOSwytheqbKu"
    get_page(url)



if __name__ == '__main__':
    main()











