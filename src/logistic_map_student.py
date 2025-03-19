import numpy as np
import matplotlib.pyplot as plt


def iterate_logistic(r, x0, n):
    """
    迭代Logistic映射

    参数:
        r: 增长率参数
        x0: 初始值
        n: 迭代次数

    返回:
        x: 迭代序列数组
    """
    x = np.zeros(n)
    x[0] = x0
    for i in range(1, n):
        x[i] = r * x[i - 1] * (1 - x[i - 1])
    return x


def plot_time_series(r, x0, n):
    """
    绘制时间序列图

    参数:
        r: 增长率参数
        x0: 初始值
        n: 迭代次数

    返回:
        fig: matplotlib图像对象
    """
    x = iterate_logistic(r, x0, n)
    t = np.arange(n)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(t, x, 'b-', lw=1)
    ax.set_xlabel('迭代次数')
    ax.set_ylabel('x')
    ax.set_title(f'Logistic映射时间序列 (r={r})')
    ax.grid(True)

    return fig


def plot_bifurcation(r_min, r_max, n_r, n_iterations, n_discard):
    """
    绘制分岔图

    参数:
        r_min: r的最小值
        r_max: r的最大值
        n_r: r的取值个数
        n_iterations: 每个r值的迭代次数
        n_discard: 每个r值丢弃的初始迭代点数

    返回:
        fig: matplotlib图像对象
    """
    r = np.linspace(r_min, r_max, int((r_max - r_min) / 0.001))
    x = np.zeros(n_iterations)
    x_plot = []
    r_plot = []

    for r_val in r:
        x[0] = 0.5
        for i in range(1, n_iterations):
            x[i] = r_val * x[i - 1] * (1 - x[i - 1])

        # 只保留稳定后的点
        x_plot.extend(x[n_discard:])
        r_plot.extend([r_val] * (n_iterations - n_discard))

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(r_plot, x_plot, s=0.1, color='black')
    ax.set_xlabel('r')
    ax.set_ylabel('x')
    ax.set_title('Logistic映射分岔图')

    return fig


# 任务1：Logistic模型的迭代
r_values = [2, 3.2, 3.45, 3.6]
x0 = 0.5
n_iterations = 60

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for i, r in enumerate(r_values):
    x = iterate_logistic(r, x0, n_iterations)
    axes[i].plot(range(n_iterations), x)
    axes[i].set_title(f'r = {r}')
    axes[i].set_xlabel('迭代次数')
    axes[i].set_ylabel('x')

    if r == 2:
        conclusion = "没有分岔"
    elif r == 3.2:
        conclusion = "周期2分岔"
    elif r == 3.45:
        conclusion = "周期4分岔"
    elif r == 3.6:
        conclusion = "混沌"

    axes[i].text(0.5, -0.1, conclusion, transform=axes[i].transAxes, ha='center')

plt.tight_layout()
plt.show()

# 任务2：费根鲍姆图的绘制
r_min = 2.6
r_max = 4
n_iterations = 250
n_discard = 100

fig = plot_bifurcation(r_min, r_max, int((r_max - r_min) / 0.001), n_iterations, n_discard)
plt.show()

# 分析费根鲍姆图
print("费根鲍姆图分析：")
print("固定点：在某些r值下，x只有一个稳定的值，表现为图中垂直方向上的一个点。")
print("有限循环：在某些r值下，x在几个固定的值之间循环，表现为图中垂直方向上的几个离散点。")
print("混沌：在某些r值下，x的值没有明显的规律，表现为图中垂直方向上的一片密集的点。")

# 确定混沌边界
chaos_boundary = 3.57
print(f"估计的混沌边界: r = {chaos_boundary}")
