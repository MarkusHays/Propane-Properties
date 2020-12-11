from enum import Enum
from data import get_interp_functions, get_vap_interp
from math import exp
from scipy.optimize import root_scalar


class DensType(Enum):
    molar_density = "Molar Density"  # 1 / molar volume = moles / volume
    mass_density = "Mass Density"  # mass / volume


def calculate_density(p: float, T: float, dens_type: DensType):
    """
    Some text

    Some more text

    Final part of text
    """
    dens_type = dens_type.value  # Make to a string for clearity in code

    # Check if temperature and pressure is within the range (TODO)

    # Predict phase type (Liquid | Vapor)
    fluid_phase_type = find_fluid_phase(p, T)

    # Find density bound
    [dens_upper, dens_lower] = _get_density_bounds(fluid_phase_type, T)

    # Solve for the density (molar density)
    density = _solve_density_root(fluid_phase_type, p, T, dens_lower, dens_upper)

    if dens_type == "Mass Density":
        density = molar_dens_2_mass_dens(density)

    return density, fluid_phase_type


def molar_dens_2_mass_dens(density: float):
    return density * (44.062 / 0.062428)


def find_fluid_phase(p: float, T: float):
    """
    Some text

    Some more text

    Final text part
    """
    vap_pres = calc_vapor_pressure(T)

    if vap_pres > p:
        fluid_phase_type = "Vapor"
    elif vap_pres < p:
        fluid_phase_type = "Liquid"
    else:
        # TODO Raise exception that the fluid is on the vapor pressure curve
        _are_conditions_in_range(p, T)
        fluid_phase_type = _find_fluid_phase(T, p)

    return fluid_phase_type


def calc_vapor_pressure(T):
    """
    Some text

    Some more text

    Final text part
    """
    # Check if T in vapor pressure curve or pseudo-vapor pressure curve (T < Tc or T > Tc)
    vap_pres_function = get_vap_interp()
    vap_pres = vap_pres_function(T)
    return vap_pres


def propane_bwr(dens: float, T: float):
    # The units are in [ft], [lb], [R] and [lb-mole]
    R = 10.7335  # In units ft3.psia/R.lb-mole

    A0 = 18634.7
    B0 = 0.954762
    C0 = 7961780000
    D0 = 453708000000
    E0 = 25605300000000
    a = 40066.4
    b = 5.46248
    c = 27446100000
    d = 15052000
    alpha = 2.01402
    g = 4.56182

    p1 = R * T * dens
    p2 = (B0 * R * T - A0 - C0 / (T ** 2) + D0 / (T ** 3) - E0 / (T ** 4)) * dens ** 2
    p3 = (b * R * T - a - d / T) * dens ** 3
    p4 = alpha * (a + d / T) * dens ** 6
    p5 = (c / (T ** 2)) * dens ** 3 * (1 + g * dens ** 2) * exp(-g * dens ** 2)

    p = p1 + p2 + p3 + p4 + p5

    return p


# ==========================================================
# Sub-functions below used in the main functions above
# ==========================================================


def _find_fluid_phase(T: float, p: float):
    check = 0
    while check == 0:
        print("\n(1) Liquid\n(2) Vapor")
        fluid_phase_input = input(
            "Please provide fluid phase (the fluid is at vapor pressure line): "
        )
        fluid_phase_input = fluid_phase_input.strip().lower()

        try:
            if int(fluid_phase_input) == 1:
                check = 1
                fluid_phase_type = "Liquid"
            elif int(fluid_phase_input) == 2:
                check = 1
                fluid_phase_type = "Vapor"
        except:
            if fluid_phase_input == "vapor":
                check = 1
                fluid_phase_type = "Vapor"
            elif fluid_phase_input == "liquid":
                check = 1
                fluid_phase_type = "Liquid"
        if check == 0:
            print("\n#################################################")
            print("The input was not correct, please input again!")
            print("#################################################")
    return fluid_phase_type


