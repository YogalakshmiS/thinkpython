'''Exercise 7.5. The mathematician Srinivasa Ramanujan found an infinite series that can be used to
generate a numerical approximation of 1/π:
1
π
=
2
√
2
9801
∞
∑
k=0
(4k)!(1103 + 26390k)
(k!)
43964k
70 Chapter 7. Iteration
Write a function called estimate_pi that uses this formula to compute and return an estimate of
π. It should use a while loop to compute terms of the summation until the last term is smaller than
1e-15 (which is Python notation for 10−15). You can check the result by comparing it to math.pi.'''  


import math


def fact(s):
    if s == 0:
        return 1
    else:
        next_val = fact(s-1)
        res = s * next_val
        return res


def estimate():
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = fact(4*k) * (1103 + 26390*k)
        den = fact(k)**4 * 396**(4*k)
        x = factor * num / den
        total += x
        if abs(x) < 1e-15:
            break
        k += 1

    return 1 / total


print(estimate())
