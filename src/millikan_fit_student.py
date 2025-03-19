import numpy as np
import matplotlib.pyplot as plt


def load_data(filename):

    data = np.loadtxt(filename)
    x = data[:, 0]
    y = data[:, 1]
    return x, y


def calculate_parameters(x, y):

    N = len(x)
    Ex = np.sum(x) / N
    Ey = np.sum(y) / N
    Exx = np.sum(x ** 2) / N
    Exy = np.sum(x * y) / N

    m = (Exy - Ex * Ey) / (Exx - Ex ** 2)
    c = (Exx * Ey - Ex * Exy) / (Exx - Ex ** 2)
    return m, c, Ex, Ey, Exx, Exy


def plot_data_and_fit(x, y, m, c):
    fig = plt.figure()
    plt.scatter(x, y, label='Data Points')
    x_fit = np.linspace(min(x), max(x), 100)#使用 numpy 的 linspace 函数生成一个包含 100 个元素的一维数组 x_fit，元素值从 x 数组的最小值到最大值均匀分布，用于生成拟合直线的横坐标。
    y_fit = m * x_fit + c
    plt.plot(x_fit, y_fit, color='red', label='Fitted Line')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Voltage (V)')
    plt.title('Millikan Data Fitting')
    plt.legend()
    return fig
def calculate_planck_constant(m):
     # 电子电荷
    e = 1.602e-19
    h_actual = 6.626e-34
    h = m * e
    relative_error = abs((h - h_actual) / h_actual) * 100
    return h, relative_error


def main():

    # 数据文件路径
    filename = "millikan.txt"

    # 加载数据
    x, y = load_data(filename)

    # 计算拟合参数
    m, c, Ex, Ey, Exx, Exy = calculate_parameters(x, y)

    # 打印结果
    print(f"Ex = {Ex:.6e}")
    print(f"Ey = {Ey:.6e}")
    print(f"Exx = {Exx:.6e}")
    print(f"Exy = {Exy:.6e}")
    print(f"斜率 m = {m:.6e}")
    print(f"截距 c = {c:.6e}")

    # 绘制数据和拟合直线
    fig = plot_data_and_fit(x, y, m, c)

    # 计算普朗克常量
    h, relative_error = calculate_planck_constant(m)
    print(f"计算得到的普朗克常量 h = {h:.6e} J·s")
    print(f"与实际值的相对误差: {relative_error:.2f}%")

    # 保存图像
    fig.savefig("millikan_fit.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    main()
