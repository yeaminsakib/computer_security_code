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
    print("The value of n is :",n)

    e = int(input("Enter an integer for public key (e): "))
    

    while e < phi:
        if gcd(e, phi) == 1:
            break
        else:
            e = int(input("Public key (e) is not coprime with φ(n). Enter a different value for e: "))

    found_valid_d = False

    for k in range(11):  # This will iterate from 0 to 10 (inclusive)
        d = (1 + (k * phi)) // e

        if d % 1 == 0:  # Check if d is an integer
            print(f"For k = {k}, private key d is:", d)
            msg = int(input("Enter the message to be encrypted: "))
            found_valid_d = True
            break
        if not found_valid_d:
            print("No valid k value found.")

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