from offers import ProductOffers


def test_offers():
    offers = ProductOffers("sample_offers_types.json", "sample_offers.json")
    assert offers.get_offer_for_product("Sardines") == {"discount": 20}
    assert offers.get_offer_for_product("Baked Beans") == {"buy": 2, "free": 1}
    assert offers.get_offer_for_product("Tomatoes") is None
