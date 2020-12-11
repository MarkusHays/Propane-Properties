# This is an example file of how to use the PropaneProps package

import propane_properties as pp

from propane_functions import single_density_calc, calc_density_heatmap

# Choose the density type (mass denisty | molar density)
dens_type = pp.DensType.mass_density

# Example 1: Single condition calculation
pressure = 400  # Pressure in [psia] units
temperature = 289.67  # + 459.67  # Temperature in [R] units - 60 + 459.67

[density, phase_type] = single_density_calc(pressure, temperature, dens_type)

# Example 2: Plot heatmap of densities for range of pres. and temp.
minimum_temperature = 259.67  # Units [R]
maximum_temperature = 859.67  # Units [R]
minimum_pressure = 0.0234  # Units [psia]
maximum_pressure = 1724.0  # Units [psia]
N = 500  # (Optional) Number of grids in plot. Default is 50 in none is given
calc_density_heatmap(
    minimum_pressure, maximum_pressure, minimum_temperature, maximum_temperature, N
)
