import numpy as np
import matplotlib.pyplot as plt


# 定义细菌模型类
class BacteriaModel:
    # 初始化方法，设置模型参数A和tau
    def __init__(self, A, tau):
        self.A = A  # 参数A
        self.tau = tau  # 参数tau

    # 定义V(t)模型，V(t) = 1 - e^{-t/tau}
    def v_model(self, t):
        return 1 - np.exp(-t / self.tau)

    # 定义W(t)模型，W(t) = A*(e^{-t/tau} - 1 + t/tau)
    def w_model(self, t):
        return self.A * (np.exp(-t / self.tau) - 1 + t / self.tau)

    # 绘制模型曲线的方法
    def plot_models(self, t):
        # 计算V(t)和W(t)的值
        v = self.v_model(t)
        w = self.w_model(t)

        # 绘制V(t)和W(t)曲线
        plt.plot(t, v, label='V(t)')
        plt.plot(t, w, label='W(t)')
        plt.xlabel('Time')  # 设置x轴标签
        plt.ylabel('Response')  # 设置y轴标签
        plt.title('Bacteria Growth Models')  # 设置图表标题
        plt.legend()  # 显示图例
        plt.show()  # 显示图表


# 定义加载细菌数据的函数
def load_bacteria_data(filepath):
    try:
        # 尝试加载数据，假设数据文件中有两列，分别为时间(time)和响应(response)
        data = np.loadtxt(filepath, delimiter=',')
        # 返回时间和响应数据
        return data[:, 0], data[:, 1]
    except:
        # 如果加载失败，尝试其他方式加载数据
        return np.loadtxt(filepath, delimiter=',', unpack=True)


# 主函数
def main():
    # 初始化模型参数，创建BacteriaModel实例
    model = BacteriaModel(A=1.0, tau=2.0)

    # 生成时间序列，从0到10，共100个点
    t = np.linspace(0, 10, 100)

    # 绘制模型曲线
    model.plot_models(t)

    # 加载实验数据
    time_data, response_data = load_bacteria_data('data/g149novickA.txt')

    # 绘制实验数据点
    plt.scatter(time_data, response_data, label='Experimental Data', color='red')
    plt.legend()  # 显示图例
    plt.xlabel('Time')  # 设置x轴标签
    plt.ylabel('Response')  # 设置y轴标签
    plt.title('Bacteria Growth Models with Experimental Data')  # 设置图表标题
    plt.grid(True)  # 添加网格
    plt.show()  # 显示图表


# 如果直接运行此脚本，则执行main函数
if __name__ == "__main__":
    main()
