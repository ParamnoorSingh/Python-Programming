# WAP to covert temperature to and from celcius to farenheit

def convert_temperature(temp, scale):
    if scale.lower() == 'c':
        return (temp * (9/5))+32
    elif scale.lower() == 'f':
        return (temp-32)*(5/9)
    else:
        return "Invalid scale"
    
temperature = float(input("Enter the temperature: "))
scale = input("Enter the scale (c for celcius, f for farenheit): ")
converted = convert_temperature(temperature, scale)
if scale.lower() == 'c':
    print(f"{temperature} celcius is equal to {converted} farenheit")
elif scale.lower() == 'f':
    print(f"{temperature} farenheit is equal to {converted} celcius")
else:
    print(converted)