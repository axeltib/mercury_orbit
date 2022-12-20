import numpy as np

from integrators.base_integrator import Integrator

# child class
class BackEuler(Integrator):

    def __init__(self, initial_conditions, dt, t_end, t_start=0, M=1):
        super().__init__(initial_conditions, dt, t_end, t_start, M)

    # def function_r_dot(self, x):
    #     return (-4*self.M**2 + 2*self.M*x[0] + (x[0]-5*self.M) * x[0]**3 * x[3]**2) / (x[0]**3)

    def get_jacobian(self, x):
        # TODO rewrite this thing
        r = x[0]
        r_dot = x[1]
        phi_dot = x[3]
        
        # Define jacobian
        J = np.zeros((4,4)) + np.diag(np.array([1, 1, 1, 1]))
        # Define non-trivial elemts of the matrix
        J[0,1] = -self.dt
        # J[1,0] = -self.dt * ( 12*self.M**2 / (r**4) - 4*self.M / (r**3) + phi_dot**2)
        terms_j10 = [
            (16*x[0] - 24*self.M) * self.M**3 * x[0]**2 / (((2*self.M-x[0]) * x[0]**3)**2), 
            (16*self.M - 12*x[0]) * self.M**2 * x[0] / (((2*self.M-x[0]) * x[0]**2)**2), 
            (4*self.M * x[0] * x[3]**2 - 4*self.M**2 * x[3]**2 - x[0]**2 * x[3]**2) / ((2*self.M - x[0])**2), 
            (4*self.M * x[3]**2 - 2 * x[0] * x[3]**2)
        ]
        J[1,0] = -self.dt * sum(terms_j10)
        J[1,1] += -self.dt * -6*self.M * x[1] / ((2*self.M - x[0])*x[0] )
        J[1,3] = -self.dt * x[3] / (2*self.M - x[0]) * (8*self.M * x[0] - 8*self.M**2 - 2 * x[0]**2)
        J[2,3] = -self.dt 
        J[3,0] = -self.dt * (  ( 12 * (self.M-r)* self.M * r_dot * phi_dot ) / (( (2*self.M-r) * r)**2 ) + (2 * r_dot * phi_dot) / ((2*self.M - r)**2) )
        J[3,1] = -self.dt * (2 * (-3*self.M - r) * phi_dot) / ((2*self.M - r) * r)
        J[3,3] += -self.dt * (2 * (-3*self.M - r) * r_dot) / ((2*self.M - r) * r)
        
        return J

    def newtons_method(self, last_time_step, epsilon=1e-7):
        """ Returns the next state of the system. """
        x = last_time_step
        x_old = x + 1
        
        while np.linalg.norm(x_old - x) > epsilon:        
            jacobian = self.get_jacobian(x)
            
            F = x - last_time_step - self.dt * np.array([
                self.function_r(x), 
                self.function_r_dot(x), 
                self.function_phi(x), 
                self.function_phi_dot(x) 
            ]).T
            
            y = - np.matmul(np.linalg.inv(jacobian), F)
            x_old = x
            x += y

        return x
        
    def integrate_step(self, t):
        last_time_step = self.obs[-1,:]
        return self.newtons_method(last_time_step)
        
        
        

def main():
    t_start = 0
    t_end = 1
    dt = 0.001
    
    # initial_conditions = {
    #     "r": 1, 
    #     "r_dot": 1, 
    #     "phi": 1, 
    #     "phi_dot": 1, 
    #     "t": t_start
    # }
    
    initial_conditions = np.array([1.0,1.0,1.0,1.0])
    
    integrator = BackEuler(initial_conditions, dt, t_end, t_start)
    integrator.newtons_method(initial_conditions, initial_conditions)
    
if __name__ == '__main__':
    main()