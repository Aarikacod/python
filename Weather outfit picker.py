temperature = int(input("temperature is ?"))
if temperature < 20:
   outfit = "jacket"
   print("it is so cold today")
   print("wear a", outfit)
else: 
    outfit = "t-shirt"
    print("wear a", outfit)


    print("it is a warm day today")
    

is_raining = input("is it raining today ? yes/no")


if is_raining == "yes":

    print("bring an umbrella!")


wind_speed = int(input("enter the wind speed in km/h:"))


if wind_speed > 30:

   needs_windbreaker = "yes"

   print("It is windy today.")

   print("Wear a windbreaker over your", outfit)

else:

   needs_windbreaker = "no"

   print("It is calm today.")

   print("No windbreaker needed over your", outfit)

# PART 7: Ask whether there are puddles on the ground

has_puddles = input("Are there puddles on the ground? (yes/no): ")

# PART 8: Decide between boots and sneakers

if has_puddles == "yes":

    shoes = "boots"

    print("The ground is wet.")

    print("Wear", shoes)

else:

    shoes = "sneakers"

    print("The ground is dry.")

    print("Wear", shoes)

# PART 9: This message always prints, no matter what was chosen above

print("")

print("Weather check complete!")

# PART 10: Print the final outfit summary

print("===== WEATHER OUTFIT PICKER =====")

print("Temperature:", temperature)

print("Outfit Chosen:", outfit)

print("Raining:", is_raining)

print("Windbreaker Needed:", needs_windbreaker)

print("Shoes Chosen:", shoes)

print("===================================")

