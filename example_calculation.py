# This is an example file of how to use the PropaneProps package

import propane_properties as pp

# Example 1: Single condition calculation
pressure = 400  # Pressure in [psia] units
temperature = 60 + 459.67  # Temperature in [R] units

# Choose the density type (mass denisty | molar density)
dens_type = pp.DensType.mass_density

density = pp.calculate_density(pressure, temperature, dens_type)
