def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

temp = input("Enter temperature (C/F): ")

if temp[-1].upper() == 'C':
    c = float(temp[:-1])
    print(f"{c}°C is equal to {celsius_to_fahrenheit(c)}°F")
elif temp[-1].upper() == 'F':
    f = float(temp[:-1])
    print(f"{f}°F is equal to {fahrenheit_to_celsius(f)}°C")
else:
    print("Invalid input")
