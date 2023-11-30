import math


def compute_alpha(max_velocity, wished_velocity, alpha_c, alpha_v):
    assert wished_velocity < max_velocity
    return -alpha_c + (alpha_c - alpha_v) * math.log(1 - wished_velocity / max_velocity)


def compute_brake_rate(max_velocity):
    magnitude = 10 ** math.floor(math.log10((max_velocity // 10) * 6))
    return  math.log(2) / (magnitude ** 2)
