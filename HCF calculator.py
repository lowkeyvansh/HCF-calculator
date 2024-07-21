def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

print(hcf(60, 48))
