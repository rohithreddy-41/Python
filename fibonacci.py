n = int(input("Enter the number of Fibonacci numbers to generate: "))
a, b = 0, 1
print(a, b, end=", ")
for _ in range(n):
    c = a + b
    print(c, end=", ")
    a, b = b, c
print("Fibonacci sequence generated successfully.")
