#------------------------------------------------------------------------------
# A utility to fixes red-corrupted pixels in RGB images
#------------------------------------------------------------------------------
import sys
import numpy as np
from matplotlib.pyplot import imread, imsave
def pixelfix(I):
"""Replace bad pixels with color averaged from neighbors.
Parameters
----------
I : ndarray, M-by-N-by-3
A color image array to fix, in RGB format.
Returns
-------
I_new : ndarray, same shape as I
Copy of image with corrupt pixels fixed.
"""
I_new = I.copy()
nrows = I.shape[0] ### FINISH THIS LINE, HOW MANY ROWS?
ncols = I.shape[1] ### FINISH THIS LINE, HOW MANY COLUMNS?
badpx = [] # a log of bad pixels for diagnostic
for i in range(nrows):
for j in range(ncols):
if _iscorrupt(I,i,j):
badpx.append((i,j))
neighbors = _healthy_neighbors(I,i,j) # A list of index pairs
### FINISH THE NEW COLOR CALCULATION; IT MAY TAKE MORE THAN ONE
### LINE; IT MAY TAKE A LOOP, OR A LISTCOPM; DO WHATEVER IT
### TAKES
if len(neighbors) > 0:
colors = np.array([I[r, c, :] for (r, c) in neighbors])
new_r, new_g, new_b = colors.mean(axis=0)
else:
new_r = I[i,j,0]
new_g = I[i,j,1]
new_b = I[i,j,2]
###
###
new_color = np.array([new_r, new_g, new_b])
I_new[i,j,:] = new_color
print(f"Found and fixed {len(badpx)} bad pixels.")
return I_new
def _iscorrupt(I, i, j):
"""Return True if pixel is red-corrupted, else False."""
r, g, b = I[i, j, :]
return (abs(r - 1.0) < 0.01) and (abs(g) < 0.01) and (abs(b) < 0.01) ### FINISH
THIS FUNCTION
def _healthy_neighbors(I,i,j):
"""Return list of healthy neighbors of pixel (i,j) in image I."""
### MAKE A LIST OF HEALTHY NEIGHBORS
### A NEIGHBOR IS A TUPLE OF TWO INTS, ROW AND COL
### MOST PIXELS HAVE FOUR HEALTHY NEIGHBORS: UP, DOWN, LEFT, RIGHT
### IN WHICH CASE THE LIST OFFERED BELOW WILL WORK FINE
### BUT SOME PIXELS ARE MISSING ONE OR TWO OF THEIR NEGIHBORS
### FURTHERMORE, SOME NEIGHBORS MAY BE CORRUPTED PIXELS
### YOUR JOB IS TO MAKE A LIST INCLUDING ONLY NEIGHBORS THAT
### A) EXIST
### AND
### B) ARE NOT CORRUPTED
### THIS MAKE TAKE MORE THAN ONE LINE
nrows, ncols = I.shape[:2]
candidates = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
goodnbs = []
for (r, c) in candidates:
if (0 <= r < nrows) and (0 <= c < ncols):
if not _iscorrupt(I, r, c):
goodnbs.append((r, c))
return goodnbs
### Your work is finished. Below are functions and statements we use to test
### your solution. Feel free to look, but know that if you make any changes
### here they will just be overwritten by our grader. The assignment
### description explains how the submitted script will be called and what the
### expected results should be. That is all you need to know.
def _main():
image_file = sys.argv[1]
I = imread(image_file)
I = pixelfix(I)
imsave('fixed_' + image_file, I)
if __name__ == '__main__':
_main()
