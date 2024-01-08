import numpy as np

import simulation.euler as simu
import simulation.visualisation as visu
import simulation.utils as tools
import simulation.ftl as ftl


def traffic_jam():
    N = 50
    ALPHA_INF = 0

    STEP = 0.02
    DURATION = 240

    MAX_VEL = 42
    ALPHA_C = 4
    ALPHA_V = 70

    INITIAL = np.array([ALPHA_V * 2 * j for j in range(N)])

    parameters = {
        "V": MAX_VEL,
        "alpha_c": ALPHA_C,
        "alpha_v": ALPHA_V,
        "alpha_inf": ALPHA_INF,
    }

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(INITIAL, ftl.lead_constant, parameters)

    name = str(N) + "-"
    for k, v in parameters.items():
        name += str(k) + str(v) + "-"

    visu.classic_view(r, STEP, "position" + name + ".png")
    visu.distance_view(r, STEP, "distance" + name + ".png")
    visu.velocity_view(r, STEP, "velocity" + name + ".png")


def traffic_jam_10_cars():
    N = 15

    STEP = 0.02
    DURATION = 45

    INITIAL = np.array([30 * 2 * j for j in range(N)])

    parameters = {"V": 18, "alpha_c": 6, "alpha_v": 30, "alpha_inf": 0}

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(INITIAL, ftl.lead_constant, parameters)

    name = str(N) + "-"
    for k, v in parameters.items():
        name += str(k) + str(v) + "-"

    visu.position_versus_time_scatter(r, STEP, 10, "traffic-at-10-time" + name + ".png")
    visu.classic_view(r, STEP, "position" + name + ".png")
    visu.distance_view(r, STEP, "distance" + name + ".png")
    # visu.velocity_view(r, STEP) #"velocity" + name + ".png")


def huge_traffic_jam():
    N = 1500
    ALPHA_INF = 0

    STEP = 0.2
    DURATION = 3600

    MAX_VEL = 57
    ALPHA_C = 6
    ALPHA_V = 70

    INITIAL = np.array([ALPHA_V * j for j in range(N)])

    parameters = {
        "V": MAX_VEL,
        "alpha_c": ALPHA_C,
        "alpha_v": ALPHA_V,
        "alpha_inf": ALPHA_INF,
    }

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(INITIAL, ftl.lead_constant, parameters)

    name = str(N) + "-"
    for k, v in parameters.items():
        name += str(k) + str(v) + "-"

    visu.density_heatmap(
        r, STEP, 100, ALPHA_C
    )  # "traffic-jam-density-" + name + ".jpg")
    # visu.distance_heatmap(r, STEP, "traffic-jam-distance-" + name + ".jpg")
    # visu.density_heatmap(r, STEP, 100, ALPHA_C) # "traffic-jam-density-" + name + ".jpg")
    # visu.display_density(r, STEP, 500, ALPHA_C)


def main_accident():
    ALPHA_INF = 300

    STEP = 0.2
    DURATION = 1200

    MAX_VEL = 37
    ALPHA_C = 6
    ALPHA_V = 70

    N = 200
    INITIAL = np.array([80 * j for j in range(N)])

    parameters_130 = {
        "V": MAX_VEL,
        "alpha_c": ALPHA_C,
        "alpha_v": ALPHA_V,
        "alpha_inf": ALPHA_INF,
        "t_start": 20,
        "t_end": 210,
        "step": STEP,
        "alpha_min": 70,
    }

    parameters_110_70 = {
        "V": 35,
        "alpha_c": ALPHA_C,
        "alpha_v": 70,
        "alpha_inf": 150,
        "t_start": 10,
        "t_end": 190,
        "step": STEP,
        "alpha_min": 91,
    }

    m = simu.EulerMethod(DURATION, STEP)

    for p in [parameters_130, parameters_110_70]:
        r = m.compute(INITIAL, ftl.accident, p)
        # print(tools.mean_velocity(r, STEP))
        visu.distance_heatmap(r, STEP)
        # visu.density_heatmap(r, STEP, 90, ALPHA_C)


main_accident()
