class Application:
    """
    simple Application Class
    """

    def __init__(self, f: float, t: float) -> None:
        """
        each application is expressed by baseline execution time and
        their sequential fragment

        :param f: sequential fragment
        :param t: baseline exec time
        """

        if f > 1 or f < 0:
            raise ValueError("invalid sequnetial fragment! f is not in range (0, 1)")

        self.f = f  # set sequential fragment
        self.t = t  # execution time on base model
