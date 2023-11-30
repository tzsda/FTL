import math

import numpy as np


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


def FTL_traffic_light(data, t, V=30, alpha_c=10, alpha_v=40, alpha_inf=60):
    """Function used by FTL model"""
    temp = np.ediff1d(data[..., t - 1], to_end=np.array([alpha_inf]))
    temp = 1 - np.exp(-(temp - alpha_c) / (alpha_v - alpha_c))
    temp[temp < 0] = 0
    # print(temp)
    return V * temp


def FTL_slowdown(
    data,
    t,
    V=30,
    alpha_c=10,
    alpha_v=40,
    alpha_inf=60,
    max_time=100,
    rate=2,
    min_alpha=30,
):
    """Function used by FTL model"""
    temp = np.ediff1d(
        data[..., t - 1],
        to_end=np.array(
            [
                min_alpha
                + (alpha_inf - min_alpha) 
                * (1 - math.exp(-rate * (t - max_time) ** 2))
            ]
        ),
    )
    temp = 1 - np.exp(-(temp - alpha_c) / (alpha_v - alpha_c))
    temp[temp < 0] = 0
    return V * temp
