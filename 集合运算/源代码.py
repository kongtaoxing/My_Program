#Author：夏云峰
#2021/12/03
import numpy as np
from matplotlib import pyplot as plt
from matplotlib_venn import venn2     #画Venn图的库
import tkinter as tk      #GUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk 

def create_matplotlib(var_A:str,var_B:str):
    f=plt.figure(num=2,figsize=(16,12),dpi=80,facecolor="white",edgecolor='green',frameon=True)
    set1=set(map(int,var_A.split()))
    set2=set(map(int,var_B.split()))
    plt.rcParams['font.sans-serif']=['SimHei'] #使界面可以显示中文字体   
    plt.rcParams['axes.unicode_minus']=False   #用来显示负号
    subset=[set1,set2]
    g=venn2(subset,set_labels = ('A','B'), set_colors=('g','r'))   
    plt.title('两个集合的交集、并集、相对补集、对称差集和两个集合的幂集') 
    #求集合的幂集
    def add_set_to_list(l,s):
        if s not in l:
            l.append(s)
    def F(e, T):
        l=[]
        add_set_to_list(l,e)
        for x in T:
            y=e|x
            add_set_to_list(l,y)
        return l
    def P(s):
        l=[set(),]
        for e in s:
            l.extend(F(set((e,)),l))
        l[0]='∅'
        return l
    #两个集合均为空集
    if len(set1)==0 and len(set2)==0:    
        result=tk.Tk()
        result.title("结论")
        result.geometry("600x50")
        result.l=tk.Label(result,text="A∩B=∅，A∪B=∅，A-B=∅，B-A=∅，A⊕B=∅，P(A)={∅}，P(B)={∅}")
        result.l.place(x=10,y=10)
    #集合A为空集
    elif len(set1)==0 and len(set2)!=0:
        #相对补集、并集、对称差集
        plt.annotate('这部分为 A 在 B 中的相对补集(B-A)，并集( A∪B)，对称差集(A⊕B)', 
         color='black',
         xy=g.get_label_by_id('01').get_position() + np.array([0, 0.05]), 
         xytext=(80,40),
         ha='center', textcoords='offset points', 
         bbox=dict(boxstyle='round,pad=0.5', fc='#c72e29', alpha=0.6),
         arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=0.5',color='black')
        )     
        result=tk.Tk()
        result.title("结论")
        result.geometry("600x150")
        result.l=tk.Label(result,
                          text="A∩B=∅，A∪B={}，A-B=∅，B-A={}，A⊕B={}\nP(A)={}\nP(B)={}"
                          .format(set1|set2,set2-set1,set1^set2,P(set1),P(set2)),
                          wraplength=600)
        result.l.place(x=10,y=10)
    #集合B为空集
    elif len(set1)!=0 and len(set2)==0:
        #相对补集、并集、对称差集
        plt.annotate('这部分的 A 在 B 中的相对补集(B-A)，并集( A∪B)，对称差集(A⊕B)', 
         color='black',
         xy=g.get_label_by_id('10').get_position() + np.array([0, 0.05]), 
         xytext=(80,40),
         ha='center', textcoords='offset points', 
         bbox=dict(boxstyle='round,pad=0.5', fc='#098154', alpha=0.6),
         arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=0.5',color='black')
        )  
        result=tk.Tk()
        result.title("结论")
        result.geometry("600x150")
        result.l=tk.Label(result,
                          text="A∩B=∅，A∪B={}，A-B={}，B-A=∅，A⊕B={}\nP(A)={}\nP(B)={}"
                          .format(set1|set2,set1-set2,set1^set2,P(set1),P(set2)),
                          wraplength=600)
        result.l.place(x=10,y=10)
    else:
    #集合A、B的交集为空集
        if len(set1&set2)==0:
            #相对补集
            plt.annotate('这部分是 B 在 A 中的相对补集，即 A-B', 
             color='black',
             xy=g.get_label_by_id('10').get_position() - np.array([0, 0.05]), 
             xytext=(-80,40),
             ha='center', textcoords='offset points', 
             bbox=dict(boxstyle='round,pad=0.5', fc='#098154', alpha=0.6),#注释文字底纹
             arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=0.5',color='black')#箭头属性设置
            )
            plt.annotate('这部分是 A 在 B 中的相对补集，即 B-A', 
             color='black',
             xy=g.get_label_by_id('01').get_position() - np.array([0, 0.05]), 
             xytext=(80,40),
             ha='center', textcoords='offset points', 
             bbox=dict(boxstyle='round,pad=0.5', fc='#c72e29', alpha=0.6),#注释文字底纹
             arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=0.5',color='black')#箭头属性设置
            )
            #并集
            plt.annotate('这两部分之和是 A 与 B 的并集，即A∪B', 
             color='black',
             xy=g.get_label_by_id('10').get_position() + np.array([0, 0.3]), 
             xytext=(140,30),
             ha='center', textcoords='offset points', 
             bbox=dict(boxstyle='round,pad=0.5', fc='grey', alpha=0.6),
             arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=-0.5',color='black')
            )
            plt.annotate('', 
             color='black',
             xy=g.get_label_by_id('01').get_position() + np.array([0, 0.3]), 
             xytext=(-100,30),
             ha='center', textcoords='offset points', 
             bbox=dict(boxstyle='round,pad=0.5', fc='grey', alpha=0.6),
             arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=0.5',color='black')
            )           
            #对称差集
            plt.annotate('', 
             color='black',
             xy=g.get_label_by_id('01').get_position() - np.array([0, 0.3]), 
             xytext=(-100,-80),
             ha='center', textcoords='offset points', 
             bbox=dict(boxstyle='round,pad=0.5', fc='grey', alpha=0.6),
             arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=0.5',color='black')
            )
            plt.annotate('这两部分之和是 A 与 B 的对称差集，即A⊕B', 
             color='black',
             xy=g.get_label_by_id('10').get_position() - np.array([0, 0.3]), 
             xytext=(120,-80),
             ha='center', textcoords='offset points', 
             bbox=dict(boxstyle='round,pad=0.5', fc='grey', alpha=0.6),
             arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=-0.5',color='black')
            )
            result=tk.Tk()
            result.title("结论")
            result.geometry("600x150")
            result.l=tk.Label(result,
                              text="A∩B=∅，A∪B={}，A-B={}，B-A={}，A⊕B={}\nP(A)={}\nP(B)={}"
                              .format(set1|set2,set1-set2,set2-set1,set1^set2,P(set1),P(set2)),
                              wraplength=600)
            result.l.place(x=10,y=10)
        else:      
        #A、B相等
            if set1==set2:
                #交集、并集
                plt.annotate('这部分是 A 与 B 的交集和并集，即A∩B，A∩B', 
                 color='black',
                 xy=g.get_label_by_id('11').get_position() + np.array([0, 0.05]), 
                 xytext=(20,40),
                 ha='center', textcoords='offset points', 
                 bbox=dict(boxstyle='round,pad=0.5', fc='grey', alpha=0.6),
                 arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=-0.5',color='black')
                )          
                result=tk.Tk()
                result.title("结论")
                result.geometry("600x150")
                result.l=tk.Label(result,
                                  text="A∩B={}，A∪B={}，A-B=∅，B-A=∅，A⊕B=∅\nP(A)={}\nP(B)={}"
                                  .format(set1&set2,set1|set2,P(set1),P(set2)),
                                  wraplength=400)
                result.l.place(x=10,y=10)
            else:
            #A包含于B
                if len(set1-set2)==0:
                #相对补集    
                    plt.annotate('这部分的 A 在 B 中的相对补集(B-A)和对称差集(A⊕B)', 
                     color='black',
                     xy=g.get_label_by_id('01').get_position() + np.array([0, 0.05]), 
                     xytext=(80,40),
                     ha='center', textcoords='offset points', 
                     bbox=dict(boxstyle='round,pad=0.5', fc='#c72e29', alpha=0.6),
                     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=0.5',color='black')
                    )   
                #交集
                    plt.annotate('这部分是 A 与 B 的交集，即A∩B', 
                     color='black',
                     xy=g.get_label_by_id('11').get_position() + np.array([0, 0.05]), 
                     xytext=(20,40),
                     ha='center', textcoords='offset points', 
                     bbox=dict(boxstyle='round,pad=0.5', fc='grey', alpha=0.6),
                     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=-0.5',color='black')
                    )   
                #并集
                    plt.annotate('这两部分之和是 A 与 B 的并集，即A∪B', 
                     color='black',
                     xy=g.get_label_by_id('11').get_position() + np.array([0, 0.3]), 
                     xytext=(140,30),
                     ha='center', textcoords='offset points', 
                     bbox=dict(boxstyle='round,pad=0.5', fc='grey', alpha=0.6),
                     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=0.5',color='black')
                    )
                    plt.annotate('', 
                     color='black',
                     xy=g.get_label_by_id('01').get_position() + np.array([0, 0.3]), 
                     xytext=(-100,30),
                     ha='center', textcoords='offset points', 
                     bbox=dict(boxstyle='round,pad=0.5', fc='grey', alpha=0.6),
                     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=-0.5',color='black')
                    )  
                    result=tk.Tk()
                    result.title("结论")
                    result.geometry("600x150")
                    result.l=tk.Label(result,
                                      text="A∩B={}，A∪B={}，A-B={}，B-A={}，A⊕B={}\nP(A)={}\nP(B)={}"
                                      .format(set1&set2,set1|set2,set1-set2,set2-set1,set1^set2,P(set1),P(set2)),
                                      wraplength=400)
                    result.l.place(x=10,y=10)
            #B包含于A
                elif len(set2-set1)==0:
                #相对补集    
                    plt.annotate('这部分的 A 在 B 中的相对补集(B-A)和对称差集(A⊕B)', 
                     color='black',
                     xy=g.get_label_by_id('11').get_position() + np.array([0, 0.05]), 
                     xytext=(80,40),
                     ha='center', textcoords='offset points', 
                     bbox=dict(boxstyle='round,pad=0.5', fc='#c72e29', alpha=0.6),
                     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=0.5',color='black')
                    )   
                #交集
                    plt.annotate('这部分是 A 与 B 的交集，即A∩B', 
                     color='black',
                     xy=g.get_label_by_id('11').get_position() + np.array([0, -0.05]), 
                     xytext=(20,-40),
                     ha='center', textcoords='offset points', 
                     bbox=dict(boxstyle='round,pad=0.5', fc='grey', alpha=0.6),
                     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=-0.5',color='black')
                    )   
                #并集
                    plt.annotate('这两部分之和是 A 与 B 的并集，即A∪B', 
                     color='black',
                     xy=g.get_label_by_id('11').get_position() + np.array([0, 0.3]), 
                     xytext=(-140,30),
                     ha='center', textcoords='offset points', 
                     bbox=dict(boxstyle='round,pad=0.5', fc='grey', alpha=0.6),
                     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=0.5',color='black')
                    )
                    plt.annotate('', 
                     color='black',
                     xy=g.get_label_by_id('10').get_position() + np.array([0, 0.3]), 
                     xytext=(-40,30),
                     ha='center', textcoords='offset points', 
                     bbox=dict(boxstyle='round,pad=0.5', fc='grey', alpha=0.6),
                     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=0.9',color='black')
                    )    
                    result=tk.Tk()
                    result.title("结论")
                    result.geometry("600x150")
                    result.l=tk.Label(result,
                                      text="A∩B={}，A∪B={}，A-B={}，B-A={}，A⊕B={}\nP(A)={}\nP(B)={}"
                                      .format(set1&set2,set1|set2,set1-set2,set2-set1,set1^set2,P(set1),P(set2)),
                                      wraplength=400)
                    result.l.place(x=10,y=10)
            #一般情况
                else:
                    #相对补集
                    plt.annotate('这部分是 B 在 A 中的相对补集，即 A-B', 
                     color='black',
                     xy=g.get_label_by_id('10').get_position() - np.array([0, 0.05]), 
                     xytext=(-80,40),
                     ha='center', textcoords='offset points', 
                     bbox=dict(boxstyle='round,pad=0.5', fc='#098154', alpha=0.6),#注释文字底纹
                     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=0.5',color='black')#箭头属性设置
                    )
                    plt.annotate('这部分的 A 在 B 中的相对补集，即 B-A', 
                         color='black',
                         xy=g.get_label_by_id('01').get_position() + np.array([0, 0.05]), 
                         xytext=(80,40),
                         ha='center', textcoords='offset points', 
                         bbox=dict(boxstyle='round,pad=0.5', fc='#c72e29', alpha=0.6),
                         arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=0.5',color='black')
                        )
                    #交集
                    plt.annotate('这部分是 A 与 B 的交集，即A∩B', 
                     color='black',
                     xy=g.get_label_by_id('11').get_position() + np.array([0, 0.05]), 
                     xytext=(20,40),
                     ha='center', textcoords='offset points', 
                     bbox=dict(boxstyle='round,pad=0.5', fc='grey', alpha=0.6),
                     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=-0.5',color='black')
                    )
                    #并集
                    plt.annotate('这三部分之和是 A 与 B 的并集，即A∪B', 
                     color='black',
                     xy=g.get_label_by_id('11').get_position() + np.array([0, 0.3]), 
                     xytext=(20,65),
                     ha='center', textcoords='offset points', 
                     bbox=dict(boxstyle='round,pad=0.5', fc='grey', alpha=0.6),
                     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=-0.5',color='black')
                    )
                    plt.annotate('', 
                     color='black',
                     xy=g.get_label_by_id('10').get_position() + np.array([0, 0.3]), 
                     xytext=(140,65),
                     ha='center', textcoords='offset points', 
                     bbox=dict(boxstyle='round,pad=0.5', fc='grey', alpha=0.6),
                     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=-0.5',color='black')
                    )
                    plt.annotate('', 
                     color='black',
                     xy=g.get_label_by_id('01').get_position() + np.array([0, 0.3]), 
                     xytext=(-100,65),
                     ha='center', textcoords='offset points', 
                     bbox=dict(boxstyle='round,pad=0.5', fc='grey', alpha=0.6),
                     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=0.5',color='black')
                    )
                    #对称差集
                    plt.annotate('', 
                     color='black',
                     xy=g.get_label_by_id('01').get_position() - np.array([0, 0.1]), 
                     xytext=(-100,-80),
                     ha='center', textcoords='offset points', 
                     bbox=dict(boxstyle='round,pad=0.5', fc='grey', alpha=0.6),
                     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=0.5',color='black')
                    )
                    plt.annotate('这两部分之和是 A 与 B 的对称差集，即A⊕B', 
                     color='black',
                     xy=g.get_label_by_id('10').get_position() - np.array([0, 0.1]), 
                     xytext=(120,-80),
                     ha='center', textcoords='offset points', 
                     bbox=dict(boxstyle='round,pad=0.5', fc='grey', alpha=0.6),
                     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=-0.5',color='black')
                    )   
                    result=tk.Tk()
                    result.title("结论")
                    result.geometry("600x150")
                    result.l=tk.Label(result,
                                      text="A∩B={}，A∪B={}，A-B={}，B-A={}，A⊕B={}\nP(A)={}\nP(B)={}"
                                      .format(set1&set2,set1|set2,set1-set2,set2-set1,set1^set2,P(set1),P(set2)),
                                      wraplength=400)
                    result.l.place(x=10,y=10)
    return f

