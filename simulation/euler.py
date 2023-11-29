import numpy as np
import matplotlib.pyplot as plt


class EulerMethod:
    """Implementation of Euler Method"""

    def __init__(self, duration, step):
        assert duration > 0
        assert step > 0
        self.step = step
        self.iter_max = int(duration / step)

    def compute(self, initial, f, f_param):
        """Execute Euler method"""
        result = np.zeros(shape=(len(initial), self.iter_max + 1))
        result[..., 0] += initial
        for t in range(1, self.iter_max + 1):
            a = f(result, t, **f_param)
            result[..., t] = result[..., t - 1] + self.step * a
        return result


def f_FTL(data, t, V=30, alpha_c=10, alpha_v=40, alpha_inf=60):
    """Function used by FTL model"""
    temp = np.ediff1d(data[..., t - 1], to_end=np.array([alpha_inf]))
    temp = 1 - np.exp(-(temp - alpha_c) / (alpha_v - alpha_c))
    temp[temp < 0] = 0
    # print(temp)
    return V * temp
