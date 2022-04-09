"""自己设计一个计算器，能够实现加减乘除和求余"""

# Calculator
try:
    from tkinter import *
except:
    from Tkinter import *


class Calculator:
    def __init__(self):
        # 新建一个窗口
        self.frame = Tk()
        # 指定窗体的标题
        self.frame.title("Calculator")
        #指定窗体大小
        self.frame.geometry("320x500")
        # 窗体不允许变化
        self.frame.resizable(0,0)
        # 设置窗口图标
        #self.iconbitmap('.\\icon.ico')

        # # 添加顶部Lable 标签--显示具体表达式
        self.var_detail = StringVar()
        self.Lable_datail = Label(self.frame, text="25+100=", textvariable=self.var_detail, font=("微软雅黑", 16), bg="lightgray", fg="DimGray",anchor="se")
        self.Lable_datail.place(x=0, y=0, width=320, height=200)

        # 添加结果标签 --显示结果
        self.var_result = StringVar()
        self.Lable_result = Label(self.frame, text="125", textvariable=self.var_result, font=("微软雅黑", 16), bg="gray",anchor="se")
        self.Lable_result.place(x=0, y=200, width= 320, height=50)

        # 添加按钮 -ac
        self.Button_ac = Button(self.frame, text="AC", font=("微软雅黑",18), fg="Orange", command=self.ac)
        self.Button_ac.place(x=0, y=250, width=80, height=50)

        # 添加按钮 " <- " 删除
        self.Button_del = Button(self.frame, text="<-", font=("微软雅黑", 18), fg="DimGray", command=self.delete)
        self.Button_del.place(x=80, y=250, width=80, height=50)

        # 添加按钮 :除法 ÷
        self.Button_div = Button(self.frame, text="÷", font=("微软雅黑", 18), fg="DimGray", command=self.division)
        self.Button_div.place(x=160, y=250, width=80, height=50)

        # 添加按钮 :乘法 ×
        self.Button_mul = Button(self.frame, text="×", font=("微软雅黑", 18),fg="DimGray", command=self.mul)
        self.Button_mul.place(x=240, y=250, width=80, height=50)

        # 添加按钮 :7
        self.Button_seven = Button(self.frame, text="7", font=("微软雅黑", 18), fg="DimGray", command=self.get_seven)
        self.Button_seven.place(x=0, y=300, width=80, height=50)

        # 添加按钮 :8
        self.Button_eight = Button(self.frame, text="8", font=("微软雅黑", 18), fg="DimGray", command=self.get_eight)
        self.Button_eight.place(x=80, y=300, width=80, height=50)

        # 添加按钮 :9
        self.Button_nine = Button(self.frame, text="9", font=("微软雅黑", 18), fg="DimGray", command=self.get_nine)
        self.Button_nine.place(x=160, y=300, width=80, height=50)

        # 添加按钮 :“- ”
        self.Button_minus = Button(self.frame, text="－", font=("微软雅黑", 18), fg="DimGray", command=self.sub)
        self.Button_minus.place(x=240, y=300, width=80, height=50)

        # 添加按钮 :4
        self.Button_four = Button(self.frame, text="4", font=("微软雅黑", 18), fg="DimGray", command=self.get_four)
        self.Button_four.place(x=0, y=350, width=80, height=50)

        # 添加按钮 :5
        self.Button_five = Button(self.frame, text="5", font=("微软雅黑", 18), fg="DimGray", command=self.get_five)
        self.Button_five.place(x=80, y=350, width=80, height=50)

        # 添加按钮 :6
        self.Button_six = Button(self.frame, text="6", font=("微软雅黑", 18), fg="DimGray", command=self.get_six)
        self.Button_six.place(x=160, y=350, width=80, height=50)

        # 添加按钮 :“＋ ”
        self.Button_plus = Button(self.frame, text="＋", font=("微软雅黑", 18), fg="DimGray", command=self.add)
        self.Button_plus.place(x=240, y=350, width=80, height=50)

        # 添加按钮 :1
        self.Button_one = Button(self.frame, text="1", font=("微软雅黑", 18), fg="DimGray", command=self.get_one)
        self.Button_one.place(x=0, y=400, width=80, height=50)

        # 添加按钮 :2
        self.Button_two = Button(self.frame, text="2", font=("微软雅黑", 18), fg="DimGray", command=self.get_two)
        self.Button_two.place(x=80, y=400, width=80, height=50)

        # 添加按钮 :3
        self.Button_three = Button(self.frame, text="3", font=("微软雅黑", 18), fg="DimGray", command=self.get_three)
        self.Button_three.place(x=160, y=400, width=80, height=50)

        # 添加按钮 : 取余 %
        self.Button_remainder = Button(self.frame, text="%", font=("微软雅黑", 18), fg="DimGray", command=self.get_remainder)
        self.Button_remainder.place(x=0, y=450, width=80, height=50)

        # 添加按钮 : 0
        self.Button_zero = Button(self.frame, text="0", font=("微软雅黑", 18), fg="DimGray", command=self.get_zero)
        self.Button_zero.place(x=80, y=450, width=80, height=50)

        # 添加按钮 : .
        self.Button_point = Button(self.frame, text=".", font=("微软雅黑", 18), fg="DimGray", command=self.get_point)
        self.Button_point.place(x=160, y=450, width=80, height=50)

        # 添加按钮 : =
        self.Button_equal = Button(self.frame, text="=", font=("微软雅黑", 18), bg="Orange", command=self.get_result)
        self.Button_equal.place(x=240, y=400, width=80, height=100)


    def ac(self):
        self.var_result.set("0")

    def delete(self):
        # 删除最后一个字符
        content = self.var_result.get()
        self.var_result.set(content[0:len(content)-1])

    def add(self):
        content = self.var_result.get()
        # 为明细赋值
        self.var_detail.set(content + " + ")
        # result 归0
        self.var_result.set("0")

    def sub(self):
        content = self.var_result.get()
        # 为明细赋值
        self.var_detail.set(content + " - ")
        # result 归0
        self.var_result.set("0")

    def mul(self):
        content = self.var_result.get()
        # 为明细赋值
        self.var_detail.set(content + " × ")
        # result 归0
        self.var_result.set("0")

    def division(self):
        content = self.var_result.get()
        # 为明细赋值
        self.var_detail.set(content + " ÷ ")
        # result 归0
        self.var_result.set("0")

    def get_remainder(self):
        content = self.var_result.get()
        # 为明细赋值
        self.var_detail.set(content + " % ")
        # result 归0
        self.var_result.set("0")

    def get_result(self):
        # 获取detail 明细
        detail = self.var_detail.get()
        num01 = detail.replace(" ", "")[0:len(detail.replace(" ", ""))-1]
        # 操作符取倒数第一个
        action = detail.replace(" ", "")[-1]
        num02 = self.var_result.get()
        # 根据操作符进行操作
        if action == "+":
            result = float(num01) + float(num02)
            # 修改明细
            self.var_detail.set("{0} + {1} = ".format(num01, num02))
            # 修改result
            self.var_result.set("{:.12g}".format(result))

        if action =="-":
            result = float(num01) - float(num02)
            # 修改明细
            self.var_detail.set("{0} - {1} = ".format(num01, num02))
            # 修改result
            self.var_result.set("{:.12g}".format(result))

        if action =="×":
            result = float(num01) * float(num02)
            # 修改明细
            self.var_detail.set("{0} × {1} = ".format(num01, num02))
            # 修改result
            self.var_result.set("{:.12g}".format(result))

        if action =="÷":
            result = float(num01) / float(num02)
            # 修改明细
            self.var_detail.set("{0} ÷ {1} = ".format(num01, num02))
            # 修改result
            self.var_result.set("{:.12g}".format(result))

        if action =="%":
            result = float(num01) % float(num02)
            # 修改明细
            self.var_detail.set("{0} % {1} = ".format(num01, num02))
            # 修改result
            self.var_result.set("{:.12g}".format(result))


    def get_one(self):
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("1")
        else:
            self.var_result.set(content + "1")

    def get_two(self):
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("2")
        else:
            self.var_result.set(content + "2")

    def get_three(self):
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("3")
        else:
            self.var_result.set(content + "3")

    def get_four(self):
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("4")
        else:
            self.var_result.set(content + "4")

    def get_five(self):
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("5")
        else:
            self.var_result.set(content + "5")

    def get_six(self):
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("6")
        else:
            self.var_result.set(content + "6")

    def get_seven(self):
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("7")
        else:
            self.var_result.set(content + "7")

    def get_eight(self):
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("8")
        else:
            self.var_result.set(content + "8")

    def get_nine(self):
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("9")
        else:
            self.var_result.set(content + "9")

    def get_zero(self):
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("0")
        else:
            self.var_result.set(content + "0")

    def get_point(self):
        content = self.var_result.get()
        self.var_result.set(content + ".")


    def show(self):
        self.frame.mainloop()


if __name__ == "__main__":
    my_cal = Calculator()
    my_cal.show()
#    multiprocessing.freeze_support()