import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from . import page
from .exceptions import InvalidUrlError

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'referer': 'https://www.bestbuy.com/',
}

def validate_url(url):
    '''Ensure that a URL points to bestbuy.com.'''
    hostname = urlparse(url).hostname
    bb = 'bestbuy.com' in hostname
    if not bb:
        raise InvalidUrlError('This is not a bestbuy.com URL.')

def get_product(url):
    '''Scrape product info from bestbuy.com
    
    Parameters:
    url (string): the URL to the product page on bestbuy.com

    Returns:
    A dictionary containing the product's info:
    url (string): the URL to the product page
    sku (string): the product's SKU
    name (string): the product's name as it appears on the page
    price (string): the product's price
    available (boolean): whether the product is in stock
    '''
    validate_url(url)
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    page.validate(soup)
    product = {
        'url': url,
        'sku': page.get_sku(soup),
        'name': page.get_name(soup),
        'price': page.get_price(soup),
        'available': page.get_availability(soup)
    }
    return product