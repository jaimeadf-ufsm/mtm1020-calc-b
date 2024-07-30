import matplotlib.pyplot as plt
import numpy as np
import sympy

from matplotlib import cm
from matplotlib.widgets import Slider
print('Digite a função f(x, y):')
f = sympy.sympify(input())

print('Digite o chute inicial (x0, y0):')
x0, y0 = map(float, input().split())

print('Digite o início, o fim e a quantidade de pontos para os eixos X e Y:')
xy_axes_start, xy_axes_end, xy_axes_points = map(float, input().split())

print('Digite o início e o fim para o eixo Z:')
z_axis_start, z_axis_end = map(float, input().split())

fx = sympy.diff(f, 'x')
fy = sympy.diff(f, 'y')

print(f'f(x, y) = {f}')
print(f'x0 = {x0}, y0 = {y0}')
print()
print(f'fx = {fx}, fy = {fy}')

f_lambda = sympy.lambdify(('x', 'y'), f, 'numpy')

plt.style.use('bmh')

figure, ax = plt.subplots(1, 1, figsize=(10, 8), subplot_kw={'projection': '3d'})
figure.subplots_adjust(bottom=0.28)

ax.set_xlim([xy_axes_start, xy_axes_end])
ax.set_ylim([xy_axes_start, xy_axes_end])
ax.set_zlim([z_axis_start, z_axis_end])

x_space = np.linspace(xy_axes_start, xy_axes_end, int(xy_axes_points))
y_space = np.linspace(xy_axes_start, xy_axes_end, int(xy_axes_points))

x_mesh, y_mesh = np.meshgrid(x_space, y_space)

z_mesh = f_lambda(x_mesh, y_mesh)

z1_mesh = np.ma.masked_where((z_mesh < z_axis_start) | (z_mesh > z_axis_end), z_mesh)

x1_mesh = np.ma.masked_where(z1_mesh.mask, x_mesh)
y1_mesh = np.ma.masked_where(z1_mesh.mask, y_mesh)

surface = ax.plot_surface(x1_mesh, y1_mesh, z1_mesh, alpha=0.5, cmap=cm.viridis, edgecolor='none')

previous_points, = ax.plot([], [], 'yo')
current_points, = ax.plot(x0, y0, f_lambda(x0, y0), 'ro')

axes_iteration = figure.add_axes([0.2, 0.15, 0.6, 0.03])
axes_step = figure.add_axes([0.2, 0.1, 0.6, 0.03])

def update(_):
    x = x0
    y = y0

    x_data = []
    y_data = []

    for i in range(int(iteration.val)):
        x_data.append(x)
        y_data.append(y)

        x -= float(step.val * fx.subs({'x': x, 'y': y}))
        y -= float(step.val * fy.subs({'x': x, 'y': y}))

    previous_points.set_data(x_data, y_data)
    previous_points.set_3d_properties([f_lambda(x, y) for x, y in zip(x_data, y_data)])

    current_points.set_data([x], [y])
    current_points.set_3d_properties([f_lambda(x, y)])

    figure.canvas.draw_idle()

iteration = Slider(axes_iteration, 'Iteration', 0, 100, valinit=0, valstep=1)
step = Slider(axes_step, 'Step', 0.01, 1, valinit=0.01, valstep=0.01)

iteration.on_changed(update)
step.on_changed(update)

plt.show()