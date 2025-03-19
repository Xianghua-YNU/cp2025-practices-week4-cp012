import numpy as np
import matplotlib.pyplot as plt


def logistic_iteration(r, x0, num_iterations):
    x = np.zeros(num_iterations)
    x[0] = x0
    for i in range(1, num_iterations):
        x[i] = r * x[i - 1] * (1 - x[i - 1])
    return x


x0 = 0.5
num_iterations = 60
r_values = [2, 3.2, 3.45, 3.6]

plt.figure(figsize=(12, 8))

for i, r in enumerate(r_values):
    x = logistic_iteration(r, x0, num_iterations)
    plt.subplot(2, 2, i + 1)
    plt.plot(range(num_iterations), x)
    plt.title(f'r = {r}')
    plt.xlabel('迭代次数')
    plt.ylabel('x')

    if r == 2:
        conclusion = "没有分岔"
    elif r == 3.2:
        conclusion = "周期2分岔"
    elif r == 3.45:
        conclusion = "周期4分岔"
    elif r == 3.6:
        conclusion = "混沌"
    else:
        conclusion = "未知行为"
    plt.text(0.5, -0.1, conclusion, transform=plt.gca().transAxes, ha='center')
# 设置参数
r_min = 2.6
r_max = 4
step = 0.001
x0 = 0.5
total_iterations = 250
transient_iterations = 100
record_iterations = total_iterations - transient_iterations
    # 初始化存储结果的列表
r_values = np.arange(r_min, r_max, step)
x_values = []
# 对每个 r 值进行迭代
for r in r_values:
    x = logistic_iteration(r, x0, total_iterations)
    # 记录后 150 次迭代的值
    x_values.extend([(r, x_val) for x_val in x[transient_iterations:]])
# 分离 r 和 x 坐标
r_coords, x_coords = zip(*x_values)
# zip(*x_values)：使用 zip 函数的解包操作，将 x_values 列表中的元组 (r, x_val) 解包，分别提取出所有的 r 值和 x 值。
# r_coords, x_coords = ...：将提取出的 r 值和 x 值分别赋值给 r_coords 和 x_coords 变量。
# 绘制费根鲍姆图
plt.figure(figsize=(10, 6))
plt.scatter(r_coords, x_coords, s=0.1, c='black')
plt.xlabel('r')
plt.ylabel('x')
plt.title('费根鲍姆图')
plt.show()
chaos_boundary = 3.57
print(f"估计的混沌边界: r = {chaos_boundary}")

plt.tight_layout()
plt.show()
