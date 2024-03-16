import numpy as np

from application import Application
from processor import IdealProcessor
from plotter import gen_speedup_plt, gen_efficiency_plt

P_CORE_LIST = [1, 2, 10, 50, 100]


def main():
    processors = []
    apps = []

    # gen processors
    for cn in P_CORE_LIST:
        processors.append(IdealProcessor(cn))

    # gen app list
    for i in range(50):
        apps.append(Application(i / 50.0, t=1))

    # plot the result
    gen_speedup_plt(processors=processors, apps=apps)
    gen_efficiency_plt(processors=processors, apps=apps)


if __name__ == "__main__":
    main()
