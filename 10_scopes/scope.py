
# closure 

def power(num):
    def actual(x):
        return x ** num
    return actual

result = power(3)

print(result(2))
