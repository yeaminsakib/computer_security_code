# Shared prime number and base (generator)
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a generator (g): "))

# Alice's private key
a_private = int(input("Enter Alice's private key: "))

# Bob's private key
b_private = int(input("Enter Bob's private key: "))

# Calculate Alice's public key
a_public = (g ** a_private) % p

# Calculate Bob's public key
b_public = (g ** b_private) % p

# Calculate the shared secret key for Alice
alice_shared_secret = (b_public ** a_private) % p

# Calculate the shared secret key for Bob
bob_shared_secret = (a_public ** b_private) % p

print("Alice's public key:", a_public)
print("Bob's public key:", b_public)
print("Shared secret key (Alice's perspective):", alice_shared_secret)
print("Shared secret key (Bob's perspective):", bob_shared_secret)
