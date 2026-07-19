field1 = 120
field2 = 132
field3 = 110
field4 = 100
field5 = 90


total = field1 + field2 + field3 + field4 + field5
average = total / 5 
print ("total harvest", total)
print ("average", average )

price_perkg = 15
earning = total * 15
print ("total earnings", earning)

bags = total // 25
leftover = total % 25
print ("bags packed", leftover)
print ("leftover bags", )


last_year = 500
print ("Better than last year?:", total < last_year)
print ("Same as last year", total == last_year)


total+= 30
print ("total after bonus", total)


bags = total // 25
print ("final bags pack", bags)