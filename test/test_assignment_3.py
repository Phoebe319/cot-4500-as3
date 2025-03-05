from main.assignment_3 import euler_method, runge_kutta_method

euler_result = euler_method(0, 2, 10, 0, 1)
print(euler_result)

runge_kutta_result = runge_kutta_method(0, 2, 10, 0, 1)
print(runge_kutta_result)