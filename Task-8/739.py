import math
import fractions

a, b = map(int, input().split())
g = math.gcd(a, b)
lcm = a * b // g
print(lcm)
