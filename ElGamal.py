from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.backends import default_backend
import random

def generate_elgamal_parameters(bits=2048):
    # Using DH for params, since there's no library I could find 
    # that directly implements ElGamal encryption
    parameters = dh.generate_parameters(generator=2, key_size=bits, backend=default_backend())
    p = parameters.parameter_numbers().p
    g = parameters.parameter_numbers().g
    return p, g

def ElGamalEncrypt(M, public_key, prime_q, primitive_root_alpha):
    k = random.SystemRandom().randint(1, prime_q - 2)  
    c1 = pow(primitive_root_alpha, k, prime_q)
    c2 = (pow(public_key, k, prime_q) * M) % prime_q
    return c1, c2

def ElGamalDecrypt(c1, c2, private_key, prime_q):
    s = pow(c1, private_key, prime_q)
    M = (c2 * pow(s, prime_q - 2, prime_q)) % prime_q
    return M

if __name__ == "__main__":
    prime_q, primitive_root_alpha = generate_elgamal_parameters()
    # Simulation of ElGamal public/private key generation
    private_key = random.SystemRandom().randint(1, prime_q - 2)
    public_key = pow(primitive_root_alpha, private_key, prime_q)

    M = 1337  # Message to encrypt, change as needed
    
    c1, c2 = ElGamalEncrypt(M, public_key, prime_q, primitive_root_alpha)
    print(f"Encrypted message (c1, c2): {c1}, {c2}")
    
    decrypted_M = ElGamalDecrypt(c1, c2, private_key, prime_q)
    print(f"\nDecrypted Message: {decrypted_M}\n")
