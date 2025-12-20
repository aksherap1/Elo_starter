#------------------------------------------------------------------------------
# PHYSUNITS: Dimensionally aware variables and expressions
# This module implements the preal class and defines the basic type preal
# variables.
#------------------------------------------------------------------------------
import numpy as np
_nbdim = 6
_dim_labels = ['m', 'kg', 's', 'K', 'A', 'mol']
class preal:
### PREAL CONSTRUCTOR
### A RUDIMENTARY CONSTRUCTOR IS PROVIDED; YOU MAY MODIFY AS NEEDED
def __init__(self, value=np.nan, units=np.zeros(_nbdim)):
#checks if it has the right number of dimensions
units = np.array(units)
if units.shape[0] != _nbdim:
raise ValueError("Unit vector has incorrect length")
self.value = np.float64(value)
self.units = np.array(units)
### TYPE CAST DUNDERS
def __int__(self):
return int(self.value)
def __float__(self):
return float(self.value)
def __complex__(self):
return complex(self.value)
### DISPLAY DUNDERS
# IMPLEMENT __str__ TO CREATE AN EASY-TO-READ STRING REPRESENTATION OF A
# PREAL VARIABLE. YOU MAY CHOOSE TO IMPLEMENT __repr__ DIFFERENTLY OR
# LEAVE IT AS IS. YOU CAN READ ABOUT THE DIFFERENT ROLES OF __str__ AND
# __repr__ IN THE DOCUMENTATION IF/WHEN YOU HAVE TIME.
def __str__(self):
#removes any trailing zeros
valstr = f"{self.value:g}"
#stores numerator/denominator units
num_parts, den_parts = [], []
#looping through each exponent and its label
for exp, label in zip(self.units, _dim_labels):
#skips 0 exponents
if abs(exp) < 1e-12: continue
#handles positive exponents
if exp > 0:
num_parts.append(label if abs(exp-1)<1e-12 else f"{label}^{exp:g}")
else:
#handles negative exponents
den_parts.append(label if abs(-exp-1)<1e-12 else f"{label}^{-
exp:g}")
#if there are not units then dimensionless
if not num_parts and not den_parts:
units_str = "dimensionless"
elif den_parts and not num_parts:
units_str = "1 / " + "*".join(den_parts)
elif den_parts:
units_str = "*".join(num_parts) + " / " + "*".join(den_parts)
else:
units_str = "*".join(num_parts)
return f"{valstr} [{units_str}]"
def __repr__(self):
#converts number into a string
valstr = f"{self.value: .16g}"
return f"preal(value={valstr}, units={self.units})"
@staticmethod #does not need a self argument
#checks if x is a preal object and if yes then it will return as it is
#function makes it easy to not repeat these lines again and again for
arithmetic operations & ensure you always have a preal object to work with
def _to_preal(x):
if isinstance(x, preal):
return x
#if x is a real number, it will convert into preal
if isinstance(x, (int,float,np.floating,np.integer)):
return preal(x)
raise TypeError(f"Cannot convert type {type(x)} to preal")
### PREAL ARITHMETIC
# IMPLEMENT BELOW THE VARIOUS FUNCTIONS THAT WILL HANDLE OPERATIONS WITH
# PREAL VARIABLES. CONCRETELY, IF *EITHER* a OR b OR BOTH ARE OF TYPE PREAL
# YOU WILL NEED TO TELL PYTHON HOW TO HANDLE THE FOLLOWING EXPRESSIONS,
# SOME OF WHICH MAY ONLY APPLY TO DIMENSIONLESS PREALS:
#makes number negative
def __neg__(self):
return preal(-self.value, self.units)
#Addition
def __add__(self, other):
#converts other into preal object
otherp = preal._to_preal(other)
#checks if both objects have same units
if not np.allclose(self.units, otherp.units):
raise ValueError("Dimension mismatch!")
return preal(self.value + otherp.value, self.units)
#reverse add is same function as add
__radd__ = __add__
#Subtraction
def __sub__(self, other):
#converts other into preal object
otherp = preal._to_preal(other)
#checks if both objects have same units
if not np.allclose(self.units, otherp.units):
raise ValueError("Dimension mismatch, check your units!")
return preal(self.value - otherp.value, self.units)
#reverse subtraction
def __rsub__(self, other):
#converts other into preal object
otherp = preal._to_preal(other)
#checks if both objects have same units
if not np.allclose(self.units, otherp.units):
raise ValueError("Dimension mismatch, check your units!")
return preal(otherp.value - self.value, self.units)
#Multiplication
def __mul__(self, other):
#converts other into preal object
otherp = preal._to_preal(other)
return preal(self.value * otherp.value, self.units + otherp.units)
#reverse multiplication is same function as multiplication
__rmul__ = __mul__
#Division
def __truediv__(self, other):
#converts other into preal object
otherp = preal._to_preal(other)
return preal(self.value / otherp.value, self.units - otherp.units)
#reverse division
def __rtruediv__(self, other):
#converts other into preal object
otherp = preal._to_preal(other)
return preal(otherp.value / self.value, otherp.units - self.units)
#Powers
def __pow__(self, exponent):
if isinstance(exponent, preal):
if not np.allclose(exponent.units, 0):
raise ValueError("Exponent must be dimensionless")
expval = float(exponent.value)
else:
expval = float(exponent)
return preal(self.value ** expval, self.units * expval)
def __rpow__(self, base):
if not np.allclose(self.units, 0):
raise ValueError("Exponent must be dimensionless")
return preal(float(base) ** float(self.value), np.zeros(_nbdim))
def __eq__(self, other):
try: otherp = preal._to_preal(other)
except: return False
return np.allclose(self.units, otherp.units) and np.allclose(self.value,
otherp.value)
def _ensure_dimensionless(p):
#checks if p is a preal object
if isinstance(p, preal):
#checks if unit vector is all 0s & if units are not all 0s then input is
not dimensionless
if not np.allclose(p.units, 0): raise ValueError("Argument must be
dimensionless preal or numeric")
return float(p.value)
#if p is already a regular number then it is dimensionless
if isinstance(p, (int,float,np.floating,np.integer)):
return float(p)
#if something out than the type is passed it will produce an error
raise TypeError("Unsupported type")
### TRANSCENDENTAL FUNCTIONS OVERLOADED FOR PREAL
# IMPLEMENT THE FOLLOWING FUNCTIONS SO THEY WORK CORRECTLY FOR PREAL VARIABLES
# *AND* REGULAR NUMERIC VARIABLES
#cos,sin, & tan will convert p into dimensionless float, computes, and then wraps
back into preal object with 0 units
def cos(p):
return preal(np.cos(_ensure_dimensionless(p)), np.zeros(_nbdim))
def sin(p):
return preal(np.sin(_ensure_dimensionless(p)), np.zeros(_nbdim))
def tan(p):
return preal(np.tan(_ensure_dimensionless(p)), np.zeros(_nbdim))
def exp(p):
return preal(np.exp(_ensure_dimensionless(p)), np.zeros(_nbdim))
def log(p):
v = _ensure_dimensionless(p)
if v <= 0: raise ValueError("log domain error")
return preal(np.log(v), np.zeros(_nbdim))
def log10(p):
v = _ensure_dimensionless(p)
if v <= 0: raise ValueError("log10 domain error")
return preal(np.log10(v), np.zeros(_nbdim))
def sqrt(p):
p = preal._to_preal(p) # checks if it is a preal
new_units = p.units * 0.5 # sqrt
new_value = np.sqrt(p.value)
return preal(new_value, new_units)
### PREDEFINED INTERFACE VARIABLES ###
# Base units
meter = preal(1,[1,0,0,0,0,0])
kilogram = preal(1,[0,1,0,0,0,0])
second = preal(1,[0,0,1,0,0,0])
kelvin = preal(1,[0,0,0,1,0,0])
ampere = preal(1,[0,0,0,0,1,0])
mole = preal(1,[0,0,0,0,0,1])
radian = preal(1,[0,0,0,0,0,0])
# Abbreviations
m = meter
kg = kilogram
s = second
K = kelvin
A = ampere
mol = mole
rad = radian
# Derived units
N = kg*m/s**2
J = N*m
W = J/s
Pa = N/m**2
C = A*s
V = W/A
# -----------
# Test Cases
# -----------
if __name__ == "__main__":
import physunits_starter as u
g = 9.8*u.m/u.s**2
h = 5*u.m
m = 2*u.kg
U = m*g*h
v = 4*u.m/u.s
K = 0.5*m*v #error on purpose
try:
E = U + K # should give an error
except ValueError:
pass
K = 0.5*m*v**2 # fix the bug
E = U + K # should work
print(f"mechanical energy {E}")
# Addition & Subtraction
x1 = 2*u.m + 3*u.m # [m]
x2 = 10*u.kg - 4*u.kg # [kg]
print("x1 =", x1)
print("x2 =", x2)
# incompatible units so should give error
try:
_ = 2*u.m + 3*u.s
except ValueError as e:
print("Caught expected error (add incompatible units):", e)
# Multiplication & Division
F = 10*u.N
d = 2*u.m
W = F * d # Should be [J]
print("Work W =", W)
t = 2*u.s
v = d / t # Velocity [m/s]
a = v / t # Acceleration [m/s^2]
print("Velocity v =", v)
print("Acceleration a =", a)
# Powers
area = (3*u.m)**2 # [m^2]
volume = (2*u.m)**3 # [m^3]
dimensionless = (2*u.m/2*u.m)**3 # [dimensionless]
print("Area =", area)
print("Volume =", volume)
print("Dimensionless =", dimensionless)
# Exponent as preal (dimensionless)
x = (3*u.m)**u.preal(2) # works
print("x =", x)
# Exponent not dimensionless so gives error
try:
y = (3*u.m)**(2*u.m)
except ValueError as e:
print("Caught expected error (non-dimensionless exponent):", e)
# Transcendentals (dimensionless only)
theta = u.preal(np.pi/4) # dimensionless
print("sin(theta) =", u.sin(theta))
try:
u.sin(2*u.m) # error
except ValueError as e:
print("Caught expected error (sin of dimensioned quantity):", e)
#Square Root
length_squared = 9 * u.m**2
length = u.sqrt(length_squared)
print("sqrt(9 m^2) =", length)
velocity_squared = 16 * u.m**2 / u.s**2
velocity = u.sqrt(velocity_squared)
print("sqrt(16 m^2/s^2) =", velocity)
dimless_squared = u.preal(25)
dimless = u.sqrt(dimless_squared)
print("sqrt(25) =", dimless)
# Additional test: nested sqrt
nested = u.sqrt(u.sqrt(81*u.m**4))
print("sqrt(sqrt(81 m^4)) =", nested)
# Derived units
m = 2*u.kg
g = 9.8*u.m/u.s**2
F = m*g # Force [N]
print("Force F =", F)
v = 4*u.m/u.s
K = 0.5*m*v**2 # Kinetic energy [J]
print("Kinetic energy K =", K)
h = 5*u.m
U = m*g*h # Potential energy [J]
print("Potential energy U =", U)
E = K + U # Total mechanical energy [J]
print("Total mechanical energy E =", E)
# Combined expressions
density = 1000*u.kg/u.m**3
volume = 0.01*u.m**3
mass = density*volume # output kg
print("Mass =", mass)
pressure = 2*u.N/u.m**2 # output [Pa]
print("Pressure =", pressure)
voltage = 12*u.V
current = 2*u.A
power = voltage * current # output [W]
print("Power =", power)
# Albedo
albedo = u.preal(0.5)
print("albedo =", albedo)
x = albedo + 0.25
y = albedo * 2
print("x =", x)
print("y =", y)
