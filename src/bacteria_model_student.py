import numpy as np
import matplotlib.pyplot as plt

# 定义V(t)函数，表示模型V(t) = 1 - e^{-t/τ}
def V(t, tau):
    """
    计算V(t)的值，V(t) = 1 - e^{-t/τ}
    参数：
    t : 时间数组
    tau : 时间常数τ
    返回：
    V(t)的值
    """
    return 1 - np.exp(-t / tau)

# 定义W(t)函数，表示模型W(t) = A*(e^{-t/τ} - 1 + t/τ)
def W(t, A, tau):
    """
    计算W(t)的值，W(t) = A*(e^{-t/τ} - 1 + t/τ)
    参数：
    t : 时间数组
    A : 参数A
    tau : 时间常数τ
    返回：
    W(t)的值
    """
    return A * (np.exp(-t / tau) - 1 + t / tau)

# 定义加载Novick实验数据的函数
def load_novick_data(filename):
    """
    加载Novick实验数据
    参数：
    filename : 数据文件名
    返回：
    time_data : 时间数据数组
    value_data : 对应的测量值数组
    """
    try:
        # 尝试使用逗号作为分隔符加载数据
        data = np.loadtxt(filename, delimiter=',')
        time_data = data[:, 0]
        value_data = data[:, 1]
    except ValueError:
        # 如果加载失败，尝试使用更鲁棒的方法处理
        print(f"Error loading file {filename}. Trying alternative method.")
        # 使用 genfromtxt 处理可能的缺失值或格式问题
        data = np.genfromtxt(filename, delimiter=',', dtype=None, encoding=None)
        # 转换为浮点数数组
        time_data = np.array([float(row[0]) for row in data])
        value_data = np.array([float(row[1]) for row in data])
    return time_data, value_data

# 定义绘制模型曲线和实验数据点的函数
def plot_models_and_data():
    """
    绘制模型曲线和实验数据点
    """
    # 时间范围0到2，用于绘制W(t)
    t = np.linspace(0, 2, 100)

    # 创建一个新的图形，设置大小为10x6英寸
    plt.figure(figsize=(10, 6))

    # 绘制A=1, τ=1的W(t)曲线
    plt.plot(t, W(t, 1, 1), label='W(t) A=1, τ=1', color='blue')

    # 定义不同的参数组合，用于绘制多条W(t)曲线
    parameters = [
        (0.5, 1, 'green', '--', 'W1: A=0.5, τ=1'),
        (1, 0.5, 'red', '-.', 'W2: A=1, τ=0.5'),
        (1.5, 2, 'purple', ':', 'W3: A=1.5, τ=2')
    ]

    # 遍历参数组合，绘制每条曲线
    for A, tau, color, linestyle, label in parameters:
        plt.plot(t, W(t, A, tau), color=color, linestyle=linestyle, label=label)

    # 添加图例、标题和轴标签
    plt.legend()
    plt.title('W(t) Model Curves')
    plt.xlabel('Time (t)')
    plt.ylabel('W(t)')
    plt.grid(True)

    # 尝试加载并绘制Novick实验数据
    try:
        time_data, value_data = load_novick_data('g149novickA.txt')
        plt.scatter(time_data, value_data, color='black', marker='o', label='Experimental Data')
    except Exception as e:
        print(f"Error loading or plotting data: {e}")

    # 设置合理τ值进行拟合，这里以τ=2为例
    tau_fit = 2
    plt.plot(t, V(t, tau_fit), label=f'V(t) τ={tau_fit}', color='orange', linestyle='--')

    # 添加图例和其他选项
    plt.legend()
    plt.title('Model Curves and Experimental Data')
    plt.xlabel('Time (t)')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()

    # 处理g149novickB.csv数据，截取时间小于等于10小时的数据
    try:
        time_data_b, value_data_b = load_novick_data('g149novickB.csv')
        mask = time_data_b <= 10
        time_data_b = time_data_b[mask]
        value_data_b = value_data_b[mask]

        # 创建一个新的图形，设置大小为10x6英寸
        plt.figure(figsize=(10, 6))

        # 绘制截取后的数据点
        plt.scatter(time_data_b, value_data_b, color='black', marker='o', label='Experimental Data (t<=10)')

        # 根据提示估计A和τ的初始值，并绘制拟合曲线
        A_fit = 0.8
        tau_fit = 1.5
        plt.plot(t, W(t, A_fit, tau_fit), label=f'W(t) Fit: A={A_fit}, τ={tau_fit}', color='green')

        # 添加图例和其他选项
        plt.legend()
        plt.title('W(t) Fit to Experimental Data (t<=10)')
        plt.xlabel('Time (t)')
        plt.ylabel('Value')
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error loading or plotting data for part b: {e}")

# 如果直接运行此脚本，则执行plot_models_and_data函数
if __name__ == "__main__":
    plot_models_and_data()
