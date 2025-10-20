import numpy as np
def move(pos_x1,pos_y1,pos_x2,pos_y2): 
    global flag 
    pos1_x = 10-pos_y1 
    pos1_y = pos_x1-1 
    pos2_x = 10-pos_y2 
    pos2_y = pos_x2-1 
    select1 = a[pos1_x,pos1_y] 
    select2 = a[pos2_x,pos2_y] 
    flag_1 = 0  
    if(not(pos_x1>=1 and pos_x1<=9 and pos_y1>=1 and pos_y1<=10 and pos_x2>=1 and pos_x2>=1 and pos_y2>=1 and pos_y2<=10)):
        print("erro") 
    elif(select1=="  "): 
        print("err1") 
    elif(flag in select2): 
        print("err2") 
    else: 
        if(flag in select1): 
            if("a" in select1): 
                if(pos1_x==pos2_x): 
                    for i in range(pos1_y,pos2_y): 
                        if(a[pos1_x,i] != "  "): 
                            if(i==pos1_y or i==pos2_y): 
                                continue 
                            flag_1 = 1
                            break
                elif(pos1_y==pos2_y): 
                    for i in range(pos1_x,pos2_x): 
                        if(a[i,pos1_y] !="  "): 
                            if(i==pos1_x or i==pos2_x): 
                                continue 
                            flag_1 = 1 
                            break 
                        else: 
                            flag_1 = 1 

            elif("b" in select1): 
                if(abs(pos2_x-pos1_x) == 2 and abs(pos2_y-pos1_y) == 1): 
                    if(pos2_x>pos1_x): 
                        if(a[pos1_x + 1,pos1_y] != "  "): 
                            flag_1 = 1 
                        elif(pos2_x<pos1_x): 
                            if(a[pos1_x - 1,pos1_y] != "  "): 
                                flag_1 = 1 
                elif(abs(pos2_x-pos1_x) == 1 and abs(pos2_y-pos1_y) == 2): 
                    if(pos2_y>pos1_y): 
                        if(a[pos1_x,pos1_y + 1] != "  "): 
                            flag_1 = 1 
                    elif(pos2_y<pos1_y): 
                        if(a[pos1_x,pos1_y- 1] != "  "): 
                            flag_1 = 1 
                else: 
                    flag_1 = 1 

            elif("c" in select1): 
                if((flag == 0 and pos_y2>5) or (flag == 1 and pos_y2<=5)):
                    flag_1 = 1 
                elif(abs(pos2_x-pos1_x) == 2 and abs(pos2_y-pos1_y) == 2): 
                    if(pos2_x>pos1_x and pos2_y>pos1_y): 
                        if(a[pos1_x + 1,pos1_y + 1] !="  "): 
                            flag_1 = 1 
                    elif(pos2_x<pos1_x and pos2_y<pos1_y):
                        if(a[pos1_x - 1,pos1_y - 1] !="  "): 
                                flag_1 = 1 
                    elif(pos2_x>pos1_x and pos2_y<pos1_y):
                        if(a[pos1_x + 1,pos1_y - 1] !="  "): 
                                flag_1 = 1 
                    elif(pos2_x<pos1_x and pos2_y>pos1_y): 
                        if(a[pos1_x - 1,pos1_y+ 1] != "  "):
                                    flag_1 = 1 
                else: 
                    flag_1 = 1 

            elif("d" in select1):
                if((flag == "0" and (pos_y2>3 or pos_x2<4 or pos_x2>6)) or (flag == "1" and (pos_y2<8 or pos_x2<4 or pos_x2>6))):
                    flag_1 = 1
                elif(abs(pos2_x-pos1_x) == 1 and abs(pos2_y-pos1_y) == 1): 
                    pass 
                else: 
                    flag_1 = 1 

            elif("e" in select1): 
                if((flag == "0" and (pos_y2>3 or pos_x2<4 or pos_x2>6)) or (flag == "1" and (pos_y2<8 or pos_x2<4 or pos_x2>6))):
                    flag_1 = 1 
                elif((abs(pos2_x-pos1_x) == 1 and pos2_y == pos1_y) or (abs(pos2_y-pos1_y) == 1 and pos2_x==pos1_x)): 
                    pass 
                else: 
                    flag_1 = 1 

            elif("f" in select1): 
                if(select2 == "  "): 
                    if(pos1_x==pos2_x): 
                        for i in range(pos1_y,pos2_y):
                            if(a[pos1_x,i] != "  "):
                                if(i==pos1_y or i==pos2_y):
                                    continue 
                                flag_1 = 1
                                break
                    elif(pos1_y==pos2_y):
                        for i in range(pos1_x,pos2_x):
                            if(a[i,pos1_y]!="  "):
                                if(i==pos1_x or i==pos2_x):
                                    continue
                                flag_1 = 1
                                break
                elif(select2 != "  "):
                    num =0
                    if(pos1_x==pos2_x):
                        for i in range(pos1_y,pos2_y):
                            if(a[pos1_x,i] != "  "):
                                if(i==pos1_y or i==pos2_y):
                                    continue
                                num = num + 1
                        if(num != 1):
                            flag_1 =1
                    elif(pos1_y==pos2_y):
                        for i in range(pos1_x,pos2_x):
                            if(a[i,pos1_y]!= "  "):
                                if(i==pos1_x or i==pos2_x):
                                    continue
                                num =num +1
                        if(num != 1):
                            flag_1 = 1
                    else:
                        flag_1 =1

            elif("g" in select1):
                if((flag =="0"and pos_y2<pos_y1) or (flag =="1" and pos_y2>pos_y1)):
                    flag_1 =1
                elif((flag =="0"and pos_y1<=5) or (flag == "1" and pos_y1>=6)):
                    if(pos_x2 != pos_x1):
                        flag_1=1
                elif((abs(pos2_x-pos1_x)== 1 and pos2_y == pos1_y) or (abs(pos2_y-pos1_y)== 1 and pos2_x==pos1_x)):
                    pass
                else:
                    flag_1 = 1
            if(flag_1 ==0):
                a[pos1_x,pos1_y] = "  "
                a[pos2_x,pos2_y] = select1
                if(flag =="0"):
                   flag ="1"
                elif(flag =="1"):
                    flag ="0"
                print("player "+flag+" turn")
            else:
                flag_1 =0
                print("err3")
        else:
            print("err4")
        print(a)

if __name__ == "__main__":
    global a
    global flag
    a = np.array([["a1","b1","c1","d1","e1","d1","c1","b1","a1"],
                  ["  ","  ","  ","  ","  ","  ","  ","  ","  "],
                  ["  ","f1","  ","  ","  ","  ","  ","f1","  "],
                  ["g1","  ","g1","  ","g1","  ","g1","  ","g1"],
                  ["  ","  ","  ","  ","  ","  ","  ","  ","  "],
                  ["  ","  ","  " ,"  ","  ","  ","  ","  ","  "],
                  ["g0","  ","g0","  ","g0","  ","g0","  ","g0"],
                  ["  ","f0","  ","  ","  ","  ","  ","f0","  "],
                  ["  ","  ","  ","  ","  ","  ","  ","  ","  "],
                  ["a0","b0","c0","d0","e0","d0","c0","b0","a0"]])
    flag = "0" 
    print("player "+flag+" turn")
    print(a)
    move(1,10,1,9) 
    move(1,1,1,2) 
    move(2,10,3,8) 
    move(2,1,3,3) 
    move(3,10,4,8) 
    move(3,1,4,3) 
    move(4,10,5,9) 
    move(4,1,5,2)








