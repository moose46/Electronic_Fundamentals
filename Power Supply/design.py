DEGREE_SYMBOL = "\u00B0"
MU_SYMBOL = "\u03BC"
THETA_SYMBOL = "\u03B8"


class PowerSupply:
    def __init__(self, frequency: [int | float] = 50, current: [int, float] = 1, mfd: [float | int] = 0.0):
        self._frequency = frequency * 4
        self._current = current
        self._ripple = 0
        self._capacitance = mfd

    def calc_mfd(self, voltage_ripple=1.2):
        self._capacitance = self._current / (self._frequency * voltage_ripple)
        self._ripple = voltage_ripple
        return self._capacitance

    def calc_ripple(self, pcapacitance):
        self._ripple = self._current / (self._frequency * pcapacitance)
        return self._ripple

    def __repr__(self):
        return f'frequency={self._frequency / 4}Hz / %Vr = {self._ripple:0.02f} / {self._capacitance:.02}{MU_SYMBOL}Fd I={self._current}'


psu = PowerSupply()

print(f'C = {psu.calc_mfd(voltage_ripple=1.2):.2}{MU_SYMBOL}Fd')

print(f'%Vr = {psu.calc_ripple(pcapacitance=.0042):.2}')

psu1 = PowerSupply(frequency=60, current=7)
psu1.calc_mfd(voltage_ripple=.02)
# psu1.mfd(voltage_ripple=1)
print(psu1)
