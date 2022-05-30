import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ui_Dialog import Ui_Dialog


# 创建对话框类 并继承UI类
class QmyDialog(QWidget, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)  # 构造UI

    # 计算总价按钮
    def on_btnCalculate_clicked(self):
        num = int(self.ui.editCount.text())  # 获取输入框值
        price = float(self.ui.editPrice.text())
        self.ui.editTotal.setText("%.2f" % (num * price))  # 设置输入框值

    # 数量变化事件
    @pyqtSlot(int)
    def on_spinCount_valueChanged(self, count):  # 变化后的值 count
        price = self.ui.spinPrice.value()  # 获取值
        self.ui.spinTotal.setValue(price * count)  # 设置值

    # 价格变化事件
    @pyqtSlot(float)
    def on_spinPrice_valueChanged(self, price):  # 变化后的值 price
        count = self.ui.spinCount.value()  # 获取值
        self.ui.spinTotal.setValue(price * count)  # 设置值


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = QmyDialog()
    main_form.show()

    sys.exit(app.exec_())
