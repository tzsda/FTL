import numpy as np


class EulerMethod:
    """Implementation of Euler Method"""

    def __init__(self, duration, step, callback=None, callback_parameters={}):
        assert duration > 0
        assert step > 0
        self.step = step
        self.iter_max = int(duration / step)
        self.callback = callback
        self.callback_parameters = callback_parameters

    def compute(
        self,
        initial,
        f,
        f_param,
    ):
        """Execute Euler method"""
        result = np.zeros(shape=(len(initial), self.iter_max + 1))
        result[..., 0] += initial
        for t in range(1, self.iter_max + 1):
            a = f(result, t, **f_param)
            if callable(self.callback):
                a = self.callback(a, **self.callback_parameters)
            result[..., t] = result[..., t - 1] + self.step * a
        return result
