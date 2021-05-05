from basket import Basket


def test_basket():
    basket = Basket('sample_catalogue.json', 'sample_offers_types.json', 'sample_offers.json')
    basket.update('Baked Beans', 1)
    assert basket.pricer() == {"sub-total": 0.99, "discount": 0.0, "total": 0.99}
    basket.update('Baked Beans', 1)
    assert basket.pricer() == {"sub-total": 1.98, "discount": 0.0, "total": 1.98}
    basket.update('Baked Beans', 1)
    assert basket.pricer() == {"sub-total": 2.97, "discount": 0.99, "total": 1.98}
    basket.update('Baked Beans', 1)
    assert basket.pricer() == {"sub-total": 3.96, "discount": 0.99, "total": 2.97}
    basket.update('Baked Beans', 2)
    assert basket.pricer() == {"sub-total": 5.94, "discount": 1.98, "total": 3.96}
    basket.update('Baked Beans', -2)
    basket.update('Biscuits')
    assert basket.pricer() == {"sub-total": 5.16, "discount": 0.99, "total": 4.17}
    basket.empty()
    assert basket.pricer() == {"sub-total": 0.0, "discount": 0.0, "total": 0.0}
    basket.update('Sardines', 1)
    assert basket.pricer() == {"sub-total": 1.89, "discount": 0.38, "total": 1.51}
