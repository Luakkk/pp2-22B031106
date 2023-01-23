price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))
quantity = 3

itemno = 567
price2 = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price2))