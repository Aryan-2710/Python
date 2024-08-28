def gcd(a, b):
    while b != 0:
        a, b = b, a % b 
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)  

n1 = int(input("Enter 1st no. : "))
n2 = int(input("Enter 2nd no. : "))

gcd_ = gcd(n1, n2)
lcm_ = lcm(n1, n2)

print("GCD  is :",gcd_)
print("LCM  is :",lcm_)
