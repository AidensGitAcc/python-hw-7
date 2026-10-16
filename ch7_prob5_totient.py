# Chapter 7, Problem 5 — Euler's Totient Function
# gcd()  — Euclidean algorithm (textbook p. 232)
# phi(n) — returns a list of integers 1..n-1 that are coprime to n

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def phi(n):
    coprimes = []
    for k in range(1, n):
        if gcd(n, k) == 1:
            coprimes.append(k)
    return coprimes

def main():
    n = int(input("Enter a positive integer n: "))
    result = phi(n)
    print()
    print("Integers from 1 to", n - 1, "that are relatively prime to", n, ":")
    print(result)
    print()
    print("phi(", n, ") =", len(result))

main()
