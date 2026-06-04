def restaurant_order(*items_price, **customer):
    print("Customer Name:", customer["name"])
    total = sum(items_price)
    delivery_charge = 100
    print("Order total:",total)
    print("Delivery Charge:",delivery_charge)
    print("Total Amount:",total + delivery_charge)
restaurant_order(250, 200, 100, name="Varun")