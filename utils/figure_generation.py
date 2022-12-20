import matplotlib

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