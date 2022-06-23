# Method Fucntion เป็นการจำ Fucntion ไปใช้เพื่อการเปลี่ยนแปลง ค่าบางอย่างสำหรับ oject ที่เป็น string

h = "Hello World My world is happy" #h เก็บค่าตัวแปล Hello World My world is happy

print(h) #แสดงประโยคทั้งหมด
print(h.split()) #Method split  แยกคำออกจากกันคั้นด้วยลูกน้ำ ,
m=(h.split("l"))#Method split แยกคำด้วยตัว l

q="".join(m)
print(q)
print("จำนวนที่เหลืออยู่:",len(q))
print("จำนวนคงเหลือทั้งหมด",len(h))
print(h.upper())# Method upper วิธีใช้ จะเปลี่ยนคำตัวอักษรใช้ทั้งหมด
print(h.lower()) #ทำให้เป็นตัวเล็ก