def create_form(figure):
    win=tk.Tk()
    win.title("图形展示")
    win.geometry("800x600")
    win.canvas=FigureCanvasTkAgg(figure,win)
    win.canvas.draw()
    win.canvas.get_tk_widget().place(x=100, y=300)
    toolbar =NavigationToolbar2Tk(win.canvas, win)
    toolbar.update()
    win.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH)

Win=tk.Tk()
Win.title("数据输入")
Win.geometry("500x400")
Win.canvas=tk.Canvas()
Win.l0=tk.Label(Win,text="请输入 A，B 两个集合，每个集合的元素与元素之间用空格隔开")
Win.l0.place(x=100,y=100)
Win.l1=tk.Label(Win, text="集合 A ：")
Win.l1.place(x=100,y=150)
var_A=tk.StringVar()
Win.e1=tk.Entry(Win,textvariable=var_A)
Win.e1.place(x=160,y=150)
Win.l2=tk.Label(Win, text="集合 B ：")
Win.l2.place(x=100,y=200)
var_B=tk.StringVar()
Win.e2=tk.Entry(Win,textvariable=var_B)
Win.e2.place(x=160,y=200)   
Win.b1=tk.Button(Win,
                 text="运行",
                 command=lambda:create_form(create_matplotlib(str(var_A.get()),str(var_B.get())))
                 )
Win.b1.place(x=130,y=250)
Win.b2=tk.Button(Win,text="退出",command=Win.destroy)
Win.b2.place(x=250,y=250)
Win.mainloop()  
