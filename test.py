import bby

urls = [
    # in stock product
    'https://www.bestbuy.com/site/apple-earpods-with-lightning-connector-white/5577816.p?skuId=5577816',
    # out of stock product
    'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440',
    # page on bestbuy.com that isn't a product page
    'https://www.bestbuy.com/site/electronics/computers-pcs/abcat0500000.c?id=abcat0500000',
    # other website
    'https://www.target.com/p/pepperidge-farm-goldfish-cheddar-crackers-6-6oz/-/A-13005401'
]

for url in urls:
    print()
    try:
        product = bby.get_product(url)
    except bby.exceptions.PageError as e:
        print(e)
    else:
        print(product)