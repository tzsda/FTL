import math

import numpy as np


def compute_alpha(max_velocity, wished_velocity, alpha_c, alpha_v):
    a = wished_velocity / max_velocity
    return alpha_c + (alpha_c - alpha_v) * math.log(1 - a)


def compute_brake_rate(brake_distance):
    return math.log(2) / (brake_distance**2)


def mod_radius(vector, radius, eps):
    sign = np.sign(vector)
    for j in range(len(vector)):
        while vector[j] - 2 * np.pi * radius >= eps or vector[j] <= -eps:
            vector[j] += sign[j] * 2 * np.pi * radius
    return vector


def mean_velocity(data, step):
    return (np.sum(np.diff(data, axis=1) / step)) / (data.shape[0] * data.shape[1])


def get_name(param, N, init_dist):
    result = str(N) + "-" + str(init_dist) + "-"
    for k, v in param.items():
        result += f"{k}:{v}-"
    return result
