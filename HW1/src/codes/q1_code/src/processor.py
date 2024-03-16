from abc import ABC, abstractclassmethod
from application import Application


class Processor(ABC):
    """
    Abstract Processor class
    """

    def __init__(self, core_units: int) -> None:
        """
        Each processor must be defined by their cores number.

        :param core_units: number of system cores
        """
        self.core_units = core_units


class IdealProcessor(Processor):
    def __init__(self, core_units: int) -> None:
        super().__init__(core_units)

    def get_speedup(self, app: Application) -> float:
        """
        Ideal Processor calculate speedup based on Amdahl's law

        :param app: input application
        :return: speedup
        """
        # calculate performance gain via Amdahl's law
        return 1.0 / (((1 - app.f) / self.core_units) + app.f)

    def get_efficiency(self, app: Application) -> float:
        """
        calculate efficiency by diving speedup by number of cores

        :param app: input application
        :return: efficient
        """
        return self.get_speedup(app) / self.core_units
