print("Activity day planner")
day = input("enter your day")
weather = input("enter your weather")
homework = input("enter your homework")
print("your plan")
if day in ("saturday, sunday"):
    print("weekend")
elif day == "monday":
    print("First day") 
elif day == "Friday":
    print("Last day of school")    
elif day in ("tuesday, wednesday, thursday "): 
    print("regular day off") 
else: print("day invalid")


if weather == "Sunny" and homework == "yes":
       print("Weather is sunny")


if weather == "Sunny" or weather == "Cloudy":
     print("Pack umbrela")
if not (homework ==" yes"):
      print("homework not done")
if weather == "Rainy"  and not (homework == "yes"):
     print("stay inside finish homework") 
elif weather == "Sunny" or homework == "Yes":
     print("enjoy")
else: 
     print("next")


print("Planner completed")


