import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# 画sin曲线
fig = plt.figure(tight_layout=True)

# 设置坐标轴范围
plt.xlim((-1, 7))
plt.ylim((-2, 2))

# 画动点
point_ani, = plt.plot(x[3], y[10], "r-")  # 必须有,，表示得到元组
text_pt = plt.text(3.5, 0.8, '', fontsize=16)


def update(num):
    '''更新数据点
    .set_data()的意思是将这里的(x[num], y[num])代替上面的(x[0], y[0])
    也可以.set_ydata,需要将上面的x[0]改成x,这里的x[num]去掉
    '''
    xx = np.linspace(0, 2 * np.pi * num / 100, num)
    yy = np.sin(xx)
    point_ani.set_data(xx, yy)
    # text_pt.set_position([num], y[num])#更新文本位置
    text_pt.set_text("x=%.3f, y=%.3f" % (x[num], y[num]))
    return point_ani, text_pt,


# 开始制作动画
ani = animation.FuncAnimation(fig=fig, func=update, frames=np.arange(0, 100),
                              interval=80, blit=True)

# ani.save('sin.gif', writer='imagegick', fps=10)
plt.show()
