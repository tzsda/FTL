import numpy as np


class EulerMethod:
    """Implementation of Euler Method"""

    def __init__(self, duration, step):
        assert duration > 0
        assert step > 0
        self.step = step
        self.iter_max = int(duration / step)

    def compute(self, initial, f, f_param, callback=None, callback_parameters={}):
        """Execute Euler method"""
        result = np.zeros(shape=(len(initial), self.iter_max + 1))
        result[..., 0] += initial
        for t in range(1, self.iter_max + 1):
            a = f(result, t, **f_param)
            if callable(callback):
                a = callback(a, **callback_parameters)
            result[..., t] = result[..., t - 1] + self.step * a
        return result
