import math

def gcd(a, h):
  """Calculates the greatest common divisor of two numbers."""
  temp = 0
  while(1):
    temp = a % h
    if (temp == 0):
      return h
    a = h
    h = temp

def egcd(a, b):
  """Calculates the extended greatest common divisor of two numbers."""
  x, y, r0, r1 = 1, 0, a, b
  while r1 != 0:
    q = r0 // r1
    x, y, r0, r1 = y, x - q * y, r1, r0 - q * r1
  return x, y, r0

def get_user_input():
  """Gets the user input for the RSA encryption algorithm."""
  p = int(input("Enter a prime number (p): "))
  q = int(input("Enter another prime number (q): "))
  phi = (p - 1) * (q - 1)
  print("The value of phi is :",phi)
  n = p * q
  print("The value of n is :",n)

  e = int(input("Enter an integer for public key (e): "))

  # Check if the public key is coprime with phi(n).
  while e < phi and gcd(e, phi) != 1:
    e = int(input("Public key (e) is not coprime with φ(n). Enter a different value for e: "))

  # Find a valid private key d using the Extended Euclidean Algorithm.
  x, y, r = egcd(e, phi)
  if r != 1:
    print("No valid private key found.")
    return None
  d = x % phi

  msg = int(input("Enter the message to be encrypted: "))
  if msg == "":
    print("Message cannot be empty.")
    return None

  return n, e, d, msg

def encrypt(msg, e, n):
  """Encrypts a message using the RSA encryption algorithm."""
  c = pow(msg, e, n)
  return c

def decrypt(c, d, n):
  """Decrypts a message using the RSA encryption algorithm."""
  m = pow(c, d, n) % phi
  return m

if __name__ == "__main__":
  n, e, d, msg = get_user_input()

  if n is None:
    exit()

  print("Message data = ", msg)

  c = encrypt(msg, e, n)
  print("Encrypted data = ", c)

  m = decrypt(c, d, n)
  print("Original Message Sent = ", m)
