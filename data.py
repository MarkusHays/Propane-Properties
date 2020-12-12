from scipy.interpolate import interp1d

# Temperatures used when generating the database of vapor pressures and density bounds
temp = [
    259.67,
    289.67,
    319.67,
    349.67,
    379.67,
    409.67,
    439.67,
    469.67,
    499.67,
    529.67,
    559.67,
    589.67,
    619.67,
    649.67,
    665.69,
    695.69,
    725.69,
    755.69,
    785.69,
    815.69,
    859.67,
]

# Liquid Upper Molar Density bound
LU_MD = [
    0.9459,
    0.9190,
    0.8943,
    0.8712,
    0.8490,
    0.8274,
    0.8060,
    0.7843,
    0.7619,
    0.7385,
    0.7136,
    0.6865,
    0.6564,
    0.6221,
    0.6016,
    0.5577,
    0.5058,
    0.4477,
    0.3906,
    0.3410,
    0.2857,
]

# Liquid Lower Molar Density bound
LL_MD = [
    0.9408,
    0.9125,
    0.8862,
    0.8612,
    0.8369,
    0.8127,
    0.7881,
    0.7625,
    0.7352,
    0.7052,
    0.6711,
    0.6301,
    0.5758,
    0.4825,
    0.3739,
    0.3774,
    0.3381,
    0.3207,
    0.3113,
    0.3053,
    0.2857,
]

# Vapor Upper Molar Density bound
VU_MD = [
    8.40e-06,
    4.77e-05,
    1.88e-04,
    5.65e-04,
    1.40e-03,
    2.99e-03,
    5.74e-03,
    1.01e-02,
    1.68e-02,
    2.66e-02,
    4.08e-02,
    6.18e-02,
    0.0944,
    0.1572,
    0.3739,
    0.3774,
    0.3381,
    0.3207,
    0.3113,
    0.3053,
    0.2857,
]

# Vapor Lower Molar Density bound
VL_MD = [
    8.40e-06,
    7.53e-06,
    6.83e-06,
    6.24e-06,
    5.75e-06,
    5.33e-06,
    4.96e-06,
    4.65e-06,
    4.37e-06,
    4.12e-06,
    3.90e-06,
    3.70e-06,
    3.52e-06,
    3.36e-06,
    3.28e-06,
    3.14e-06,
    3.01e-06,
    2.89e-06,
    2.78e-06,
    2.67e-06,
    2.54e-06,
]

# Vapor and pseudo-vapor pressures
vapp = [
    2.34e-02,
    1.48e-01,
    6.41e-01,
    2.10e00,
    5.58e00,
    1.27e01,
    2.54e01,
    4.64e01,
    7.85e01,
    1.25e02,
    1.89e02,
    2.75e02,
    3.86e02,
    5.27e02,
    6.16e02,  # <- Critical point
    8.74e02,
    1.05e03,
    1.22e03,
    1.39e03,
    1.56e03,
    1.72e03,
]


def get_interp_functions():
    """
    Generate interpolation for density upper and lower limits.
    """
    dens_upper_vapor = interp1d(temp, VU_MD)
    dens_lower_vapor = interp1d(temp, VL_MD)
    dens_upper_liquid = interp1d(temp, LU_MD)
    dens_lower_liquid = interp1d(temp, LL_MD)
    return dens_upper_vapor, dens_lower_vapor, dens_upper_liquid, dens_lower_liquid


def get_vap_interp():
    """
    Generate interpolation for vapor pressure curve.
    """
    vap_interp = interp1d(temp, vapp, kind="quadratic")
    return vap_interp