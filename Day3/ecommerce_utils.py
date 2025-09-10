def apply_discount(price,discount_percent):
    discount=price*(discount_percent/100)
    return price-discount

def add_gst(price,gst_percent=18):
    gst=price*(gst_percent/100)
    return price+gst

def generate_invoice(cart):
    for key in cart:
        print(key,': ',cart[key])
    print('SubTotal: ',sum(cart.values()))
    after_discount=apply_discount(sum(cart.values()),10)
    print('After 10% discount: ',after_discount)
    print('After 18% gst: ',add_gst(after_discount))
    print("Thank you for shopping with us!")

    