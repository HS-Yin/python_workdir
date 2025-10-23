from functools import partial
import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QGridLayout, QPushButton
import numpy as np

      
class MainWindow(QWidget):

    
    def __init__(self):
        super().__init__()  
        self.a = np.array([["a1","b1","c1","d1","e1","d1","c1","b1","a1"],
                ["  ","  ","  ","  ","  ","  ","  ","  ","  "],
                ["  ","f1","  ","  ","  ","  ","  ","f1","  "],
                ["g1","  ","g1","  ","g1","  ","g1","  ","g1"],
                ["  ","  ","  ","  ","  ","  ","  ","  ","  "],
                ["  ","  ","  " ,"  ","  ","  ","  ","  ","  "],
                ["g0","  ","g0","  ","g0","  ","g0","  ","g0"],
                ["  ","f0","  ","  ","  ","  ","  ","f0","  "],
                ["  ","  ","  ","  ","  ","  ","  ","  ","  "],
                ["a0","b0","c0","d0","e0","d0","c0","b0","a0"]])
        self.flag = "0" 
        self.d1 = []
        self.bt = []
        self.setWindowTitle("PyQt5")  
        layout = QGridLayout()
        
        for i in range(10):
            for j in range(9):
                  button = QPushButton(" ")
                  self.bt.append(button)
                  self.bt[i*9+j].setFixedSize(40,40)
                  self.bt[i*9+j].clicked.connect(partial(self.on_button_clicked, i, j))
                  layout.addWidget(self.bt[i*9+j], i, j)
                 
        self.mapping()
        self.setLayout(layout)
        
    def on_button_clicked(self,i,j):
        self.d1.append(i)
        self.d1.append(j)
        print(self.d1)
        if(len(self.d1) ==4):
            pos1_x = self.d1[1]+1
            pos1_y = 10-self.d1[0] 
            pos2_x = self.d1[3]+1
            pos2_y = 10-self.d1[2]
            self.move(pos1_x,pos1_y,pos2_x,pos2_y)
            self.mapping()
            self.d1 = []

    def mapping(self):
        for i in range(10):
            for j in range(9):
                piece = self.a[i,j]
                self.bt[i*9+j].setText(piece)

    def move(self,pos_x1,pos_y1,pos_x2,pos_y2):  
        pos1_x = 10-pos_y1 
        pos1_y = pos_x1-1 
        pos2_x = 10-pos_y2 
        pos2_y = pos_x2-1
        print(pos1_x,pos1_y,pos2_x,pos2_y) 
        select1 = self.a[pos1_x,pos1_y] 
        select2 = self.a[pos2_x,pos2_y] 
        flag_1 = 0  
        if(not(pos_x1>=1 and pos_x1<=9 and pos_y1>=1 and pos_y1<=10 and pos_x2>=1 and pos_x2>=1 and pos_y2>=1 and pos_y2<=10)):
            print("erro") 
        elif(select1=="  "): 
            print("err1") 
        elif(self.flag in select2): 
            print("err2") 
        else: 
            if(self.flag in select1): 
                if("a" in select1): 
                    if(pos1_x==pos2_x):
                        if(pos1_y>pos2_y):
                            m=-1
                        else:
                            m=1 
                        for i in range(pos1_y,pos2_y,m): 
                            if(self.a[pos1_x,i] != "  "): 
                                if(i==pos1_y or i==pos2_y): 
                                    continue 
                                flag_1 = 1
                                break
                    elif(pos1_y==pos2_y): 
                        if(pos1_x>pos2_x):
                            m=-1
                        else:
                            m=1 
                        for i in range(pos1_x,pos2_x,m): 
                            if(self.a[i,pos1_y] !="  "): 
                                if(i==pos1_x or i==pos2_x): 
                                    continue 
                                flag_1 = 1 
                                break 
                    else: 
                        flag_1 = 1 

                elif("b" in select1): 
                    if(abs(pos2_x-pos1_x) == 2 and abs(pos2_y-pos1_y) == 1): 
                        if(pos2_x>pos1_x): 
                            if(self.a[pos1_x + 1,pos1_y] != "  "): 
                                flag_1 = 1 
                            elif(pos2_x<pos1_x): 
                                if(self.a[pos1_x - 1,pos1_y] != "  "): 
                                    flag_1 = 1 
                    elif(abs(pos2_x-pos1_x) == 1 and abs(pos2_y-pos1_y) == 2): 
                        if(pos2_y>pos1_y): 
                            if(self.a[pos1_x,pos1_y + 1] != "  "): 
                                flag_1 = 1 
                        elif(pos2_y<pos1_y): 
                            if(self.a[pos1_x,pos1_y- 1] != "  "): 
                                flag_1 = 1 
                    else: 
                        flag_1 = 1 

                elif("c" in select1): 
                    if((self.flag == 0 and pos_y2>5) or (self.flag == 1 and pos_y2<=5)):
                        flag_1 = 1 
                    elif(abs(pos2_x-pos1_x) == 2 and abs(pos2_y-pos1_y) == 2): 
                        if(pos2_x>pos1_x and pos2_y>pos1_y): 
                            if(self.a[pos1_x + 1,pos1_y + 1] !="  "): 
                                flag_1 = 1 
                        elif(pos2_x<pos1_x and pos2_y<pos1_y):
                            if(self.a[pos1_x - 1,pos1_y - 1] !="  "): 
                                    flag_1 = 1 
                        elif(pos2_x>pos1_x and pos2_y<pos1_y):
                            if(self.a[pos1_x + 1,pos1_y - 1] !="  "): 
                                    flag_1 = 1 
                        elif(pos2_x<pos1_x and pos2_y>pos1_y): 
                            if(self.a[pos1_x - 1,pos1_y+ 1] != "  "):
                                        flag_1 = 1 
                    else: 
                        flag_1 = 1 

                elif("d" in select1):
                    if((self.flag == "0" and (pos_y2>3 or pos_x2<4 or pos_x2>6)) or (self.flag == "1" and (pos_y2<8 or pos_x2<4 or pos_x2>6))):
                        flag_1 = 1
                    elif(abs(pos2_x-pos1_x) == 1 and abs(pos2_y-pos1_y) == 1): 
                        pass 
                    else: 
                        flag_1 = 1 

                elif("e" in select1): 
                    if((self.flag == "0" and (pos_y2>3 or pos_x2<4 or pos_x2>6)) or (self.flag == "1" and (pos_y2<8 or pos_x2<4 or pos_x2>6))):
                        flag_1 = 1 
                    elif((abs(pos2_x-pos1_x) == 1 and pos2_y == pos1_y) or (abs(pos2_y-pos1_y) == 1 and pos2_x==pos1_x)): 
                        pass 
                    else: 
                        flag_1 = 1 

                elif("f" in select1): 
                    if(select2 == "  "): 
                        if(pos1_x==pos2_x):
                            if(pos1_y>pos2_y):
                                m=-1
                            else:
                                m=1 
                            for i in range(pos1_y,pos2_y,m):
                                if(self.a[pos1_x,i] != "  "):
                                    if(i==pos1_y or i==pos2_y):
                                        continue 
                                    flag_1 = 1
                                    break
                        elif(pos1_y==pos2_y):
                            if(pos1_x>pos2_x):
                                m=-1
                            else:
                                m=1
                            for i in range(pos1_x,pos2_x,m):
                                if(self.a[i,pos1_y]!="  "):
                                    if(i==pos1_x or i==pos2_x):
                                        continue
                                    flag_1 = 1
                                    break
                    elif(select2 != "  "):
                        num =0
                        if(pos1_x==pos2_x):
                            if(pos1_y>pos2_y):
                                m=-1
                            else:
                                m=1
                            for i in range(pos1_y,pos2_y,m):
                                if(self.a[pos1_x,i] != "  "):
                                    if(i==pos1_y or i==pos2_y):
                                        continue
                                    num = num + 1
                                    
                            if(num != 1):
                                flag_1 =1
                        elif(pos1_y==pos2_y):
                            if(pos1_x>pos2_x):
                                m=-1
                            else:
                                m=1
                            for i in range(pos1_x,pos2_x,m):
                                if(self.a[i,pos1_y]!= "  "):
                                    print(self.a[i,pos1_y])
                                    if(i==pos1_x or i==pos2_x):
                                        continue
                                    num =num +1
                            if(num != 1):
                                print("m")
                                flag_1 = 1
                    else:
                        flag_1 =1

                elif("g" in select1):
                    if((self.flag =="0"and pos_y2<pos_y1) or (self.flag =="1" and pos_y2>pos_y1)):
                        flag_1 =1
                    elif((self.flag =="0"and pos_y1<=5) or (self.flag == "1" and pos_y1>=6)):
                        if(pos_x2 != pos_x1):
                            flag_1=1
                    elif((abs(pos2_x-pos1_x)== 1 and pos2_y == pos1_y) or (abs(pos2_y-pos1_y)== 1 and pos2_x==pos1_x)):
                        pass
                    else:
                        flag_1 = 1

                if(flag_1 == 0):
                    self.a[pos1_x,pos1_y] = "  "
                    self.a[pos2_x,pos2_y] = select1
                    if(self.flag =="0"):
                        self.flag ="1"
                    elif(self.flag =="1"):
                        self.flag ="0"
                    print("player "+self.flag+" turn")
                else:
                    flag_1 =0
                    print("err3")
            else:
                print("err4")
            print(self.a)


app = QApplication(sys.argv)
window = MainWindow()
window.setGeometry(300, 300, 300, 300)
window.show() 
sys.exit(app.exec_())
