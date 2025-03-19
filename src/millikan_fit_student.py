import numpy as np
import matplotlib.pyplot as plt


def load_data(filename):
    """
    加载数据文件
    参数：
    filename : 数据文件名
    返回：
    x : 频率数据数组
    y : 电压数据数组
    """
    try:
        data = np.loadtxt(filename)
        return data[:, 0], data[:, 1]
    except Exception as e:
        raise FileNotFoundError(f"无法加载文件: {filename}") from e


def calculate_parameters(x, y):
    """
    计算最小二乘拟合参数
    参数：
    x : 频率数据数组
    y : 电压数据数组
    返回：
    m : 斜率
    c : 截距
    Ex : x的平均值
    Ey : y的平均值
    Exx : x平方的平均值
    Exy : x和y乘积的平均值
    """
    if len(x) == 0 or len(y) == 0:
        raise ValueError("输入数据不能为空")
    if len(x) != len(y):
        raise ValueError("x和y数组长度必须相同")

    N = len(x)
    Ex = np.mean(x)
    Ey = np.mean(y)
    Exx = np.mean(x ** 2)
    Exy = np.mean(x * y)

    denominator = Exx - Ex ** 2
    if denominator == 0:
        raise ValueError("无法计算参数，分母为零")

    m = (Exy - Ex * Ey) / denominator
    c = (Exx * Ey - Ex * Exy) / denominator

    return m, c, Ex, Ey, Exx, Exy


def plot_data_and_fit(x, y, m, c):
    """
    绘制数据点和拟合直线
    参数：
    x : 频率数据数组
    y : 电压数据数组
    m : 斜率
    c : 截距
    返回：
    fig : 图形对象
    """
    if np.isnan(m) or np.isnan(c):
        raise ValueError("斜率和截距不能为NaN")

    fig, ax = plt.subplots()
    ax.scatter(x, y, label='实验数据')
    y_fit = m * x + c
    ax.plot(x, y_fit, 'r', label='拟合直线')
    ax.set_xlabel('频率 (Hz)')
    ax.set_ylabel('电压 (V)')
    ax.legend()
    return fig


def calculate_planck_constant(m):
    """
    计算普朗克常量
    参数：
    m : 斜率
    返回：
    h : 计算得到的普朗克常量
    relative_error : 相对误差百分比
    """
    if m <= 0:
        raise ValueError("斜率必须为正数")

    e = 1.602e-19  # 电子电荷
    h = m * e
    actual_h = 6.626e-34
    relative_error = abs(h - actual_h) / actual_h * 100
    return h, relative_error


def main():
    """主函数"""
    try:
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

    except Exception as e:
        print(f"程序出错: {str(e)}")


if __name__ == "__main__":
    main()
