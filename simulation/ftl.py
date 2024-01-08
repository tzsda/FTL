import numpy as np


def lead_constant(data, t, V, alpha_c, alpha_v, alpha_inf):
    """Function used to model a start at green light"""
    temp = np.ediff1d(data[..., t - 1], to_end=np.array([alpha_inf]))
    temp = 1 - np.exp(-(temp - alpha_c) / (alpha_v - alpha_c))
    temp[temp < 0] = 0
    return V * temp


def accident(
    data,
    t,
    step,
    V=30,
    alpha_c=10,
    alpha_v=40,
    alpha_inf=60,
    t_start=10,
    t_end=100,
    alpha_min=50,
):
    """accident"""
    temp = np.ediff1d(data[..., t - 1], to_end=np.array([alpha_inf]))

    if t * step >= t_start and t * step <= t_end:
        temp[-1] = alpha_min

    temp = 1 - np.exp(-(temp - alpha_c) / (alpha_v - alpha_c))
    temp[temp < 0] = 0
    return V * temp


def roundabout(
    data,
    t,
    V,
    alpha_c,
    alpha_v,
    radius,
    step,
    t_start=20,
    t_end=40,
    alpha_min=12,
    alpha_inf=20,
    eps=1e-4,
):
    """Function used to model the Jami's roundabout"""
    temp = np.ediff1d(
        data[..., t - 1], to_end=np.array([data[0, t - 1] - data[-1, t - 1]])
    )

    while temp[-1] < -eps:
        temp[-1] += 2 * np.pi * radius

    if t * step >= t_start and t * step <= t_end:
        if temp[-1] > alpha_min - eps:
            temp[-1] = alpha_min
    else:
        if temp[-1] > alpha_inf - eps:
            temp[-1] = alpha_inf

    temp = 1 - np.exp(-(temp - alpha_c) / (alpha_v - alpha_c))
    temp[temp < 0] = 0
    return V * temp
