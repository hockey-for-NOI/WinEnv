# Try python with primes

## Prime

- A prime `p` satisfy the following conditions:
	- `p % i != 0 (2 <= i <= p-1)`
	- `!=` means unequal, while `==` means equal
	- Remember to distinguish `=` (assignment) and `==` (comparison)

## Use IPython

- `ipython`

```
In [6]: import math

In [7]: math.floor(3.5)
Out[7]: 3

In [8]: type(math.floor(3.5))
Out[8]: int

In [9]: def check_prime(p):
   ...:     square_root = math.floor(p ** 0.5)
   ...:     for i in range(2, square_root + 1):
   ...:         if p % i == 0:
   ...:             return i
   ...:     return p
   ...:

In [10]: check_prime(3331)
Out[10]: 3331

In [11]: check_prime(3337)
Out[11]: 47
```

## Use Python script

- Download [`check_prime_script.py`](./check_prime_script.py)
- `python check_prime_script.py`

## Use IPython call Python script

- `ipython`

```
In [1]: from check_prime_script import check_prime

In [2]: check_prime(3331)
Out[2]: 3331

In [3]: check_prime(3337)
Out[3]: 47
```

## Expansion: Sieve method

- How to get all primes between 0..100 ?

```
In [1]: from check_prime_script import check_prime

In [2]: primes = []

In [3]: for i in range(2, 101):
   ...:     if check_prime(i) == i:
   ...:         primes.append(i)
   ...:

In [4]: print(primes)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

- You can implement these in a tighter version:
	- `primes = [i for i in range(2, 101) if check_prime(i) == i]`

- Time Complexity
	- `check_prime(p)`: `O(p ** 0.5)` or `O(sqrt(p))`, which `sqrt` is square root.
	- Overall: `O(n ** 1.5)` or `O(n * sqrt(n))`

- A faster version
	- Download [`sieve_prime_script.py`](./sieve_prime_script.py)
	- How to use python to execute this script?

- Some more info

```
In [1]: from sieve_prime_script import sieve_prime

In [2]: a, primes = sieve_prime(100000)

In [3]: primes[-10:]
Out[3]: [99877, 99881, 99901, 99907, 99923, 99929, 99961, 99971, 99989, 99991]

In [4]: def factor(x):
   ...:     factors = []
   ...:     while x > 1:
   ...:         factors.append(primes[a[x] - 1])
   ...:         x //= factors[-1]
   ...:     return factors
   ...:

In [5]: factor(25519)
Out[5]: [13, 13, 151]

In [6]: factor(35531)
Out[6]: [35531]

In [7]: factor(46542)
Out[7]: [2, 3, 7757]

In [8]: factor(53375)
Out[8]: [5, 5, 5, 7, 61]

In [9]: factor(65536)
Out[9]: [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
```
