# Chapter-6/resistor.py

"""
# - Contains functions to calculate series and parallel voltages, current and total resistance
# - serve this page by using python -m mkdocs server from the command line

"""


class Series:
    """
    ## Passed a list of resistor values, and voltages, it will calculate voltage drop across each resistor , total resistance and total current
    """

    def __init__(self, resistors: list[float, int], vs: [int, float]):
        """
        - resistors is a list of resistors in ohms
        - vs is the voltage source in volts
        Examples:
            >>> x = Series([10,10],10)
            >>> x.volts # volts
            10
            >>> x.it
            0.5
            >>> x.rt
            20
            >>> r1 = Series([100,100],10)
            >>> r2 = Series([200,200],vs=20)
            >>> r3 = Series([r1.rt,r2.rt], 25)
            >>> r3.rt
            600

        param resistors:list[int,float]
        param volts:[int,float]
        """
        self._resistors = resistors
        if isinstance(self._resistors[0], Series):
            print('Yes')
            self._resistors[0] = self._resistors[0].rt
        self._volts = vs

    @property
    def rt(self):
        """
        rt = r1 + r2 + r3 + r...
        Examples:
            >>> x =Series([33, 68, 100, 47, 10], 10)
            >>> x.rt
            258

        return: Total Ohms in the series circuit
        """
        if isinstance(self._resistors[0], Series):
            print(f'{self._resistors[0].rt}')
        rt = 0
        [rt := rt + r for r in self._resistors]
        return rt

    @property
    def it(self):
        """
        it = volts/rt
        Examples:
            >>> x = Series([82,18,15,10], vs=25)
            >>> x.it
            0.2

        return: Total Current in the series circuit
        """
        it = self._volts / self.rt
        return round(it, 2)

    @property
    def voltage_drops(self):
        """
        voltage_drop = restance/rt * volts
        Examples:
            >>> x = Series([100,100], 10)
            >>> x.voltage_drops
            {'R1=100Ω': 5.0, 'R2=100Ω': 5.0}

        return: Voltage drop dictionary, for each resitor in the circuit
        """
        drops = dict()
        n = 1
        for r in self._resistors:
            drops[f'R{n}={r}\u03A9'] = round((r / self.rt) * self._volts, 2)
            n += 1
        return drops

    @property
    def volts(self):
        """
        Examples:
            >>> v = Series([100,200], 10)
            >>> v.volts
            10
            >>> v.volts = 26.6
            >>> v.volts
            26.6

        :return:
        """
        return self._volts

    @volts.setter
    def volts(self, value):
        self._volts = value

    def __repr__(self):
        return f"rt={self.rt} \u03A9" \
               f"\nit={self.it}" \
               f"\nvolts({self._volts})={self.voltage_drops}"


x = Series([33, 68, 100, 47, 10], 10)
print(x)
y = Series([x], 35)
print(y)
x.volts = 25
print(x)
