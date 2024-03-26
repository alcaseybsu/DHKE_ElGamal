import random

def DiffieHellmanKeyExchange(prime_q, primitive_root_alpha):
    # Randomly generate private keys for users A and B
    private_key_A = random.randint(1, prime_q - 1)
    private_key_B = random.randint(1, prime_q - 1)

    # Compute public keys for users A and B
    public_key_A = pow(primitive_root_alpha, private_key_A, prime_q)
    public_key_B = pow(primitive_root_alpha, private_key_B, prime_q)

    # Print public keys
    print("Public Key of User A:", public_key_A)
    print("Public Key of User B:", public_key_B)

    # Compute the shared secret for both users
    shared_secret_A = pow(public_key_B, private_key_A, prime_q)
    shared_secret_B = pow(public_key_A, private_key_B, prime_q)

    # Print the shared secrets (should be the same)
    print("Shared Secret for User A:", shared_secret_A)
    print("Shared Secret for User B:", shared_secret_B)


