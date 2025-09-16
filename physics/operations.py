"""
Physics and mathematical operations module.

This module contains common physics and mathematics operations
that can be used for simulations and computations.
"""

import numpy as np
import math


# Physics Constants
class Constants:
    """Physical constants for physics calculations."""
    
    # Universal constants
    c = 299792458  # Speed of light in vacuum (m/s)
    h = 6.62607015e-34  # Planck constant (J⋅s)
    hbar = h / (2 * math.pi)  # Reduced Planck constant
    G = 6.67430e-11  # Gravitational constant (m³⋅kg⁻¹⋅s⁻²)
    k_B = 1.380649e-23  # Boltzmann constant (J/K)
    N_A = 6.02214076e23  # Avogadro constant (mol⁻¹)
    R = 8.314462618  # Gas constant (J⋅mol⁻¹⋅K⁻¹)
    
    # Electromagnetic constants
    epsilon_0 = 8.8541878128e-12  # Vacuum permittivity (F/m)
    mu_0 = 4 * math.pi * 1e-7  # Vacuum permeability (H/m)
    e = 1.602176634e-19  # Elementary charge (C)
    
    # Particle masses (kg)
    m_e = 9.1093837015e-31  # Electron mass
    m_p = 1.67262192369e-27  # Proton mass
    m_n = 1.67492749804e-27  # Neutron mass


# Mechanics Operations
def kinetic_energy(mass, velocity):
    """
    Calculate kinetic energy.
    
    Args:
        mass (float): Mass in kg
        velocity (float): Velocity in m/s
    
    Returns:
        float: Kinetic energy in Joules
    """
    return 0.5 * mass * velocity**2


def potential_energy_gravity(mass, height, g=9.81):
    """
    Calculate gravitational potential energy.
    
    Args:
        mass (float): Mass in kg
        height (float): Height in meters
        g (float): Gravitational acceleration (default: 9.81 m/s²)
    
    Returns:
        float: Potential energy in Joules
    """
    return mass * g * height


def force_gravity(mass1, mass2, distance):
    """
    Calculate gravitational force between two masses.
    
    Args:
        mass1 (float): First mass in kg
        mass2 (float): Second mass in kg
        distance (float): Distance between masses in meters
    
    Returns:
        float: Gravitational force in Newtons
    """
    return Constants.G * mass1 * mass2 / distance**2


def centripetal_force(mass, velocity, radius):
    """
    Calculate centripetal force.
    
    Args:
        mass (float): Mass in kg
        velocity (float): Velocity in m/s
        radius (float): Radius in meters
    
    Returns:
        float: Centripetal force in Newtons
    """
    return mass * velocity**2 / radius


# Thermodynamics Operations
def ideal_gas_pressure(n, temperature, volume):
    """
    Calculate pressure using ideal gas law.
    
    Args:
        n (float): Number of moles
        temperature (float): Temperature in Kelvin
        volume (float): Volume in m³
    
    Returns:
        float: Pressure in Pascals
    """
    return n * Constants.R * temperature / volume


def thermal_energy(temperature):
    """
    Calculate thermal energy per particle.
    
    Args:
        temperature (float): Temperature in Kelvin
    
    Returns:
        float: Thermal energy in Joules
    """
    return 1.5 * Constants.k_B * temperature


# Electromagnetism Operations
def coulomb_force(charge1, charge2, distance):
    """
    Calculate electrostatic force between two charges.
    
    Args:
        charge1 (float): First charge in Coulombs
        charge2 (float): Second charge in Coulombs
        distance (float): Distance between charges in meters
    
    Returns:
        float: Electrostatic force in Newtons
    """
    k = 1 / (4 * math.pi * Constants.epsilon_0)
    return k * charge1 * charge2 / distance**2


def electric_field(charge, distance):
    """
    Calculate electric field at a distance from a point charge.
    
    Args:
        charge (float): Charge in Coulombs
        distance (float): Distance from charge in meters
    
    Returns:
        float: Electric field strength in N/C
    """
    k = 1 / (4 * math.pi * Constants.epsilon_0)
    return k * charge / distance**2


