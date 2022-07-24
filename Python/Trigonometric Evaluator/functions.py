from math import factorial, radians, degrees
from decimal import getcontext, Decimal
def set_sign(rt: str, qd: int) -> int:
    if qd == 2 and rt == 'cos':
        return -1
    elif qd == 3:
        return -1
    elif qd == 4 and rt =='sin':
        return -1
    return 1
        

def rnd(num: list, p) -> list:
    return_value: list = []
    for n in range(0, 6):
        if num[n] == 1 or num[n] == 0 or num[n] == -1:
            return_value.append(str(int(num[n])) + '  ' * 15)
            continue
        elif 'Not' in str(num[n]):
            return_value.append(num[n] + '       ')
            continue
        num[n] = Decimal(num[n])
        sign: int = abs(num[n]) / num[n]
        num[n] = abs(num[n])
        for z in range(p, 26)[::-1]:
            num[n] = int(num[n] * 10 ** z + Decimal(0.4)) / Decimal(10 ** z)
        return_value.append(str(num[n] * sign) + '               ')
    return return_value


def quadrant(ang: float) -> int:
    if ang <= 90:
        return 1
    elif ang <= 180:
        return 2
    elif ang <= 270:
        return 3
    elif ang <= 360:
        return 4


class TrigFunc:
    def __init__(self, angle: Decimal ,radian_mode=False):
        if radian_mode:
            self.__angle = degrees(angle)
        else:
            self.__angle = angle
        self.__angle %= 360
        if self.__angle < 0:
            self.__angle += 360
        quad: int = quadrant(self.__angle)
        if quad > 1:
            self.__angle = {2: 180 - self.__angle,
                            3: self.__angle -  180,
                            4: 360 - self.__angle}[quad]
        getcontext().prec = 30
        self.ratios: list = []
        self.ratios.append(self.__cos() * set_sign('cos', quad))
        self.ratios.append(self.__sin() * set_sign('sin', quad))
        self.ratios.append(self.__tan())
        self.ratios.append(self.__csc())
        self.ratios.append(self.__sec())
        self.ratios.append(self.__cot())

    def __cos(self):
        if self.__angle % 90 == 0:
            return {
                90: 0,
                0: 1
            }[self.__angle]
        x = Decimal(radians(self.__angle))
        val = Decimal(0)
        for n in range(0, 55):
            val += (-1) ** n * x ** (2 * n) / factorial(2 * n)
        return val

    def __sin(self):
        return (1 - Decimal(self.ratios[0]) ** Decimal(2)) ** Decimal(0.5)

    def __tan(self):
        try:
            return self.ratios[1] / self.ratios[0]
        except ZeroDivisionError:
            return 'Not Defined / ∞'

    def __csc(self):
        try:
            return 1 / self.ratios[1]
        except ZeroDivisionError:
            return 'Not Defined / ∞'

    def __sec(self):
        try:
            return 1 / self.ratios[0]
        except ZeroDivisionError:
            return 'Not Defined / ∞'

    def __cot(self):
        try:
            return 1 / self.ratios[2]
        except (ZeroDivisionError, TypeError):
            return 'Not Defined / ∞'

