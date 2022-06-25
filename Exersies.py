#lesson_of_two_evens(2,4) >>2
#lesson_of_two_evens(2,5) >>5

#1.รับค่ามาจากตัวแปร int1
#2.รับค่ามาจากตัวแปร int2
#3.เปลี่ยนเทียบค่า int1>int2 แสดงค่า ที่น้อยกว่า
#4.เปลี่ยนเทียบค่า int1>int2 แสดงค่า ทีมากกว่า



def pynumber (int1,int2):
    if int1>int2:
        print("ตัวเลขที่น้อยกว่า = " ,int1)
    elif int1<int2:
        print("ตัวลขที่มากกว่า =", int2)
    else:
        print("มีค่าเท่ากัน")

int1= input("ตัวเลขที่ 1 : ")
int2= input("ตัวเลขที่ 2 : ")
pynumber(int1,int2)