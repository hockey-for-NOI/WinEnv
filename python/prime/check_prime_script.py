# coding: utf-8

import math

def check_prime(p):
    square_root = math.floor(p ** 0.5)
    for i in range(2, square_root + 1):
        if p % i == 0:
            return i
    return p
    
if __name__ == "__main__":
	print("check_prime(3331) = ", check_prime(3331))
	print("check_prime(3337) = ", check_prime(3337))
