import bby

urls = [
    'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440',
    'https://www.bestbuy.com/site/macbook-air-13-3-laptop-apple-m1-chip-8gb-memory-256gb-ssd-latest-model-gold/6418599.p?skuId=6418599',
    'https://www.bestbuy.com/site/samsung-70-class-7-series-led-4k-uhd-smart-tizen-tv/6429416.p?skuId=6429416',
    'https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161'
]

for url in urls:
    product = bby.get_product(url)
    print(f'{product}\n')