def _are_conditions_in_range(p, T):
    Tmin = -200 + 459.67  # degrees Rankine
    Tmax = 400 + 459.67  # degrees Rankine
    pmax = 10000  # psia

    if (T >= Tmin and T <= Tmax) and (p <= pmax):
        pass
    else:
        # Raise exception
        print("#######################################################################")
        print("#######################################################################")
        print("###  The input conditions are outside the conditions of this model  ###")
        print("#######################################################################")
        print("#######################################################################")
        exit()
        pass


def _get_density_bounds(fluid_phase_type, T):
    [
        dens_upper_vapor,
        dens_lower_vapor,
        dens_upper_liquid,
        dens_lower_liquid,
    ] = get_interp_functions()
    if fluid_phase_type == "Liquid":
        upper_bound = dens_upper_liquid(T)
        lower_bound = dens_lower_liquid(T)
    else:
        upper_bound = dens_upper_vapor(T)
        lower_bound = dens_lower_vapor(T)

    return upper_bound, lower_bound


def _solve_density_root(
    fluid_phase_type: str, p: float, T: float, dens_lower: float, dens_upper: float
):
    if fluid_phase_type == "Liquid":
        initial_density = dens_upper
        dx = -0.0001
    else:
        initial_density = dens_lower
        dx = 0.0000001
    diff_lower = _difference(dens_lower, T, p)
    diff_upper = _difference(dens_upper, T, p)
    cnt = 0
    while (diff_lower * diff_upper > 0) and cnt < 100000:
        if diff_lower < 0:
            dens_upper *= 0.99
        else:
            dens_lower *= 1.01
        diff_lower = _difference(dens_lower, T, p)
        diff_upper = _difference(dens_upper, T, p)
        cnt += 1
    if cnt == 100000:
        test = 1
        pass

    results = root_scalar(
        _difference,
        x0=initial_density,
        args=(T, p),
        bracket=(dens_lower, dens_upper),
    )

    # results = root_scalar(
    #    _difference,
    #    x0=initial_density,
    #    x1=initial_density + dx,
    #    method="secant",
    #    args=(T, p),
    #    bracket=(dens_lower, dens_upper),
    # )
    density = results.root
    return density


def _difference(density: float, *args):
    T = args[0]
    p = args[1]
    p_bwr = propane_bwr(density, T)
    difference = p - p_bwr
    return difference


def _liquid_upper_limit(T):
    a0 = 2.883919e-2
    a1 = 1.237724e-2
    a2 = -5.929265e-5
    a3 = 1.272258e-7
    a4 = -1.292991e-10
    a5 = 4.946095e-14
    molar_density = a0 + a1 * T + a2 * T ** 2 + a3 * T ** 3 + a4 * T ** 4 + a5 * T ** 5
    return molar_density


def _liquid_lower_limit(T):
    a0 = 3.590758
    a1 = -3.138352e-2
    a2 = 1.508490e-4
    a3 = -3.675026e-7
    a4 = 4.428079e-10
    a5 = -2.116798e-13
    molar_density = a0 + a1 * T + a2 * T ** 2 + a3 * T ** 3 + a4 * T ** 4 + a5 * T ** 5
    return molar_density


def _vapor_upper_limit(T):
    a0 = -1.539523
    a1 = 1.985460e-2
    a2 = -1.003009e-4
    a3 = 2.485524e-7
    a4 = -3.032984e-10
    a5 = 1.469470e-13
    molar_density = a0 + a1 * T + a2 * T ** 2 + a3 * T ** 3 + a4 * T ** 4 + a5 * T ** 5
    return molar_density


def _vapor_lower_limit(T):
    a0 = 2.809999e-5
    a1 = -1.451954e-7
    a2 = 3.857916e-10
    a3 = -5.570498e-13
    a4 = 4.154120e-16
    a5 = -1.253100e-19
    molar_density = a0 + a1 * T + a2 * T ** 2 + a3 * T ** 3 + a4 * T ** 4 + a5 * T ** 5
    return molar_density
