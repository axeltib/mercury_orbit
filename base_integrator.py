import numpy as np

class Integrator:
    def __init__(self, initial_conditions, dt, t_end, t_start=0, M=1):
        
        # Check that inputs are correct
        assert dt > 0
        assert t_start < t_end
        assert dt < t_end - t_start
        
        self.dt = dt
        self.t_start, self.t_end = t_start, t_end
        self.n_steps = int((t_end - t_start) // dt)
        
        self.t_array = np.linspace(t_start, t_end, self.n_steps)
        
        # Physical quantities
        self.M = M
        # Defining the observables used
        self.obs = {"r": [], "r_dot": [], "phi": [], "phi_dot": [], "t": []}
        self.initiate_initial_condition(initial_conditions)
        
    
    def initiate_initial_condition(self, initial_conditions):
        for key, val in initial_conditions.items():
            assert key in self.obs
            self.obs[key].append(val)
    
    
    def save_observable(self, key, val):
        """ Used to save the current state of the system, such that it can be retrieved later. """
        self.obs[key].append(val)

    def update_observables(self):
        pass

    def integrate_step(self, t):
        pass

        
    def run_simulation(self):
        
        for t in self.t_array:
            self.integrate_step(t)
            
        return self.obs
    
    
def main():
    
    t_start = 0
    t_end = 1
    dt = 0.1
    
    initial_conditions = {
        "r": 1, 
        "r_dot": 0, 
        "phi": 1, 
        "phi_dot": 0, 
        "t": t_start
    }
    
    integrator = Integrator(initial_conditions, dt, t_end, t_start)
    integrator.run_simulation()
    
if __name__ == '__main__':
    main()