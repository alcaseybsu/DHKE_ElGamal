import random

def ElGamalEncrypt(M, public_key, prime_q, primitive_root_alpha):
    k = random.randint(1, prime_q - 2)  # randomly select k
    c1 = pow(primitive_root_alpha, k, prime_q)
    c2 = (pow(public_key, k, prime_q) * M) % prime_q
    return c1, c2

def ElGamalDecrypt(c1, c2, private_key, prime_q):
    s = pow(c1, private_key, prime_q)
    M = (c2 * pow(s, prime_q - 2, prime_q)) % prime_q
    return M
