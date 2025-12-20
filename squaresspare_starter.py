# Visualize equimaterial zones on a rolled cylinder
import numpy as np
import matplotlib.pyplot as plt
def visualize_danger(n, R_new=3, saveas=''):
"""Use n line segments of equal product to visualize Paradox
of the Roll.
Parameters
----------
n : int scalar
Number of line segments to display.
R_new : scalar, optional, default: 3
Radius of roll when new, in units of r0, the cardboard
cylinder radius.
saveas : str, optional, default: empty
If not empty save figure to file
Returns
-------
None
"""
# Start with a new figure window
plt.close('all') # this helps get rid of old figures you
forgot to close
fh = plt.figure(figsize=(8,6)) # my favorite figure size
r0 = 1
# Generate radii and corresponding remaining product fractions
r = np.linspace(r0, R_new, 400)
el = _el_of_r(r, R_new)
# Plot the main curve
plt.plot(r, el, color='black', linewidth=2)
# Divide into n equal-length (equal-material) zones
els = np.linspace(0, 1, n+1)
rs = _r_of_el(els, R_new)
colors = plt.cm.plasma(np.linspace(0, 1, n))
for i in range(n):
plt.plot([rs[i], rs[i+1]], [els[i], els[i+1]],
color=colors[i], lw=3)
# vertical guide
plt.plot([rs[i+1], rs[i+1]], [0, els[i+1]], 'k:', lw=1)
# horizontal guide
plt.plot([r0, rs[i+1]], [els[i+1], els[i+1]], 'k:', lw=1)
# Axis limits and ticks
plt.xlim(r0, R_new)
plt.ylim(0, 1)
plt.xticks(np.arange(1.00, 3.01, 0.25)) # x-axis: 1.00 1.0 in
0.2 steps
# Stylize and annotate
plt.xlabel('Product visible, r/r', fontsize=14)
plt.grid(False)
# Format tick labels to show 2 decimals
plt.gca().xaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'
))
# Finally, show on screen and/or save to file
if saveas:
plt.savefig(saveas, dpi=300, bbox_inches='tight')
plt.show(block=True)
def _el_of_r(r, R_new):
"""Fraction of product remaining given visible roll radius."""
r0 = 1
return (r**2 - r0**2) / (R_new**2 - r0**2)
def _r_of_el(el, R_new):
"""Visible roll radius given fraction of remaining product."""
r0 = 1
return np.sqrt(el*(R_new**2 - r0**2) + r0**2)
# Run example
if __name__ == "__main__":
visualize_danger(5, R_new=3, saveas='roll_paradox.png')
