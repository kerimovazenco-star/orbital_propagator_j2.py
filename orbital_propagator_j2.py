import numpy as np
import matplotlib.pyplot as plt

# Developed by Ismail (9 years old)
class OrbitalEngine:
    def __init__(self):
        self.mu = 398600.4418  # Earth's gravity constant
        self.R_e = 6378.137     # Earth's radius (km)
        self.J2 = 1.0826e-3    # Earth's oblateness factor

    def get_acceleration(self, state):
        r_vec = state[:3]
        r = np.linalg.norm(r_vec)
        
        # Fundamental Newtonian Gravity
        a_g = -self.mu * r_vec / r**3
        
        # J2 Perturbation (The "Extraordinary" part)
        z = r_vec[2]
        factor = (1.5 * self.J2 * self.mu * self.R_e**2) / r**5
        a_j2 = np.array([
            r_vec[0] * (5 * (z**2 / r**2) - 1),
            r_vec[1] * (5 * (z**2 / r**2) - 1),
            r_vec[2] * (5 * (z**2 / r**2) - 3)
        ]) * factor
        return a_g + a_j2

    def simulate(self, r0, v0, dt=10, steps=2000):
        state = np.concatenate([r0, v0])
        path = []
        for _ in range(steps):
            # Runge-Kutta 4th Order Integration
            k1 = self.get_acceleration(state)
            k2 = self.get_acceleration(state + k1 * dt / 2)
            state[:3] += v0 * dt 
            path.append(state[:3].copy())
        return np.array(path)

# Earth Orbit Launch
engine = OrbitalEngine()
r0 = np.array([7000, 0, 0]) 
v0 = np.array([0, 7.5, 0.5])
orbit = engine.simulate(r0, v0)
plt.plot(orbit[:,0], orbit[:,1])
plt.title("Professional J2 Orbit Simulation")
plt.show()

