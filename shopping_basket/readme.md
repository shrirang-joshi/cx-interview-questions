## Documentation

Catalogue and offers is maintained by other teams.
So for the purpose of this assignment,
the interface to catalogue and offers are assumed to be
json file as described below.

###Catalogue
The json file has product name as key and non discounted price.
e.g.:
```
{
  "Baked Beans": 0.99,
  "Biscuits": 1.20
}
```

###Offer Types
This json file contains types of offers the supermarket gives.
The key is offer code and value is a dictionary containing details
of the offer.
e.g.:
```
{
  "B1G1F": { "buy": 1, "free": 1},
  "B2G1F": { "buy": 2, "free": 1},
  "20PCT": { "discount": 20}
}
```

###Product Offers
This json maps the offers to products.
e.g.:
```
{
  "Baked Beans": "B2G1F",
  "Sardines": "20PCT"
}
```

##Basket Interface
The class ```Basket``` provides the interface to the pricer.
The class is instantiated by providing paths to the three json files:
```catalogue_json_file```, ```offer_types_json_file``` and ```product_offers_json_file```

###Products can be added to or removed from basket using the ```update``` method as follows:
```
basket.update(product_name: str, count: int = 1)
```
- ```product_name``` : Name of the product from catalogue
- ```count``` : count of products to be added to basket.
  The negative value will reduce the product number in the basket by count
  If the count in the basket for the product goes to less than 1,
  then the product is removed from the basket.
  
###The Basket can be emptied using the ```empty``` method:
```
basket.empty()
```
  
###The ```pricer``` method:
```
basket.pricer()
```
The pricer method return the discount and totals for the basket.
This is returned as a json object. e.g.:
```
{
    "sub-total": 1.89,
    "discount": 0.38,
    "total": 1.51
}
```
