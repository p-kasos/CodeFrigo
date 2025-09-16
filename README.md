# CodeFrigo

A comprehensive toolkit for physics and mathematics operations, simulations, and computations, along with laboratory instrument control drivers.

## Features

### Physics Module
The `physics/` folder contains a comprehensive collection of physics and mathematical operations that can be used for:
- **Simulations**: Model physical systems and phenomena
- **Computations**: Perform complex physics calculations
- **Research**: Support for common physics formulas and constants

#### Available Operations
- **Mechanics**: Kinetic energy, potential energy, forces, motion
- **Thermodynamics**: Ideal gas law, thermal energy calculations
- **Electromagnetism**: Coulomb's law, electric and magnetic fields
- **Waves & Oscillations**: Wave properties, harmonic motion
- **Mathematical Utilities**: Vector operations, numerical methods
- **Unit Conversions**: Temperature, angle, energy conversions
- **Physical Constants**: Universal constants for accurate calculations

#### Usage Example
```python
import physics

# Calculate kinetic energy
energy = physics.kinetic_energy(mass=10, velocity=5)  # 125.0 J

# Use physical constants
speed_of_light = physics.Constants.c  # 299792458 m/s

# Convert units
temp_kelvin = physics.celsius_to_kelvin(25)  # 298.15 K
```

### Drivers Module
Laboratory instrument control drivers for various equipment.