import math

def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp

def get_user_input():
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))
    phi = (p - 1) * (q - 1)
    print("The value of phi is :",phi)
    n = p * q
    e = int(input("Enter an integer for public key (e): "))
    

    while e < phi:
        if gcd(e, phi) == 1:
            break
        else:
            e = int(input("Public key (e) is not coprime with φ(n). Enter a different value for e: "))

    k = 2
    d = (1 + (k * phi)) // e 
    print("private key d is :", d)
    msg = int(input("Enter the message to be encrypted: "))

    return n, e, d, msg

def encrypt(msg, e, n):
    c = pow(msg, e, n)
    return c

def decrypt(c, d, n):
    m = pow(c, d, n)
    return m

if __name__ == "__main__":
    n, e, d, msg = get_user_input()

    print("Message data = ", msg)

    c = encrypt(msg, e, n)
    print("Encrypted data = ", c)

    m = decrypt(c, d, n)
    print("Original Message Sent = ", m)
