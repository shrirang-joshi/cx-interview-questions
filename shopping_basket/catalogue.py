import json


class Catalogue:
    def __init__(self, catalogue_json_file: str):
        self.products = self.__load(catalogue_json_file)
        print(self.products)

    @staticmethod
    def __load(json_filename) -> dict:
        with open(json_filename, "rt") as fp:
            return json.load(fp)

    def is_valid_product(self, product_name: str) -> bool:
        return product_name in self.products

    def get_base_price(self, product_name: str) -> float:
        return self.products.get(product_name, 0.0)
