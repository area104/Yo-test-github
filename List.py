#การใช้งาน Fucntion Bluein List หรือ []

[] # คือ Fucntion Blidinอีกชนิดหนึ่ง ใช้ในการเก็บ Oject ได้หลายชนิดใน ลิส ๆ เดียว


#ยกตัวอย่างเช่น
list = ["a",5,5.6,("a,b,c"),[5+6],(8,9)]


#เพิ่ม Oject ลงไปใน list ด้วยคำนั่ง append
list.append("cat")


#ลบข้ลมูลออกจาก List ด้วย method .pop
list.pop(0)


#แสดงค่าด้วยคำสั่ง print
print(list)

print(len(list))