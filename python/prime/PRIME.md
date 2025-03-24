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
