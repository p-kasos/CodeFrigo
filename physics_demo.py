#!/usr/bin/env python3
"""
Example usage of the physics module for common calculations.
"""

import physics
import math

def main():
    print("=== Physics Module Demo ===\n")
    
    # Mechanics calculations
    print("1. Mechanics Calculations:")
    mass = 2.0  # kg
    velocity = 10.0  # m/s
    height = 5.0  # m
    
    ke = physics.kinetic_energy(mass, velocity)
    pe = physics.potential_energy_gravity(mass, height)
    total_energy = ke + pe
    
    print(f"   Mass: {mass} kg")
    print(f"   Velocity: {velocity} m/s")
    print(f"   Height: {height} m")
    print(f"   Kinetic Energy: {ke:.1f} J")
    print(f"   Potential Energy: {pe:.1f} J")
    print(f"   Total Energy: {total_energy:.1f} J\n")
    
    # Electromagnetic calculations
    print("2. Electromagnetic Calculations:")
    charge1 = 1e-6  # C
    charge2 = -1e-6  # C
    distance = 0.1  # m
    
    force = physics.coulomb_force(charge1, charge2, distance)
    field = physics.electric_field(charge1, distance)
    
    print(f"   Charge 1: {charge1*1e6:.1f} μC")
    print(f"   Charge 2: {charge2*1e6:.1f} μC")
    print(f"   Distance: {distance} m")
    print(f"   Coulomb Force: {force:.3f} N")
    print(f"   Electric Field: {field:.1f} N/C\n")
    
    # Wave calculations
    print("3. Wave Calculations:")
    wavelength = 500e-9  # m (green light)
    frequency = physics.wave_frequency(wavelength)
    energy = physics.wave_energy(frequency)
    
    print(f"   Wavelength: {wavelength*1e9:.0f} nm")
    print(f"   Frequency: {frequency:.2e} Hz")
    print(f"   Photon Energy: {energy:.2e} J")
    print(f"   Photon Energy: {physics.joules_to_eV(energy):.2f} eV\n")
    
    # Thermodynamics
    print("4. Thermodynamics:")
    temp_celsius = 25.0
    temp_kelvin = physics.celsius_to_kelvin(temp_celsius)
    thermal_energy = physics.thermal_energy(temp_kelvin)
    
    print(f"   Temperature: {temp_celsius}°C = {temp_kelvin} K")
    print(f"   Thermal Energy per particle: {thermal_energy:.2e} J\n")
    
    # Vector operations
    print("5. Vector Operations:")
    vec1 = [3, 4, 0]
    vec2 = [1, 2, 5]
    
    magnitude = physics.vector_magnitude(vec1)
    dot_prod = physics.dot_product(vec1, vec2)
    cross_prod = physics.cross_product(vec1, vec2)
    
    print(f"   Vector 1: {vec1}")
    print(f"   Vector 2: {vec2}")
    print(f"   Magnitude of Vector 1: {magnitude:.2f}")
    print(f"   Dot Product: {dot_prod}")
    print(f"   Cross Product: {cross_prod.tolist()}\n")
    
    # Physical constants
    print("6. Physical Constants:")
    print(f"   Speed of light: {physics.Constants.c:,} m/s")
    print(f"   Planck constant: {physics.Constants.h:.2e} J⋅s")
    print(f"   Electron mass: {physics.Constants.m_e:.2e} kg")
    print(f"   Elementary charge: {physics.Constants.e:.2e} C")

if __name__ == "__main__":
    main()