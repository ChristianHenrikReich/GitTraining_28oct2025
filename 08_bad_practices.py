"""
Bad Code Practices - File 8/10
This file demonstrates bad coding practices with serious structural issues.
"""

# Terrible imports and global pollution
from random import *
from time import *
from os import *
import *  # This would cause errors but shows bad practice

# Global variables with no organization
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = [None]*26
data1 = []
data2 = {}
data3 = [[[]]]
temp_var = 0
global_counter = 0
some_flag = True
another_flag = False
weird_list = [1,2,3,[4,5,[6,7,[8,9]]]]

# Terrible class with everything wrong
class X:
    def __init__(self,a,b,c,d,e,f,g,h,i,j):  # Too many parameters, no spacing
        self.a=a;self.b=b;self.c=c;self.d=d;self.e=e  # Semicolons in Python!
        self.f,self.g,self.h,self.i,self.j=f,g,h,i,j  # Confusing assignment
        self.stuff=[]
        self.more_stuff={}
        self.counter=0
        
    def m1(self):
        self.counter+=1;print("m1 called")  # Side effects everywhere
        
    def m2(self,val):
        self.stuff.append(val);self.counter+=1
        global global_counter
        global_counter+=1
        
    def m3(self):global temp_var;temp_var=self.counter*2;return temp_var  # One line madness

# Function that modifies everything
def chaos():
    global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
    global data1,data2,data3,temp_var,global_counter,some_flag,another_flag
    
    a=randint(1,100);b=randint(1,100);c=randint(1,100)  # Semicolons everywhere
    d,e,f=choice([1,2,3]),choice([4,5,6]),choice([7,8,9])
    
    for idx in range(10):
        obj=X(a,b,c,d,e,f,g,h,i,j) if g and h and i and j else X(1,2,3,4,5,6,7,8,9,10)
        data1.append(obj)
        obj.m1();obj.m2(randint(1,50))
        
    some_flag=not some_flag;another_flag=not another_flag

# Extremely nested and unreadable function
def nested_hell():
    global data1,data2,global_counter
    
    for item in data1:
        if item.a>50:
            if item.b<30:
                if item.c%2==0:
                    if len(item.stuff)>0:
                        for thing in item.stuff:
                            if thing>25:
                                if global_counter%3==0:
                                    if some_flag:
                                        if another_flag:
                                            data2[str(thing)]=item.counter
                                            if str(thing) in data2:
                                                if data2[str(thing)]>10:
                                                    print("deep nested result!")

# One massive function that does everything
def everything():
    global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
    global data1,data2,data3,temp_var,global_counter,some_flag,another_flag
    
    # File operations without proper handling
    try:f1=open("input.txt","r");content=f1.read();f1.close()
    except:content=""
    
    # Parse in the worst way possible
    lines=content.split("\n")
    for line in lines:
        if "," in line:
            parts=line.split(",")
            if len(parts)>=5:
                obj=X(parts[0],parts[1],parts[2],parts[3],parts[4],"","","","","")
                data1.append(obj)
    
    # Processing with terrible logic
    counter1=0;counter2=0;counter3=0
    for item in data1:
        item.m1()
        if item.a=="special":counter1+=1
        elif item.b=="important":counter2+=1
        else:counter3+=1
        
        # More nested chaos
        if counter1>counter2:
            if counter2>counter3:
                item.m2(999)
                temp_var+=item.counter
                if temp_var>1000:
                    print("threshold reached")
                    temp_var=0
                    # Reset everything randomly
                    counter1,counter2,counter3=0,0,0
                    some_flag=not some_flag
    
    # Statistics calculation inline
    total=sum([item.counter for item in data1])
    avg=total/len(data1) if len(data1)>0 else 0
    
    # Output in terrible format
    result="STATS:total="+str(total)+",avg="+str(avg)+",count="+str(len(data1))
    result+=",flag1="+str(some_flag)+",flag2="+str(another_flag)
    
    # Write output without error handling
    f2=open("output.txt","w");f2.write(result);f2.close()
    
    return result

