import pickle

def save_integrators(integrators: dict, base_name: str, save_dir: str):
    for dt, integrator in integrators.items():
        with open("{0}/{1}_{2}".format(save_dir, base_name, dt), "wb") as f:
            pickle.dump(integrator, f)