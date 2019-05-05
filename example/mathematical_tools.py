#%% approximation
import numpy as np
from matplotlib.pylab import plt, mpl

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

plt.show()

def f(x):
    return np.sin(x) + 0.5 * x

def create_plot(x, y, styles, labels, axlabels):
    plt.figure(figsize=(10, 6))
    for i in range(len(x)):
        plt.plot(x[i], y[i], styles[i], label=labels[i])
        plt.xlabel(axlabels[0])
        plt.ylabel(axlabels[1])
    plt.legend(loc=0)

x  = np.linspace(-2 * np.pi, 2 * np.pi, 50)
create_plot([x], [f(x)], ['b'], ['f(x)'], ['x', 'f(x)'])

res = np.polyfit(x, f(x), deg=5, full=True)
ry = np.polyval(res[0], x)
create_plot([x, x], [f(x), ry], ['b', 'r.'],
            ['f(x)', 'regression'], ['x', 'f(x)'])

reg = np.polyfit(x, f(x), 7)
ry = np.polyval(reg, x)
np.allclose(f(x), ry)
np.mean((f(x) - ry) ** 2)

matrix = np.zeros((3 + 1, len(x)))
matrix.ndim
matrix[3, :] = x ** 3
matrix[2, :] = x ** 2
matrix[1, :] = x
matrix[0, :] = 1

reg = np.linalg.lstsq(matrix.T, f(x), rcond=None)[0]

reg.round(4)
ry = np.dot(reg, matrix)

create_plot([x, x], [f(x), ry], ['b', 'r.'],
            ['f(x)', 'regression'], ['x', 'f(x)'])

matrix[3, :] = np.sin(x)
reg = np.linalg.lstsq(matrix.T, f(x), rcond=None)[0]
reg.round(4)
ry = np.dot(reg, matrix)
np.allclose(f(x), ry)
np.mean((f(x) - ry) ** 2)
create_plot([x, x], [f(x), ry], ['b', 'r.'],
            ['f(x)', 'regression'], ['x', 'f(x)'])
plt.show()

xn = np.linspace(-2 * np.pi, 2 * np.pi, 50)
xn = xn + 0.15 * np.random.standard_normal(len(xn))
yn = f(xn) + 0.25 * np.random.standard_normal(len(xn))
reg = np.polyfit(xn, yn, 7)
ry = np.polyval(reg, xn)
create_plot([x, x], [f(x), ry], ['b', 'r.'],
            ['f(x)', 'regression'], ['x', 'f(x)'])

xu = np.random.randn(50) * 4 * np.pi - 2 * np.pi
yu = f(xu)

print(xu[:10].round(2))
print(yu[:10].round(2))

reg = np.polyfit(xu, yu, 5)
ry = np.polyval(reg, xu)
create_plot([xu, xu], [f(xu), ry], ['b.', 'ro'],
            ['f(x)', 'regression'], ['x', 'f(x)'])
plt.show()

def fm(p):
    x, y = p
    return np.sin(x) + 0.25 * x + np.sqrt(y) + 0.05 * y ** 2

x = np.linspace(0, 10, 20)
y = np.linspace(0, 10, 20)
X, Y = np.meshgrid(x, y)