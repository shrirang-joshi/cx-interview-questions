from catalogue import Catalogue
from offers import ProductOffers


class Basket:
    def __init__(self, catalogue_json_file: str, offer_types_json_file: str, product_offers_json_file: str):
        self.catalogue = Catalogue(catalogue_json_file)
        self.product_offers = ProductOffers(offer_types_json_file, product_offers_json_file)
        self.products = {}
        self.sub_total, self.discount, self.total = 0.0, 0.0, 0.0

    def update(self, product_name: str, count: int = 1):
        # First make sure that the product is in the catalogue
        if not self.catalogue.is_valid_product(product_name):
            raise Exception("Invalid Product")

        # Update the number of items
        if product_name not in self.products and count < 1:
            return

        self.products[product_name] = count + self.products.get(product_name, 0)
        if self.products[product_name] < 1:
            del self.products[product_name]

        # Now recalculate the basket price
        self.calculate_price()

    def calculate_price(self):
        sub_total = 0.0
        discount = 0.0
        for product, product_count in self.products.items():
            product_base_price = self.catalogue.get_base_price(product)
            sub_sub_total = product_count * product_base_price
            sub_discount = 0.0

            # check if there are any offers for this product
            offer = self.product_offers.get_offer_for_product(product)
            print(product, offer)
            if offer:
                if 'buy' in offer:
                    buy = offer['buy']
                    free = offer.get('free', 0)
                    total_offer_qty = buy + free
                    offer_count = product_count // total_offer_qty if product_count >= total_offer_qty else 0
                    discount += offer_count * free * product_base_price
                elif 'discount' in offer:
                    discount_pct = offer['discount']
                    sub_discount = discount_pct * sub_sub_total / 100

            sub_total += sub_sub_total
            discount += sub_discount

        self.sub_total = round(sub_total, 2)
        self.discount = round(discount, 2)
        self.total = round(sub_total - discount, 2)

    def empty(self):
        self.products = {}
        self.sub_total, self.discount, self.total = 0.0, 0.0, 0.0

    def pricer(self) -> dict:
        return {
            "sub-total": self.sub_total,
            "discount": self.discount,
            "total": self.total
        }
