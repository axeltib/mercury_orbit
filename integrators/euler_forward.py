import numpy as np

from integrators.base_integrator import Integrator


class EulerForward(Integrator):
    def __init__(self, initial_conditions, dt, t_end, t_start=0, M=1):
        super().__init__(initial_conditions, dt, t_end, t_start, M)
        
        
    def integrate_step(self, t):
        x = self.obs[-1,:]
        return x + self.dt * self.get_functions(x)
