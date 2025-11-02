
word1 = "12345"
word2 = "abc"  
def find_gcd(a, b):
        while a != 0:
            a, b = b % a, a
        return b

print(f"output: {find_gcd(14,2)}")