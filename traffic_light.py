import numpy as np

import simulation.euler as simu
import simulation.visualisation as visu
import simulation.ftl as ftl


def twenty_five_cars():
    N = 25
    INITIAL = np.array([4 * j for j in range(N)])
    DURATION = 100

    parameters = {"V": 16, "alpha_c": 4, "alpha_v": 30, "alpha_inf": 60}

    STEP = 0.02

    name = str(N) + "-"
    for k, v in parameters.items():
        name += str(k) + str(v) + "-"

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(INITIAL, ftl.lead_constant, parameters)

    visu.classic_view(r, STEP, output="position" + name + ".png")
    visu.distance_view(r, STEP, output="gap" + name + ".png")
    visu.velocity_view(r, STEP, output="velocity" + name + ".png")

    col = -1

    counter = 0
    for i in range(N):
        if r[i, col] >= N * 4:
            counter += 1
    print(counter)


def fifty_cars():
    N = 2 * 25
    INITIAL = np.array([4 * j for j in range(N)])
    DURATION = 100

    parameters = {"V": 16, "alpha_c": 4, "alpha_v": 30, "alpha_inf": 60}

    STEP = 0.02

    name = str(N) + "-"
    for k, v in parameters.items():
        name += str(k) + str(v) + "-"

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(INITIAL, ftl.lead_constant, parameters)

    visu.classic_view(r, STEP, output="position" + name + ".png")
    visu.distance_view(r, STEP, output="gap" + name + ".png")
    visu.velocity_view(r, STEP, output="velocity" + name + ".png")

    col = -1

    counter = 0
    for i in range(N):
        if r[i, col] >= N * 4:
            counter += 1
    print(counter)


def end_huge_traffic_jam():
    N = 1000
    ALPHA_INF = 140

    STEP = 0.2
    DURATION = 3600

    MAX_VEL = 42
    ALPHA_C = 4
    ALPHA_V = 70

    INITIAL = np.array([ALPHA_C * j for j in range(N)])

    parameters = {
        "V": MAX_VEL,
        "alpha_c": ALPHA_C,
        "alpha_v": ALPHA_V,
        "alpha_inf": ALPHA_INF,
    }

    name = str(N) + "-"
    for k, v in parameters.items():
        name += str(k) + str(v) + "-"

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(INITIAL, ftl.lead_constant, parameters)

    print("fin calcul")

    # visu.velocity_heatmap(r, STEP, "end-traffic-jam-velocity-" + name + ".jpg")
    # visu.density_heatmap(r, STEP, 100, ALPHA_C)
    visu.display_density(r, STEP, 500, ALPHA_C)


end_huge_traffic_jam()
