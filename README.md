# Propane-Properties
This program calculates the density of propane for both liquid and vapor phase using the 
modified Benedict-Webb-Ruben EOS proposed by Starling in his book "Fluid Thermodynamic 
Properties for Light Petroleum Systems". 

The main features of the program at this point is: 

1) A single density and phase type calculation at a given pressure (p) and temperature (T) 
in the function called `single_density_calc()`

2) Calculate the density at a variaty of pressures and temperatures using the function called 
`calc_density_heatmap()`

## Examples
Examples of the features can be found in "example_calculations.py" and show the main features of the code. To get a detailed (refined) plot set the "number of grids in plot" or `N` to 500. However, this takes some time to generate with the existing code. 

![density-matrix](https://user-images.githubusercontent.com/31182250/104158808-695daa00-53ee-11eb-90be-ef69ffa4aab3.png)


**Figure 1**: Example result of using `calc_density_heatmap()` with `N=500`.

## Making Contributions
If you want to use the code or make contributions, then this is great! If you are planning on contributing to the code 
I prefer that you apply similar code structure to the current code and also follow the following conventions:

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
