import numpy as np

import simulation.euler as simu
import simulation.visualisation as visu
import simulation.ftl as ftl
import simulation.utils as tools


def main():
    RADIUS = 20
    N = 20
    INITIAL = np.array([round((2 * np.pi * RADIUS) / N) * j for j in range(N)])
    STEP = 0.2
    DURATION = 200

    parameters = {
        "V": 15,
        "alpha_c": 3,
        "alpha_v": 20,
        "radius": RADIUS,
        "t_start": 20,
        "t_end": 150,
        "alpha_min": 0,
        "eps": 1e-4,
    }
    callback_parameters = {"eps": 1e-4, "radius": RADIUS}

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(
        INITIAL, ftl.roundabout, parameters, tools.mod_radius, callback_parameters
    )

    visu.anim_roundabout(r, STEP, RADIUS)


def jami_1():
    RADIUS = 14
    N = 10
    INITIAL = np.array([(2 * np.pi * RADIUS) * (j / N) for j in range(N)])
    STEP = 0.2
    DURATION = 30

    parameters = {
        "V": 15,
        "alpha_c": 3,
        "alpha_v": 17,
        "radius": RADIUS,
        "t_start": 10,
        "t_end": 20,
        "alpha_min": 4,
        "eps": 1e-4,
        "alpha_inf": 25,
    }
    callback_parameters = {"eps": 1e-4, "radius": RADIUS}

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(
        INITIAL, ftl.roundabout, parameters, tools.mod_radius, callback_parameters
    )

    visu.anim_roundabout(r, STEP, RADIUS, "jami1.mp4")


def jami_2():
    RADIUS = 14
    N = 15
    INITIAL = np.array([(2 * np.pi * RADIUS) * (j / N) for j in range(N)])
    STEP = 0.2
    DURATION = 100

    parameters = {
        "V": 15,
        "alpha_c": 3,
        "alpha_v": 17,
        "radius": RADIUS,
        "t_start": 10,
        "t_end": 50,
        "alpha_min": 0,
        "eps": 1e-4,
        "alpha_inf": 25,
    }
    callback_parameters = {"eps": 1e-4, "radius": RADIUS}

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(
        INITIAL, ftl.roundabout, parameters, tools.mod_radius, callback_parameters
    )

    visu.anim_roundabout(r, STEP, RADIUS, "jami2.mp4")


def jami_3():
    RADIUS = 14
    N = 22
    INITIAL = np.array([(2 * np.pi * RADIUS) * (j / N) for j in range(N)])
    STEP = 0.2
    DURATION = 100

    parameters = {
        "V": 10,
        "alpha_c": 3,
        "alpha_v": 8,
        "radius": RADIUS,
        "t_start": 10,
        "t_end": 36,
        "alpha_min": 0,
        "eps": 1e-4,
        "alpha_inf": 3.1,
    }
    callback_parameters = {"eps": 1e-4, "radius": RADIUS}

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(
        INITIAL, ftl.roundabout, parameters, tools.mod_radius, callback_parameters
    )

    visu.anim_roundabout(r, STEP, RADIUS)

# main()

# jami_1()
# jami_2()
jami_3()
