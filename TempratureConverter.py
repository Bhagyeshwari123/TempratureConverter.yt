temp = float(input("Enter the temprature: "))
print("select a unit of choice from the list given below: ")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")

unit = int(input("Enter your choice: "))

if unit == 1:
    celsius = temp
    fahrenheit = (temp * 9/5) + 32
    kelvin = temp + 273.15
    print("temprature in celsius is:", celsius)
    print("temprature in fahrenheit is:", fahrenheit)
    print("tempratre in kelvin is:", kelvin)
elif unit == 2:
    fahrenheit = temp
    celsius = (temp - 32) * 5/9
    kelvin = celsius + 273.15
    print("temprature in fahrenheit is:", temp)
    print("temprature in celsius is:", celsius)
    print("temprature in kelvin is:", kelvin)
elif unit == 3:
    kelvin = temp
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print("temprature in kelvin is:", temp)
    print("temprature in celsius is:", celsius)
    print("temprature in fahrenheit is:", fahrenheit)
else:
    print("You have enter the wrong choice.")
