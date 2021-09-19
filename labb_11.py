first_name=str(input("Please enter your first name: "))
last_name=str(input("Please enter your last name: "))
print (f"{first_name} {last_name}")

print(" Welcome " + first_name +" " + last_name)

print("Now let's get started, you've been selected to try my calculator.\nFor you this is a privilege" )
print("You will get 2 options. select 1")




option_1=(input("This is option 1, select this if you only want to calculate the area of a square"))
option_2= (input("This is option 2, select this if you wanna calculate the area and volume"))



if option_1>option_2:
    print(str(input(" Great you chose option 1")))
else:
    print(str(input("Great you chose option 2")))


