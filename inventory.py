inventory=[
    ("Laptop",5,30000,00)
    ("Headphones",15,500.00)
    ("Mouse",50,150.00)
    ("Keyboard",20,200.00)
    ("Monitor",30,6500)
]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name,quantity,unit_price=item
    stock_value=quantity*unit_priceitem
