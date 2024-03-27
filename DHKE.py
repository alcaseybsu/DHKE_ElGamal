from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.backends import default_backend

# Diffie-Hellman algo typically creates a key of at least 2048 bits
def generate_dh_parameters(bits=2048):    
    parameters = dh.generate_parameters(generator=2, key_size=bits, backend=default_backend())
    return parameters

def DiffieHellmanKeyExchange():
    parameters = generate_dh_parameters()

    # Generate private keys for users A and B
    private_key_A = parameters.generate_private_key()
    private_key_B = parameters.generate_private_key()

    # Generate public keys for users A and B
    public_key_A = private_key_A.public_key()
    public_key_B = private_key_B.public_key()

    # Compute shared secrets
    shared_secret_A = private_key_A.exchange(public_key_B)
    shared_secret_B = private_key_B.exchange(public_key_A)

    # Verify the shared secrets match
    if shared_secret_A == shared_secret_B:
        print("Verification Successful: The shared secrets match.")
        # Print a hex of the hash of the shared secret
        print("Hash of Shared Secret:", shared_secret_A.hex())
    else:
        print("Verification Failed: The shared secrets do not match.")

DiffieHellmanKeyExchange()
