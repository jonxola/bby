def get_sku(soup):
    tag = soup.find('div', class_='sku').find('span', class_='product-data-value')
    return tag.get_text().strip()

def get_name(soup):
    tag = soup.find('div', class_='sku-title')
    return tag.get_text()

def get_price(soup):
    tag = soup.find('div', class_='priceView-customer-price').find('span')
    return tag.get_text()

def get_availability(soup):
    cart_btn = soup.find('button', class_='add-to-cart-button')
    return cart_btn.get_text() == 'Add to Cart'