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
        # self.obs = {"r": [], "r_dot": [], "phi": [], "phi_dot": [], "t": []}
        self.obs = np.empty((1,4))
        self.initiate_initial_condition(initial_conditions)
        
    def function_r_dot(self, x):
        terms =[
            4 * self.M**3,
            - 4 * self.M**2 * x[0], 
            - 4 * self.M * x[0]**3 * x[3]**2,
            4 * self.M * x[0]**4 * x[3]**2, 
            - x[0]**5 * x[3]**2, 
            x[0]**2 * (self.M - 3*self.M*x[1]**2)
        ]
        return sum(terms) / ((2*self.M - x[0]) * x[0]**3)
        
    def function_r(self, x):
        return x[1]

    def function_phi_dot(self, x):
        r = x[0]
        r_dot = x[1]
        phi_dot = x[3]
        return (2 * (-3*self.M + r) * r_dot * phi_dot ) / ((2*self.M - r) * r)
    
    def function_phi(self, x):
        return x[3]
    
    def get_functions(self, x):
        return np.array([
            self.function_r(x), 
            self.function_r_dot(x), 
            self.function_phi(x), 
            self.function_phi_dot(x) 
        ]).T
    
    def initiate_initial_condition(self, initial_conditions):
        for i, val in enumerate(initial_conditions):
            self.obs[0,i] = val

    def get_system_energy(self):
        """ Calculates the energy of the system at all saved states. """
        term1 = 1 - 2*self.M/self.obs[:,0]
        term2 = 1/term1 * self.obs[:,1]**2
        term3 = self.obs[:,0]**2 * self.obs[:,3]**2
        
        derivative = 1 / np.sqrt(term1 - term2 - term3)
        
        return (1 - 2*self.M/self.obs[:,0]) * derivative

    def integrate_step(self, t):
        """ Is implemented for each method. """
        pass

        
    def run_simulation(self):
        """ Runs the simulator. """
        for t in self.t_array:
            self.obs = np.vstack((self.obs, self.integrate_step(t)))
            
    
def main():
    # Tests that the base integrator works
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