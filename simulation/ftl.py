import math

import numpy as np


def traffic_light(data, t, V=30, alpha_c=10, alpha_v=40, alpha_inf=60):
    """Function used to model a start at green light"""
    temp = np.ediff1d(data[..., t - 1], to_end=np.array([alpha_inf]))
    temp = 1 - np.exp(-(temp - alpha_c) / (alpha_v - alpha_c))
    temp[temp < 0] = 0
    return V * temp


def slowdown(
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
    """Function used to model a traffic jam"""
    alpha = min_alpha + (alpha_inf - min_alpha) * (1 - math.exp(- rate * (t - max_time) ** 2))
    # print("alpha", round(alpha, 4), "t", round(t * 0.2, 4))
    temp = np.ediff1d(
        data[..., t - 1],
        to_end=np.array([alpha]),
    )
    temp = 1 - np.exp(-(temp - alpha_c) / (alpha_v - alpha_c))
    temp[temp < 0] = 0
    return V * temp


def radar(data, t, V=30, alpha_c=10, alpha_v=40, alpha_inf=60, t_start=10, t_end=40, min_alpha=50):
    """radar"""
    a = alpha_inf
    if t >= t_start and t <= t_end:
        a = min_alpha
    temp = np.ediff1d(
        data[..., t - 1],
        to_end=np.array([a])
    )

    temp = 1 - np.exp(-(temp - alpha_c) / (alpha_v - alpha_c))
    temp[temp < 0] = 0
    return V * temp


def roundabout(data, t, V, alpha_c, alpha_v, radius, eps=1e-4):
    """Function used to model the Jami's roundabout"""
    temp = np.ediff1d(
        data[..., t - 1],
        to_end=np.array([data[0, t-1] - data[-1, t-1]])
    )

    while temp[-1] < -eps:
        temp[-1] += 2 * np.pi * radius

    temp = 1 - np.exp(-(temp - alpha_c) / (alpha_v - alpha_c))
    temp[temp < 0] = 0
    return V * temp
