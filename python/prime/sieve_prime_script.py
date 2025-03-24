# coding: utf-8

import numpy as np

def sieve_prime(n):
	a = np.zeros(n + 1, dtype=int)
	primes = []

	for i in range(2, n + 1):
		if a[i] == 0:
			primes.append(i)
			a[i] = len(primes)
		
		for j in range(a[i]):
			prod = i * primes[j]
			if prod > n: break
			a[prod] = j + 1
	
	return a, primes

if __name__ == "__main__":
	_, primes = sieve_prime(100)
	print(primes)
