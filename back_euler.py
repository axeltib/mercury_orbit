from base_integrator import Integrator

# child class
class BackEuler(Integrator):

    def __init__(self, initial_conditions, dt, t_end, t_start=0):
     # call super() function
        super().__init__(initial_conditions, dt, t_end, t_start)


    def _r_rate_function(self, r, phi_dot):
        return (-4*self.M**2 + 2*self.M*r + (r-5*self.M) * r**3 * phi_dot**3) / (r**3)


    def _r_function(self, r_dot):
        return r_dot


    def _phi_rate_function(self, r, r_dot, phi_dot):
        return (2 * (-3*self.M + r) * r_dot * phi_dot ) / ((2*self.M - r) * r)


    def _phi_rate_derivative(self, r, r_dot):
        return (2 * (-3*self.M + r) * r_dot) / ((2*self.M - r) * r)


    def _phi_function(self, phi_dot):
        return phi_dot


    def get_phi_rate(self, initial_guess, r, r_dot, threshold=0.01):
        print(self._phi_rate_function(r, r_dot, initial_guess))
        x_new = initial_guess - self._phi_rate_function(r, r_dot, initial_guess) / self._phi_rate_derivative(r, r_dot)
        if abs(x_new - initial_guess) < threshold:
            return x_new
        else:
            return self.get_phi_rate(x_new, r, r_dot)


    def integrate_step(self, t):
       # Implementation of the back euler algorithm
        # First, integrate the rate of r
        self.obs["r_dot"].append(self.obs["r_dot"][-1] + self.dt * self._r_rate_function(self.obs["r"][-1], self.obs["phi_dot"][-1]))
        self.obs["r"].append(self.obs["r"][-1] + self.dt * self._r_function(self.obs["r_dot"][-1]))
        # new_r_dot  = self.obs["r_dot"][-1] + self.dt * self._r_rate_function(self.obs["r"][-1], self.obs["phi_dot"][-1])
        # new_r = self.obs["r"][-1] + self.dt * self._r_function(new_r_dot)
        
        # The, we can use back Euler for phi_dot
        self.obs["phi_dot"].append(self.get_phi_rate(self.obs["phi_dot"][-1], self.obs["r"][-1], self.obs["r_dot"][-1]))
        self.obs["phi"].append(self.obs["phi"][-1] + self.dt * self.obs["phi_dot"][-1])
        # new_phi_dot = self.get_phi_rate(self.obs["phi_dot"][-1], new_r, new_r_dot)
        # new_phi = self.obs["phi"][-1] + self.dt * new_phi_dot
        
        

def main():
    t_start = 0
    t_end = 1
    dt = 0.1
    
    initial_conditions = {
        "r": 1, 
        "r_dot": 1, 
        "phi": 1, 
        "phi_dot": 1, 
        "t": t_start
    }
    
    integrator = BackEuler(initial_conditions, dt, t_end, t_start)
    
    integrator.run_simulation()
    print(integrator.obs["phi"])

if __name__ == '__main__':
    main()