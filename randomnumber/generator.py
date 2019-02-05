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
