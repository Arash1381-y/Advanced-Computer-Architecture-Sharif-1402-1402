import matplotlib.pyplot as plt
from processor import IdealProcessor
from application import Application
from typing import List


def gen_speedup_plt(processors: List[IdealProcessor], apps: List[Application]):
    """
    generate speedup plt based on applications and hosts(processors) and save it to
    build directory.

    :param processors: list of hosts
    :param apps: list of apps
    :return: None
    """
    fig, ax = plt.subplots()
    fig.suptitle('Speedup of multi-core systems based on program specifications')
    ax.set_xlabel('Sequential Fragment (f)')
    ax.set_ylabel('Speedup (S)')

    for p in processors:
        f_array = [a.f for a in apps]
        p_pgain = [p.get_speedup(app=a) for a in apps]
        ax.plot(f_array, p_pgain, label=f"P={p.core_units}")

    ax.set_yscale("log")
    ax.legend(loc="upper right")
    plt.savefig("../out/speedup.png")


def gen_efficiency_plt(processors: List[IdealProcessor], apps: List[Application]):
    """
    generate efficiency plt based on applications and hosts(processors) and save it to
    build directory.

    :param processors: list of hosts(processors)
    :param apps: list of applications
    :return: None
    """
    fig, ax = plt.subplots()
    fig.suptitle('Efficiency of multi-core systems based on program specification')
    ax.set_xlabel('Sequential Fragment (f)')
    ax.set_ylabel('Efficiency (E)')

    for p in processors:
        f_array = [a.f for a in apps]
        p_efficiency = [p.get_speedup(app=a) / p.core_units for a in apps]
        ax.plot(f_array, p_efficiency, label=f"P={p.core_units}")

    ax.legend(loc="upper right")
    plt.savefig("../out/efficiency.png")
