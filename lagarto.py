class lagarto:
    def __init__(self, name, years, factor) -> None:
        self._name = name
        self._years = years
        self._factor = factor

    def computeage(self):
        return self._years*self._factor
