**bby** is a Python package for scraping product info from bestbuy.com.

## Installation

```
pip install git+https://github.com/jonxola/bby
```

## Usage

```python
import bby

url = 'https://www.bestbuy.com/site/macbook-air-13-3-laptop-apple-m1-chip-8gb-memory-256gb-ssd-latest-model-gold/6418599.p?skuId=6418599'

bby.get_product(url)
```
```python
{
    'url': 'https://www.bestbuy.com/site/macbook-air-13-3-laptop-apple-m1-chip-8gb-memory-256gb-ssd-latest-model-gold/6418599.p?skuId=6418599',
    'sku': '6418599',
    'name': 'MacBook Air 13.3" Laptop - Apple M1 chip - 8GB Memory - 256GB SSD (Latest Model) - Gold',
    'price': '$999.99',
    'available': True
}
```