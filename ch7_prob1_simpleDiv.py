# Chapter 7, Problem 1 — Integer Division by Repeated Subtraction

def simpleDiv(dividend, divisor):
    count = 0
    while dividend >= divisor:
        dividend = dividend - divisor
        count = count + 1
    return count

def main():
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
    result = simpleDiv(dividend, divisor)
    print(dividend, "//", divisor, "=", result)

main()
