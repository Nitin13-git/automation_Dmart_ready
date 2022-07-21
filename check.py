def converstion(quantity, price):
    price=float(price)
    try:
        num_weight=float(quantity.split()[0])
    except:
        try:
            mul=float(quantity.split()[0][0])
            num_weight=float(quantity.split()[0][2:])*mul
        except:
            mul=float(quantity.split()[0][0])
            num_weight=float(quantity.split()[0][3:])*mul

    try:
        unit=quantity.split()[1]
    except:
        unit="gms"
    try:
        if unit == "gms":
            price_1_gram = price/num_weight
            price = price_1_gram*1000
            quantity = 1
            return price,quantity
    # return price,quantity

        elif unit == "Kg" or "Kgs":
            price = price/num_weight
            quantity = 1

            return price,quantity
        elif unit == "ml":
            price_1_gram = price/num_weight
            price = price_1_gram*1000
            quantity = 1
            return price,quantity

        elif unit == "Litre":

            price = price/num_weight
            quantity = 1
            return price,quantity

        else:
            quantity = quantity
            price = price
            return price,quantity
    except:
        print(0)
