import time
import math

class Generator:
    def __init__(self, bits =None):
        if bits is None:
            self.seedling = int(round(time.time() * 1000))
            time.sleep(0.002)
            self.modulus = int(round(time.time() * 100))

    def seed(self):
        return self.seedling

    def modulus(self):
        return self.modulus

    def generate(self, bit=None):
        t = pow(self.seedling, self.modulus, bit)
        return t

def find_primes(): # used in generating public information
    # The primes here are not very large, but this is more for fun than implementation.
    # This is the Miller-Rabin primality test. At 40 rounds, we can be fairly certain the number a is prime.
    # if you are not convinced of this, I suggest something-searching or working out the probability yourself
    a = int(time.time())
    while pow(2, a - 1, a) != 1:
        while (a % 2) == 0:
            a = int(time.time())
        for i in range(1,50):
            if pow(i, a, a) != i:
                a = int(time.time())
                break
    return a