#Count Number of Zeroes

def count(n, zeroes):
    if(n == 0):
        return zeroes
    if(n % 10 == 0):
        zeroes += 1
    return count(n // 10, zeroes)

print(count(4080900, 0))
