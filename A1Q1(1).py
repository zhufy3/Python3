import sys

def power_modulo(m, k, n):
    # Base case
    if k == 0:
        return 1 % n
    elif k % 2 == 0:  # If k is even
        half_pow = power_modulo(m, k // 2, n)
        return (half_pow * half_pow) % n
    else:  # If k is odd
        half_pow = power_modulo(m, k // 2, n)
        return (half_pow * half_pow * m) % n

    # Read the number of lines

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    m, k, n = a[0], a[1], a[2]
    print(power_modulo(m, k, n))
