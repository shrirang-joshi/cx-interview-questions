import json


class ProductOffers:
    def __init__(self, offer_types_json_file: str, product_offers_json_file: str):
        self.product_offers = self.__load(offer_types_json_file, product_offers_json_file)
        print(self.product_offers)

    @staticmethod
    def __load(offer_types_json_filename: str, product_offers_json_file: str) -> dict:
        with open(offer_types_json_filename, "rt") as fp:
            offer_types = json.load(fp)
        with open(product_offers_json_file, "rt") as fp:
            product_offers = json.load(fp)
        return {p: offer_types[o] for p, o in product_offers.items() if o in offer_types}

    def get_offer_for_product(self, product_name: str) -> dict:
        return self.product_offers.get(product_name, None)
