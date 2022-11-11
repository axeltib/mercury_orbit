class Integrator:
    def __init__(self, dt):
        self.dt = dt

        # Physical quantities
        self.M = None
        
        # Defining the observables used
        self.observables = {"r": None, "r_dot": None, "phi": None, "phi_dot": None, "t": None}
    
    def define_initial_condition(self):
        pass
    
    def save_observables(self):
        """ Used to save the current state of the system, such that it can be retrieved later. """
        pass

    def integrate_step(self):
        pass
        
    def run_simulation(self):
        pass
    
    