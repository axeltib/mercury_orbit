import numpy as np

import matplotlib
import matplotlib.pyplot as plt

from scipy.stats import linregress
from scipy.signal import find_peaks

# PLotting parameters
# plt.rcParams['text.usetex'] = True

plt.rcParams["font.size"] = 24
plt.rcParams['xtick.major.size'] = 5.0
plt.rcParams['xtick.minor.size'] = 3.0
plt.rcParams['ytick.major.size'] = 5.0
plt.rcParams['ytick.minor.size'] = 3.0


plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def generate_figure(ax, fig, name):
    ax.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
    ax.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
    ax.grid()
    #ax.legend()

    ax.set_xlabel("$dt$")
    ax.set_ylabel("System energy trend slope")

    ax.ticklabel_format(style='sci')

    # ax.set_xticks(np.arange(0, 0.11, 0.025))

    #plt.show()

    fig.savefig("report/"+name, dpi=1000)
    

def generate_energy_radius(integrators):
    fig, axs = plt.subplots(2,1, figsize=(15,15), sharex=True)
    fig.subplots_adjust(hspace=.05)

    for dt, integrator in integrators.items():
        # if dt == "0.1":
        #     continue
        #axs[0].plot(np.append(integrator.t_array, t_end), integrator.get_system_energy(), label=dt)
        #axs[0].plot(integrator.obs[:,2], integrator.get_system_energy(), label=dt)
        axs[0].plot(np.append(integrator.t_array, integrator.t_end), integrator.get_system_energy(), label=dt)
        axs[1].plot(np.append(integrator.t_array, integrator.t_end), integrator.obs[:,0], label=dt)
        #axs[1].plot(integrator.obs[:,0]*np.cos(integrator.obs[:,2]), integrator.obs[:,0]*np.sin(integrator.obs[:,2]), label=dt)
    # ax.plot(t_array, f)

    axs[0].legend()
    axs[0].grid()
    axs[1].grid()
    axs[0].set_ylabel(r"Energy")
    axs[1].set_ylabel(r"Radius")
    axs[1].set_xlabel(r"Time t")
    fig.tight_layout()
    
    return fig, axs


def generate_precession_graph(integrators, title = None):
    fig, ax = plt.subplots(1,1, figsize=(5,5))

    dts = [float(key) for key in integrators.keys()]
    change_avgs = []

    # finding the perihelions
    for dt, integrator in integrators.items():
        # Finding valleys/perihelions
        peri_ind, _ = find_peaks(-integrator.obs[:,0])
        peri_ind = np.insert(peri_ind, 0, 0)
        # print(dt, integrator.obs[peri_ind, 2]/(2 * np.pi))
        change = np.diff(integrator.obs[peri_ind, 2]/(np.pi)) - 2
        change_avg = np.mean(change)
        change_avgs.append(change_avg)
        ax.scatter([float(dt)]*len(change), change)
    
    ax.grid()
    ax.set_xlabel("Timestep size")
    ax.set_ylabel(r"Orbit Precession, $\pi$ radians")
    fig.tight_layout()
    if title:
        ax.set_title(title)
    
    return fig, ax