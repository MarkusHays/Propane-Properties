import numpy as np
import matplotlib.pyplot as plt
from data import temp, vapp, get_vap_interp
import propane_properties as pp


def single_density_calc(pressure: float, temperature: float, dens_type: pp.DensType):
    """
    Some text (description)

    Some more text (input)

    Final text (output)
    """
    return pp.calculate_density(pressure, temperature, dens_type)


def calc_density_heatmap(
    p_min: float,
    p_max: float,
    T_min: float,
    T_max: float,
    N: int = 50,
    dens_type: pp.DensType = pp.DensType.mass_density,
):
    """
    Some text

    Some more text

    Final text
    """
    dens_matrix = np.zeros((N, N))
    phase_type_matrix = np.zeros((N, N))
    for j, T in enumerate(np.linspace(T_min, T_max, num=N)):
        for i, p in enumerate(np.linspace(p_min, p_max, num=N)):
            [dens, phase_type] = pp.calculate_density(p, T, dens_type)
            dens_matrix[i, j] = dens
            if phase_type == "Liquid":
                phase_type_matrix[i, j] = 1
            else:
                phase_type_matrix[i, j] = 0

            print(f"Percentage completion: {((i+1)+(j)*N)/(N*N)*100}%")

    ax = plt.subplot()  # Defines ax variable by creating an empty plot
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontname("Arial")
        label.set_fontsize(12)

    plt.pcolormesh(
        np.linspace(259.67, 859.67, num=N),
        np.linspace(0.0234, 1724.0, num=N),
        dens_matrix,
        cmap="RdYlGn",
    )
    if dens_type.value == "Mass Density":
        units = "kg/m3"
    else:
        units = "lb-moles/ft3"
    vapp_calc = get_vap_interp()
    temp_intrp = np.linspace(T_min, temp[:-6], num=500)
    vapp_intrp = vapp_calc(temp_intrp)
    plt.plot(temp_intrp, vapp_intrp, "k-")
    plt.scatter(temp[-7], vapp[-7], color="k", s=35)

    # Plot formatting
    axis_font = {"fontname": "Arial", "size": "14", "fontweight": "bold"}
    plt.rcParams.update({"font.size": 12})
    plt.rc("font", size=12)
    plt.xlabel("Temperature (R)", **axis_font)
    plt.ylabel("Pressure (psia)", **axis_font)
    plt.xlim(300, 800)
    plt.ylim(0, 1700)
    plt.colorbar(label=f"Density ({units})")
    plt.clim(0, 700)
    plt.show()