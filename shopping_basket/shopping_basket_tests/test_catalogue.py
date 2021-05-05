from catalogue import Catalogue


def test_catalogue():
    catalogue = Catalogue("sample_catalogue.json")
    assert catalogue.get_base_price("Sardines") == 1.89
    assert catalogue.get_base_price("Tomatoes") == 0.0
