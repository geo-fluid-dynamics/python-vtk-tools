# python-vtk-tools
This was developed primarily for the purposes of visualizing 2D unsteady fluid dynamics and heat transfer simulations.

We use Python-VTK to convert VTK data to NumPy data, and visualizes 2D data with Matplotlib.

## Applications

### Convection-coupled phase-change
Naturally convecting water in a cavity is initially at steady state, with a hot boundary on the left, cold boundary on the right, and adiabatic top and bottom walls.
The cold wall temperature is dropped well below the freezing temperature, initiating freezing from right to left.

![Freezing water in a cavity](https://github.com/geo-fluid-dynamics/python-vtk-tools/blob/master/WaterFreezing.gif?raw=true)

The streamline thickness is proportional to the velocity. This is convenient for visualizing flow within the liquid part of phase-changing domains, where the velocity in the solid region is nearly zero. Our code can write the PNG images at each time step. We used a separate converter to generate a GIF.
