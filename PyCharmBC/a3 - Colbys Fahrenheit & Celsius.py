# Created by Colby Boen-Padilla
# 2/1/23

# requesting either fahrenheit or celsius
strFC = input("Do you desire to print fahrenheit to celsius, if so type fc, otherwise, type cf for celsius to fahrenheit: ")

# if statement used for fahrenheit to celsius
if strFC == "fc": # checking for which conversion
    fahrenheit = input("Enter the fahrenheit: ") # asking for fahrenheit
    fahrenheit = int(fahrenheit) # converting the string fahrenheit to integer
    print((fahrenheit - 32) * (5/9)) # formula for fahrenheit to celsius
    print("is your celsius")

# else if statement used for celsius to fahrenheit
elif strFC == "cf": # checking for which conversion
    celsius = input("Enter the celsius: ") # asking for celsius
    celsius = int (celsius) # converting the string celsius to integer
    print(celsius * (9/5) + 32) # formula for celsius to fahrenheit
    print("is your fahrenheit")

# Bonus string format
elif strFC == "fcStrForm":
    FaCe = """{celsius} is your celsius converted from fahrenheit!"""
    fahrenheit = input("Enter the fahrenheit: ")  # asking for fahrenheit
    fahrenheit = int(fahrenheit)  # converting the string fahrenheit to integer
    print(FaCe.format(celsius=(fahrenheit - 32) * (5/9))) # The magic math

# Bonus string format
elif strFC == "cfStrForm":
    CeFa = """{fahrenheit} is your fahrenheit converted from celsius"""
    celsius = input("Enter the celsius: ")  # asking for celsius
    celsius = int(celsius)  # converting the string celsius to integer
    print(CeFa.format(fahrenheit=celsius * (9/5) + 32)) # The magic math

# for not valid inputs
else:
    print("not valid")