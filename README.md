Advanced Astrodynamics: J2 Orbital Perturbation Propagator
​This project implements a high-fidelity numerical integrator for satellite orbits, accounting for the Earth's oblateness (J2 effect)
### Mathematical Model (J2 Perturbation)

To account for Earth's non-spherical mass distribution, I used the following J2 potential function:

$$V_{J2} = \frac{\mu J_2 R_E^2}{2r^3} (1 - 3\sin^2 \phi)$$

Where:
* $\mu$ is the Earth's gravitational parameter.
* $J_2$ is the second zonal harmonic coefficient.
* $R_E$ is the Earth's equatorial radius.
* $r$ is the satellite's geocentric distance.
