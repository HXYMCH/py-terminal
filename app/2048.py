import random
from tkinter import Tk,Button,Label


def check_game_is_over():   #判断游戏是否结束
    global score,is_game_over,number_of_0
    if is_game_over:        #is_game_over是结束标志，=true已结束
        return True
    if number_of_0 !=0:     #number_of_0是列表digits中0的个数，非0不结束
        return False
    for a in digits:        #列表digits每行相邻项比较，有相等的能合并，不结束
        if a[0]==a[1] or a[1]==a[2] or a[2]==a[3]:
            return False
    for n in range(4):      #列表digits每列相邻项比较，有相等的能合并，不结束 
        if digits[0][n]==digits[1][n] or digits[1][n]==digits[2][n] or digits[2][n]==digits[3][n]:
            return False
    is_game_over=True   #列表digits各项都不为0，每行每列所有相邻项比较都不等，游戏结束
    label1['text']='Final score\n'+str(score)

def leftPressed(event):                     #按←键的事件函数
    if check_game_is_over():
        return
    if move_to_left():                      #函数返回值为true,说明数字被移动
        add2or4_and_Display(score)          #增加1个2或4，在屏幕显示得分和移动后的结果

def rightPressed(event):                    #按→键的事件函数
    if check_game_is_over():
        return
    for a in digits:                        #将列表每1行都反序
        a.reverse()
    changed=move_to_left()
    for a in digits:                        #将列表每1行都再反序，即回复原来顺序
        a.reverse()
    if changed:
        add2or4_and_Display(score)

def downPressed(event):                     #按↓键的事件函数
    global digits
    if check_game_is_over():
        return
    digits=list(map(list,zip(*digits)))     #列表digits转置，即行变列，列变行
    for a in digits:
        a.reverse()
    changed=move_to_left()
    for a in digits:
        a.reverse()
    digits=list(map(list,zip(*digits)))     #列表digits再转置，即回复原状
    if changed:
        add2or4_and_Display(score)

def upPressed(event):                       #按↑键的事件函数
    global digits
    if check_game_is_over():
        return
    digits=list(map(list,zip(*digits)))
    changed=move_to_left()
    digits=list(map(list,zip(*digits)))
    if changed:
        add2or4_and_Display(score)

def btnClick():                             #单击重玩按钮事件函数
    global digits,score,is_game_over
    is_game_over=False
    score=0
    digits=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]       
    add2or4()
    add2or4_and_Display(score)

def add2or4():                              #函数增加一个2或4
    zeros=[]                                #该列表保存列表digits是0的项的行列号
    for row in range(4):                    #row=行,0,1,2,3
        for col in range(4):                #col=列,0,1,2,3
            if digits[row][col]==0:         #如果列digits某项为0
                zeros.append([row,col])     #列表zeros保存该项的行列号
    if len(zeros) == 0:                     #如列表digits无项为0
        return 0        #返回值为0,下条语句在zeros随机选1项作为digits某项行列号变为2or4
    n=random.randint(0,len(zeros) - 1)      #下条语句令该项值为2或4,是2或4随机产生
    digits[zeros[n][0]][zeros[n][1]]=random.choice([2,2,2,4,2])#增减2,4改变出现概率比
    return len(zeros)-1       #返回值是列表digits增加了1个0或4后，各项为0的个数 
           
def add2or4_and_Display(s):   #函数增加1个2或4，并在屏幕显示移动后的结果，参数是当前得分
    global number_of_0        #number_of_0记录列表digits中为0项的个数
    label1['text']='Score\n'+str(s)
    number_of_0=add2or4()       #add2or4()返回值是列表digits中为0的项的数量
    for row in range(4):        #row=行,0,1,2,3
        for col in range(4):    #col=列,0,1,2,3
            if digits[row][col]!=0:
                labels[row,col]['text']=digits[row][col]
            else:               #为0，显示空
                labels[row,col]['text']=' '

def move_to_left():     #函数让整个数字方阵往左移动
    global score
    changed=False       #执行函数后是否移动，默认是未移动
    for a in digits:    #利用循环，取出每一行，注意a是digits某项引用
        b = []          #空列表，逐一保存移动后的数
        last=0          #存上一个数据，用来比较和下1个数据是否相等
        for v in a:     #从每一行里面读取每一个数
            if v!=0:    #如果这个数不是0，将添加到b中，是0将被丢弃
                if v!=last:      #如读取的数和上一个元素不等
                    b.append(v)  #那么将v添入b列表
                    last=v       #然后更新last，用于下一次合成判断
                else:            #否则的话，那就说明v和last相等，可以合并
                    n=b.pop()*2  #这时直接让b的最后弹出一个并*2
                    score+=n     #得分增加n
                    b.append(n)  
                    last=0       #合并后的数即使和下1个数相等,也不能合并
        b+=[0]*(4-len(b))        #合成完之后，在末尾添加0，凑足4个数
        for i in range(0,4):     #每次合成完毕之后，检查和原来的是否相同
            if a[i]!=b[i]:       #如果和原来的不同，说明已被移动
                changed = True   #只要有一行被移动，就要返回true
        a[:]=b          #每一行移动完毕后，把移动后的b列表传给原来的a列表，进行替换
    return changed      #所有行都移动完毕之后，返回移动是否成功的结果


root = Tk()                 #初始化窗口
root.title('2048')      #窗口标题
root.geometry("300x350")    #窗口宽300,高=350
root.resizable(width=False,height=False) #设置窗口是否可变,宽不可变,高不可变,默认为True

labels={}                    #字典，保存每个Label对象，键是该Label对象所在位置的行列号
digits=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]#记录label显示的数字,为0表示label显示为空
for row in range(4):            #row=行,0,1,2,3,将控件lLabel按4行4列排列，组成矩阵
    for col in range(4):        #col=列,0,1,2,3,用Label矩阵显示2048游戏的数字
        label=Label(root,fg='red',bg="Silver",font=("Arial",15))
        labels[row,col]=label    #保存label对象到字典，注意键值为行列号       
        label.place(x=35+col*60,y=90+row*60,width=55,height=55)        #见下下条注释

label1=Label(root,fg='red',font=("Arial",14))       #用来显示得分
label1.place(x=20,y=20,width=170,height=50)         #控件位置坐标为(x,y),宽=100,高=40
button=Button(root,text='again',command=btnClick,fg='red',font=("Arial",15))  #重玩按钮
button.place(x=190,y=20,width=80,height=40)
number_of_0=14                      #列表digits中项值为0的个数
score = 0                           #得分
is_game_over=False                  #游戏是否结束
add2or4()                           #初始增加2个2或4，先增加1个
add2or4_and_Display(score)          #先增加1个2或4,再显示分数,再将列表digits数据在屏幕显示


root.bind("<Left>", leftPressed)
root.bind("<Right>", rightPressed)
root.bind("<Down>", downPressed)
root.bind("<Up>", upPressed)
root.mainloop()	
