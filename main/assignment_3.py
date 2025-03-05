
def euler_method(start, stop, iterations, x, y):
    h = (stop - start) / iterations

    for n in range(0, 10):
        result = y + h * (x - (y ** 2))
        y = result
        x += h
    return result

def runge_kutta_method(start, stop, iterations, x, y):
    h = (stop - start) / iterations

    for n in range(0, 10):
        k_1 = x - (y ** 2)
        t_n = x + (h / 2)
        y_n = y + ((h / 2) * k_1)
        k_2 = t_n - (y_n ** 2)
        y_n = y + ((h / 2) * k_2)
        k_3 = t_n - (y_n ** 2)
        t_n = x + h
        y_n = y + (h * k_3)
        k_4 = t_n - (y_n ** 2)
        result = y + (h / 6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
        y = result
        x += h
    return result