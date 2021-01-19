# Propane-Properties

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![version](https://img.shields.io/badge/version-0.0.1-green.svg)]()

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


This program calculates the density of propane for both liquid and vapor phase using the
modified Benedict-Webb-Ruben EOS proposed by Starling in his book "Fluid Thermodynamic
Properties for Light Petroleum Systems".

The main features of the program at this point is:

1) A single density and phase type calculation at a given pressure (p) and temperature (T)
in the function called `single_density_calc()`

2) Calculate the density at a variaty of pressures and temperatures using the function called
`calc_density_heatmap()`


## Installation

1. Clone this repository

```
git clone https://github.com/MarkusHays/Propane-Properties.git
```

2. cd to the directory:

```
cd Propane-Properties
```

3. Run pip:

```
pip install -e .
```

You can now use `propane_propeties` anywhere on your machine by adding `import propane_properties`.

## Examples
Examples of the features can be found in "example_calculations.py" and show the main features of the code. To get a detailed (refined) plot set the "number of grids in plot" or `num_grid_poitns` to 500. However, this takes some time to generate with the existing code.

To define the density type (molar or mass density) use the `DensityType` class in the `propane_properties` package which can be imported as `pp`. An example is given below

```python
from propane_properties import DensType

# Choose the density type (mass denisty | molar density)
dens_type = DensType.mass_density
```

An example of the using `single_density_calc()` is given below

```python
from propane_properties import DensType, single_density_calc

# Choose the density type (mass denisty | molar density)
dens_type = DensType.mass_density

# Example 1: Single condition calculation
pressure = 400  # Pressure in [psia] units
temperature = 289.67  # + 459.67  # Temperature in [R] units - 60 + 459.67

[density, phase_type] = single_density_calc(pressure, temperature, dens_type)
```

An example of using `calc_density_heatmap()` is given below

```python
from propane_properties import DensType, calc_density_heatmap

# Choose the density type (mass denisty | molar density)
dens_type = DensType.mass_density

# Example 2: Plot heatmap of densities for range of pres. and temp.
minimum_temperature = 259.67  # Units [R]
maximum_temperature = 859.67  # Units [R]
minimum_pressure = 0.0234  # Units [psia]
maximum_pressure = 1724.0  # Units [psia]
num_grid_poitns = 500  # (Optional) Number of grids in plot. Default is 50 in none is given
calc_density_heatmap(
    minimum_pressure,
    maximum_pressure,
    minimum_temperature,
    maximum_temperature,
    num_grid_poitns
)
```

resulting in the figure below

![density-matrix](https://user-images.githubusercontent.com/31182250/104158808-695daa00-53ee-11eb-90be-ef69ffa4aab3.png)


**Figure 1**: Example result of using `calc_density_heatmap()` with `num_grid_poitns=500`.

These examples are also given in the "example_calculations.py" file.

## Making Contributions
If you want to use the code or make contributions, then this is great! If you are planning on contributing to the code
I prefer that you apply similar code structure to the current code and also follow the following conventions:

0) When making changes, **ALWAYS** make a new branch and remember to make short and concise comments in the commits etc.

1) Classes are in Pascal format e.g. `MyClass`.

2) Functions, variables and moduels are in snake format e.g. `my_function()` | `my_variable` | `my_module`.

3) Use type hints for all functions e.g. `my_function(my_var: float)` or `my_other_function(my_other_var: SomeClass)`

4) Use docstrings for all functions where there are two tiers of functions (see point 5). Tier 1 functions need three (or four) paragraphs
where the first paragraph describes the function in a single sentence, the second paragraph describes the input, (optional) the
third gives the relevant units and the fourth contains the output values or results. Tier 2 functions only have a single paragraph that
describes (short) what the functions do.

5) There are two tiers of functions where Tier 1 is a public function e.g. `my_function()` and Tier 2 is a hidden function e.g. `_my_hidden_function()`.
The aim of this is to move all the irelevant functions to the end of the IDE list of functions.

6) Function names should be very clear to avoid the need to add comments.

7) Comments in the code are okay, but should be kept to a minimum. If a lot of comments are needed, try to break up the code to several layers to
make it easier to understand. If there is some very complicated logic, please make some documentation (PDF file with texts).

These points will be considered before the contribution is merged to the main branch in a pull-request (PR).

## Contact
If you are interested in this code or how I solved it, please feel free to contact me [here](mailto:markushays@whitson.com) or via LinkedIn by searching for Markus Hays Nielsen.

## Theory - EOS Models
**This is coming in the future.**

Intro on EOS models in general (IGL, RGL, vdW, cubic, BWR and finally modified BWR), then specifics og solving the problem of this task.
