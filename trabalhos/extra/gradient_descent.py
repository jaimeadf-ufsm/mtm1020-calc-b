import matplotlib.pyplot as plt
import numpy as np
import sympy

from matplotlib import cm
from matplotlib.widgets import Slider
print('Digite a função f(x, y):')
f = sympy.sympify(input())

print('Digite o chute inicial (x0, y0):')
x0, y0 = map(float, input().split())

print('Digite o início, o fim e a quantidade de pontos para os eixos:')
axis_start, axis_end, axis_points = map(float, input().split())

fx = sympy.diff(f, 'x')
fy = sympy.diff(f, 'y')

print(f'f(x, y) = {f}')
print(f'fx = {fx}, fy = {fy}')

plt.style.use('bmh')

figure, ax = plt.subplots(subplot_kw={'projection': '3d'})
figure.subplots_adjust(bottom=0.28)
ax.axes.set_aspect('equal')

x_space = np.linspace(axis_start, axis_end, int(axis_points))
y_space = np.linspace(axis_start, axis_end, int(axis_points))

x_mesh, y_mesh = np.meshgrid(x_space, y_space)

f_lambda = sympy.lambdify(('x', 'y'), f, 'numpy')

surface = ax.plot_surface(x_mesh, y_mesh, f_lambda(x_mesh, y_mesh), cmap=cm.viridis, alpha=0.5)
point, = ax.plot([x0], [y0], [f_lambda(x0, y0)], 'ro')

axes_iteration = figure.add_axes([0.2, 0.15, 0.6, 0.03])
axes_step = figure.add_axes([0.2, 0.1, 0.6, 0.03])

def update(_):
    x = x0
    y = y0

    for i in range(int(iteration.val)):
        x -= float(step.val * fx.subs({'x': x, 'y': y}))
        y -= float(step.val * fy.subs({'x': x, 'y': y}))

    point.set_data([x], [y])
    point.set_3d_properties([f_lambda(x, y)])

    figure.canvas.draw_idle()

iteration = Slider(axes_iteration, 'Iteration', 0, 100, valinit=0, valstep=1)
step = Slider(axes_step, 'Step', 0.01, 1, valinit=0.01, valstep=0.01)

iteration.on_changed(update)
step.on_changed(update)

plt.show()