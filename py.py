def main():
    while 1==1:
        x,y = p.position()
        y=(450-y)*7/9
        x=(x-800)/8
        ls=int(x+y)
 
        rs=int(y-x)
        dis1=r.get_dist(31)
        dis2=r.get_dist(32)
        disc1=(dis1-dis2)
        disc2=(dis2-dis1)
        if disc1 > 50:
            ls=ls-100
            r.set_motors(1,ls,2,ls,3,rs,4,rs)
        else:
            if disc2 > 50:
                rs=rs-100
                r.set_motors(1,ls,2,ls,3,rs,4,rs)
            else:
                r.set_motors(1,ls,2,ls,3,rs,4,rs)
                


 
import sys
import irobotq_robotdriver as r
import pyautogui as p
if __name__ == '__main__':

    try:
        ret=r.init(sys.argv[1],sys.argv[2],int(sys.argv[3]))
        if(ret == 0):
            main()
            r.over()
            print("机器人程序运行结束")
        else:
            print('初始化错误，错误码:%d' % ret)
        print('按任意键退出')
        v=input()
    except Exception as e:
        print (e)
        print('按任意键退出')
        v=input()