def magnetic_force(charge, velocity, magnetic_field):
    """
    Calculate magnetic force on a moving charge.
    
    Args:
        charge (float): Charge in Coulombs
        velocity (float): Velocity in m/s
        magnetic_field (float): Magnetic field strength in Tesla
    
    Returns:
        float: Magnetic force in Newtons
    """
    return charge * velocity * magnetic_field


# Wave and Oscillation Operations
def wave_frequency(wavelength, speed=Constants.c):
    """
    Calculate wave frequency.
    
    Args:
        wavelength (float): Wavelength in meters
        speed (float): Wave speed (default: speed of light)
    
    Returns:
        float: Frequency in Hz
    """
    return speed / wavelength


def wave_energy(frequency):
    """
    Calculate photon energy.
    
    Args:
        frequency (float): Frequency in Hz
    
    Returns:
        float: Energy in Joules
    """
    return Constants.h * frequency


def simple_harmonic_motion(amplitude, angular_frequency, time, phase=0):
    """
    Calculate position in simple harmonic motion.
    
    Args:
        amplitude (float): Amplitude
        angular_frequency (float): Angular frequency in rad/s
        time (float): Time in seconds
        phase (float): Phase offset in radians (default: 0)
    
    Returns:
        float: Position
    """
    return amplitude * math.cos(angular_frequency * time + phase)


# Mathematical Utilities
def vector_magnitude(vector):
    """
    Calculate magnitude of a vector.
    
    Args:
        vector (list or numpy.array): Vector components
    
    Returns:
        float: Vector magnitude
    """
    return np.sqrt(sum(x**2 for x in vector))


def dot_product(vector1, vector2):
    """
    Calculate dot product of two vectors.
    
    Args:
        vector1 (list or numpy.array): First vector
        vector2 (list or numpy.array): Second vector
    
    Returns:
        float: Dot product
    """
    return sum(a * b for a, b in zip(vector1, vector2))


def cross_product(vector1, vector2):
    """
    Calculate cross product of two 3D vectors.
    
    Args:
        vector1 (list or numpy.array): First 3D vector
        vector2 (list or numpy.array): Second 3D vector
    
    Returns:
        numpy.array: Cross product vector
    """
    return np.cross(vector1, vector2)


def distance_3d(point1, point2):
    """
    Calculate 3D distance between two points.
    
    Args:
        point1 (list or tuple): First point (x, y, z)
        point2 (list or tuple): Second point (x, y, z)
    
    Returns:
        float: Distance
    """
    return math.sqrt(sum((a - b)**2 for a, b in zip(point1, point2)))


# Numerical Integration and Differentiation
def numerical_derivative(func, x, h=1e-5):
    """
    Calculate numerical derivative using central difference.
    
    Args:
        func (callable): Function to differentiate
        x (float): Point at which to calculate derivative
        h (float): Step size (default: 1e-5)
    
    Returns:
        float: Derivative approximation
    """
    return (func(x + h) - func(x - h)) / (2 * h)


def trapezoidal_integration(func, a, b, n=1000):
    """
    Numerical integration using trapezoidal rule.
    
    Args:
        func (callable): Function to integrate
        a (float): Lower bound
        b (float): Upper bound
        n (int): Number of subdivisions (default: 1000)
    
    Returns:
        float: Integral approximation
    """
    h = (b - a) / n
    result = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        result += func(a + i * h)
    return result * h


# Unit Conversions
def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


def degrees_to_radians(degrees):
    """Convert degrees to radians."""
    return degrees * math.pi / 180


def radians_to_degrees(radians):
    """Convert radians to degrees."""
    return radians * 180 / math.pi


def eV_to_joules(eV):
    """Convert electron volts to Joules."""
    return eV * Constants.e


def joules_to_eV(joules):
    """Convert Joules to electron volts."""
    return joules / Constants.e