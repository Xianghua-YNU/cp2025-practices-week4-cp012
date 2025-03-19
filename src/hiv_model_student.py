import numpy as np
import matplotlib.pyplot as plt

# 定义HIV模型类
class HIVModel:
    # 初始化方法，设置模型参数
    def __init__(self, A, alpha, B, beta):
        self.A = A          # 参数A，表示病毒载量的初始值
        self.alpha = alpha  # 参数alpha，表示病毒载量衰减的速率
        self.B = B          # 参数B，表示另一个病毒载量的初始值
        self.beta = beta    # 参数beta，表示另一个病毒载量衰减的速率

    # 计算病毒载量的方法
    def viral_load(self, time):
        # 病毒载量公式：V(t) = A * exp(-alpha * t) + B * exp(-beta * t)
        # time是时间数组，返回对应时间点的病毒载量值
        return self.A * np.exp(-self.alpha * time) + self.B * np.exp(-self.beta * time)

    # 绘制模型曲线的方法
    def plot_model(self, time):
        # 计算模型的病毒载量
        viral_load = self.viral_load(time)
        # 绘制曲线，label用于图例显示模型参数
        plt.plot(time, viral_load, label=f'Model: A={self.A}, alpha={self.alpha}, B={self.B}, beta={self.beta}')
        # 设置x轴标签为时间（天）
        plt.xlabel('Time (days)')
        # 设置y轴标签为病毒载量
        plt.ylabel('Viral Load')
        # 设置图表标题
        plt.title('HIV Viral Load Model')
        # 显示图例
        plt.legend()
        # 添加网格
        plt.grid(True)

# 定义加载HIV数据的函数
def load_hiv_data(filepath):
    # 使用numpy的loadtxt函数加载CSV文件，delimiter指定分隔符为逗号
    data = np.loadtxt(filepath, delimiter=',')
    # 获取第一列作为时间数据
    time_data = data[:, 0]
    # 获取第二列作为病毒载量数据
    viral_data = data[:, 1]
    # 返回时间和病毒载量数据
    return time_data, viral_data

# 主函数
def main():
    # 设置模型参数
    A = 1000    # 参数A的值
    alpha = 0.05  # 参数alpha的值
    B = 200     # 参数B的值
    beta = 0.5   # 参数beta的值

    # 加载实验数据，假设数据文件名为'HIVseries.csv'
    time_data, viral_data = load_hiv_data('HIVseries.csv')

    # 生成模型时间点，从实验数据的最小时间到最大时间，生成100个等间距的时间点
    time_model = np.linspace(min(time_data), max(time_data), 100)

    # 创建HIV模型实例，传入参数A, alpha, B, beta
    model = HIVModel(A, alpha, B, beta)

    # 调用模型的plot_model方法绘制模型曲线，传入生成的时间点
    model.plot_model(time_model)

    # 绘制实验数据点，使用红色散点图，label用于图例显示实验数据
    plt.scatter(time_data, viral_data, color='red', label='Experimental Data')

    # 显示图表
    plt.show()

    # 计算并打印1/alpha的值，单位为天
    print(f"1/alpha = {1/alpha} days")

# 如果直接运行此脚本，则执行main函数
if __name__ == "__main__":
    main()
