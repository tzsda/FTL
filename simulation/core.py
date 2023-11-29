import math


def compute_alpha(max_velocity, wished_velocity, alpha_c, alpha_v):
    assert wished_velocity < max_velocity
    return -alpha_c + (alpha_c - alpha_v) * math.log(1 - wished_velocity / max_velocity)