# Function with terrible parameter handling
def func_with_too_many_params(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15):
    global temp_var
    temp_var=p1+p2+p3+p4+p5+p6+p7+p8+p9+p10+p11+p12+p13+p14+p15
    print("sum:",temp_var)
    return temp_var if temp_var>100 else 0

# Terrible menu system
def menu():
    while True:
        print("1.chaos 2.nested 3.everything 4.params 5.random 6.exit")
        try:choice=input(">")
        except:choice="6"
        
        if choice=="1":chaos();print("chaos done")
        elif choice=="2":nested_hell();print("nested done")
        elif choice=="3":result=everything();print("result:",result)
        elif choice=="4":
            params=[randint(1,10) for _ in range(15)]
            func_with_too_many_params(*params)
        elif choice=="5":
            # Random operations that make no sense
            for _ in range(randint(5,20)):
                op=choice([lambda:chaos(),lambda:nested_hell(),lambda:everything()])
                try:op()
                except:pass
        elif choice=="6":break
        else:print("bad choice")

# More terrible functions
def save_everything():
    global data1,data2,data3,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
    
    # Save to multiple files without organization
    f1=open("vars.txt","w")
    f1.write(str(a)+","+str(b)+","+str(c)+","+str(d)+","+str(e))
    f1.close()
    
    f2=open("data1.txt","w")
    for item in data1:f2.write(str(item.a)+","+str(item.b)+"\n")
    f2.close()
    
    f3=open("data2.txt","w")
    for key,val in data2.items():f3.write(key+":"+str(val)+"\n")
    f3.close()

def load_everything():
    global data1,data2,a,b,c,d,e
    
    try:
        f1=open("vars.txt","r");line=f1.read();f1.close()
        parts=line.split(",")
        a,b,c,d,e=int(parts[0]),int(parts[1]),int(parts[2]),int(parts[3]),int(parts[4])
    except:a,b,c,d,e=1,2,3,4,5
    
    try:
        f2=open("data1.txt","r");lines=f2.readlines();f2.close()
        for line in lines:
            parts=line.strip().split(",")
            if len(parts)>=2:
                obj=X(parts[0],parts[1],"","","","","","","","")
                data1.append(obj)
    except:pass

# Terrible initialization
def init():
    global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
    global data1,data2,data3,temp_var,global_counter,some_flag,another_flag
    
    # Initialize everything randomly
    a,b,c,d,e,f,g,h,i,j=randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)
    k,l,m,n,o,p,q,r,s,t=choice("abcde"),choice("fghij"),choice("klmno"),choice("pqrst"),choice("uvwxy"),choice("z"),randint(1,100),randint(1,100),randint(1,100),randint(1,100)
    u,v,w,x,y,z=True,False,None,"string",123.456,[1,2,3]
    
    # Create random initial data
    for idx in range(randint(5,15)):
        obj=X(randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),"x","y","z","a","b")
        data1.append(obj)
        obj.m1();obj.m2(randint(1,50))

# Main function with terrible structure
def main():
    print("SYSTEM STARTING...")
    init()
    load_everything()
    
    while True:
        try:
            print("\nMAIN MENU:")
            print("1. Run Menu System")
            print("2. Save All Data") 
            print("3. Generate Random Data")
            print("4. Reset Everything")
            print("5. Quit")
            
            choice=input("Choice: ")
            
            if choice=="1":menu()
            elif choice=="2":save_everything();print("saved")
            elif choice=="3":
                chaos()
                for _ in range(10):everything()
                print("random data generated")
            elif choice=="4":
                data1.clear();data2.clear()
                init()
                print("reset complete")
            elif choice=="5":
                save_everything()
                print("goodbye")
                break
            else:print("invalid choice")
                
        except Exception as ex:
            print("ERROR:",str(ex))
            continue

if __name__=="__main__":main()