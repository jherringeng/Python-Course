total = raw_input('What is the total amount for your online shopping?')
country = raw_input('Shipping within the US or Canada?')

if country == "US":

    if total <= 50:print ("Shipping Costs $6.00")
    elif total <= 100:print ("Shipping Costs $9.00")
    elif total <= 150:print ("Shipping Costs $12.00")
    else:print ("FREE")

elif country == "Canada":
    if total <= 50:print ("Shipping Costs $8.00")
    elif total <= 100:print ("Shipping Costs $12.00")
    elif total <= 150:print ("Shipping Costs $15.00")
    else:print ("FREE")

else:
    print('We don\'t supply to that country.')
