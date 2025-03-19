import numpy as np
import matplotlib.pyplot as plt


def load_data(filename):
    """
    加载数据文件
    :param filename: 数据文件的路径
    :return: 数据的x和y值
    """
    try:
        data = np.loadtxt(filename)
        return data[:, 0], data[:, 1]
    except FileNotFoundError:
        print(f"错误: 文件 {filename} 未找到。")
        raise
    except Exception as e:
        print(f"错误: 加载文件 {filename} 时出现问题: {e}")
        raise
        
def calculate_parameters(x, y):
    """
    计算最小二乘拟合参数
    :param x: 自变量数组
    :param y: 因变量数组
    :return: 斜率m、截距c、Ex、Ey、Exx、Exy
    """
    if len(x) == 0 or len(y) == 0:
        raise ValueError("输入数据不能为空。")
    if len(x) != len(y):
        raise ValueError("x和y数组长度必须相同。")

    N = len(x)
    Ex = np.mean(x)
    Ey = np.mean(y)
    Exx = np.mean(x ** 2)
    Exy = np.mean(x * y)

    denominator = Exx - Ex ** 2
    if denominator == 0:
        raise ValueError("无法计算参数，分母为零。")

    m = (Exy - Ex * Ey) / denominator
    c = (Exx * Ey - Ex * Exy) / denominator
    return m, c, Ex, Ey, Exx, Exy
    
def plot_data_and_fit(x, y, m, c):
    """
    绘制数据点和拟合直线
    :param x: 自变量数组
    :param y: 因变量数组
    :param m: 拟合直线的斜率
    :param c: 拟合直线的截距
    :return: 绘制的图形对象
    """
    if np.isnan(m) or np.isnan(c):
        raise ValueError("斜率和截距不能为NaN。")

    fig, ax = plt.subplots()
    ax.scatter(x, y, label='experimental data')
    y_fit = m * x + c
    ax.plot(x, y_fit, 'r', label='fitted line')
    ax.set_xlabel('(Hz)')
    ax.set_ylabel('(V)')
    ax.legend()
    return fig
    
def calculate_planck_constant(m):
    """
    计算普朗克常量
    :param m: 拟合直线的斜率
    :return: 计算得到的普朗克常量h和相对误差
    """
    if m <= 0:
        raise ValueError("斜率必须为正数。")

    e = 1.602e-19  # 电子电荷
    h = m * e
    actual_h = 6.626e-34
    relative_error = abs(h - actual_h) / actual_h * 100
    return h, relative_error

def print_results(Ex, Ey, Exx, Exy, m, c, h, relative_error):
    """
    打印计算结果
    :param Ex: x的均值
    :param Ey: y的均值
    :param Exx: x平方的均值
    :param Exy: x*y的均值
    :param m: 拟合直线的斜率
    :param c: 拟合直线的截距
    :param h: 计算得到的普朗克常量
    :param relative_error: 相对误差
    """
    print(f"Ex = {Ex:.6e}")
    print(f"Ey = {Ey:.6e}")
    print(f"Exx = {Exx:.6e}")
    print(f"Exy = {Exy:.6e}")
    print(f"斜率 m = {m:.6e}")
    print(f"截距 c = {c:.6e}")
    print(f"计算得到的普朗克常量 h = {h:.6e} J·s")
    print(f"与实际值的相对误差: {relative_error:.2f}%")
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
        h, relative_error = calculate_planck_constant(m)
        print_results(Ex, Ey, Exx, Exy, m, c, h, relative_error)

        # 绘制数据和拟合直线
        fig = plot_data_and_fit(x, y, m, c)

        # 保存图像
        fig.savefig("millikan_fit.png", dpi=300)
        plt.show()

    except Exception as e:
        print(f"程序出错: {str(e)}")


if __name__ == "__main__":
    main()
