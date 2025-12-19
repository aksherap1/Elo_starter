#------------------------------------------------------------------------------
# This module defines legpoly(), a fast calculation of Legendre polynomials.
#------------------------------------------------------------------------------
def legpoly(n,x):
  
""""Return value at x of ordinary Legendre Polynomial or degree n.
This function implements the two-point recursion relation:
(k + 1)P_{k+1}(x) = (2k + 1)xP_k(x) - kP_{k-1}(x)
in a loop, without recursive calls to itself. This is the best way to
calculate values of Legendre polynomials of high degree.  

Parameters
----------
n : nonnegative integer scalar
Legendre polynomial degree
x : real scalar in [-1,1]
Legendre polynomial argument
Returns
-------
y : real scalar
Value of P_n at x
"""
# Verify valid input
assert (int(n) == n) and (n >= 0), "n must be nonnegative integer"
assert (x >= -1) and (x <= 1), "x must be in [-1,1]"

# Calculate P_n(x)
### THIS IS WHERE YOU COME IN
### USE AS MANY LINES AS YOU NEED
### USE A FOR LOOP OR WHILE LOOP, WHICHEVER YOU LIKE

y = None
if n == 0:
y=1.0
elif n == 1:
y=x
else:
previous = 1.0
current = x
for k in range (1, n):
next = ((2*k + 1)*x*current - k*previous) / (k+1)
previous, current, = current, next
y = current
###
return y

### Below are functions and statements we use to test
### your solution. 

def _test1():
print("Testing legpoly implementation.")
print()
x = 0.5
p0_true = 1.0
p1_true = x
p2_true = 0.5*(3*x**2 - 1)
p3_true = 0.5*(5*x**3 - 3*x)
p4_true = (1/8)*(35*x**4 - 30*x**2 + 3)
print(f"Calculated P_0({x}) = {legpoly(0,x)}")
print(f"Expected P_0({x}) = {p0_true}")
print()
print(f"Calculated P_1({x}) = {legpoly(1,x)}")
print(f"Expected P_1({x}) = {p1_true}")
print()
print(f"Calculated P_2({x}) = {legpoly(2,x)}")
print(f"Expected P_2({x}) = {p2_true}")
print()
print(f"Calculated P_3({x}) = {legpoly(3,x)}")
print(f"Expected P_3({x}) = {p3_true}")
print()
print(f"Calculated P_4({x}) = {legpoly(4,x)}")
print(f"Expected P_4({x}) = {p4_true}")
print()
print(f"Calculated P_3501({-1.0}) = {legpoly(3501,-1)}")
print(f"Expected P_3501({-1.0}) = -1.0")
if __name__ == '__main__':
print()
_test1()
print()
