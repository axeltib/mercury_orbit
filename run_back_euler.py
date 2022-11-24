import numpy as np

from back_euler import BackEuler

def main():
    t_start = 0
    t_end = 1
    dt = 0.001
    
    initial_conditions = np.array([1.0,1.0,1.0,1.0])
    
    integrator = BackEuler(initial_conditions, dt, t_end, t_start)
    integrator.run_simulation()
    
    print(np.shape(integrator.obs))
    
if __name__ == '__main__':
    main()