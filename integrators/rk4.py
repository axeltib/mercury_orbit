import numpy as np

from integrators.base_integrator import Integrator

class Rk4Integrator(Integrator): 
    
    def __init__(self, initial_conditions, dt, t_end, t_start=0, M=1):
        super().__init__(initial_conditions, dt, t_end, t_start, M)
        
        
    def get_integration_step(self, x):
        k1 = self.get_functions(x)
        k2 = self.get_functions(x + self.dt/2*k1)
        k3 = self.get_functions(x + self.dt/2*k2)
        k4 = self.get_functions(x + self.dt*k3)

        return x + 1/6 * (k1 + 2*k2 + 2*k3 + k4)*self.dt

    def integrate_step(self, t):
        return self.get_integration_step(self.obs[-1,:])

