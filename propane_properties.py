from enum import Enum


class DensType(Enum):
    molar_density = "Molar Density"  # 1 / molar volume = moles / volume
    mass_density = "Mass Density"  # mass / volume


def calculate_density(p: float, T: float, dens_type: DensType):
    """
    Some text

    Some more text

    Final part of text
    """
    
    dens_type = dens_type.value
    
    density = 1
    return density