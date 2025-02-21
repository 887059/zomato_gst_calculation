print("Welcome Zomato")
print("menu list")
print("1.dosa")
print("2.poori")
print("3.idly")
print("4.pongal")
dosa=30
poori=40
idly=10
pongal=30
Quantity=2
print("dosa*quantity")


you_want=input("what you want:")
your_order = int(input("quantity of the food:"))
gst_rate = 6
original_price=poori*2
gst_price = poori * 6 / 100
net_price = your_order + gst_price+Quantity+original_price
print(f"GST applied rs: {gst_price} at GST rate {gst_rate}%")
print(f"Total cost of the product after applying GST = {net_price}")