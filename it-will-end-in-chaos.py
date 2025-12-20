#------------------------------------------------------------------------------
# Collect data and display the bifurcation diagram of the logistic map.
#------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
def _main():
# Define necessary parameters
m_start, m_end, m_step = 2.4, 4, 0.0001
n_transients = 400
n_data = 200
m_vals = np.arange(m_start, m_end, m_step)
x_data = find_attractors(m_vals, n_transients, n_data)
plot_attractors(m_vals, x_data)
def find_attractors(mVec, n_burn, n_keep):
"""Return array of logistic map attractors in range of scale parameter.
For each value of the scale parameter, m, in mvec repeat the update:
x = m*x*(1 - x)
starting from arbitrary x0 and discard the first n_burn values. Then
collect and save the next n_keep values. Return a 2d array X with stable
fixed points of the map. The i-th row of X holds the fixed points of
the i-th value of mvec.
"""
X = np.zeros((mVec.size,n_keep))
# Loop over all m values
for i, m in enumerate(mVec):
x = 0.5 # starting value (arbitrary, must be in [0,1])
# Burn-in loop to discard transient values
for _ in range(n_burn):
x = m * x * (1 - x)
# Collect steady-state data
for j in range(n_keep):
x = m * x * (1 - x)
X[i, j] = x
### THIS IS WHERE YOU COME IN, FILL X WITH THE CORRECT VALUES ###
### YOU WILL NEED TO LOOP OVER ALL VALUES IN mVec AND FOR EACH VALUE ###
### YOU WILL USE TWO ADDITIONAL LOOPS, ONE TO "BURN" THE TRANSIENTS ###
### AND ONE TO CREATE THE DATA TO KEEP. FOR EACH VALUE OF m SAVE THE ###
### DATA IN A COLUMN OF X.
return X
def plot_attractors(mVec,X):
"""Scatter rows of X value for each value in mVec."""
plt.figure(figsize=(8,6))
for k in range(mVec.size):
m = mVec[k]*np.ones(X.shape[1])
x = X[k,:]
plt.plot(m, x, 'k.', ms=0.02)
plt.xlabel('$m$', fontsize=14)
plt.ylabel('$x$', fontsize=14)
plt.show()
if __name__ == '__main__':
