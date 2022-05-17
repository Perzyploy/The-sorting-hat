# oopbasic.py

class Student:

	def __init__(self,name,age,gender):
		self.name = name
		self.age = age
		self.gender = gender

	def study(self):
		print('{}กำลังเรียนอยู่...'.format(self.name))

	def sawatdee(self):
		if self.gender == 'ชาย':
			tail = 'ครับ'
			callme = 'ผม'
		else:
			tail = 'ค่ะ'
			callme = 'หนู'

		print('สวัสดี{}{}ชื่อ{}'.format(tail,callme,self.name)) # เติมหางเสียง ค่ะ ครับ


class SpecialStudent(Student): # ดึงข้อมูลมากจาก class Student

	def __init__(self,name,age,gender,parent):
		super().__init__(name,age,gender) #สือทอด class Student มา 3 อันนี้เคยประกาศไปแล้ว ไม่ต้องประกาศใหม่
		self.parent = parent # อันนี้ใน class student ยังไม่มี เลยต้องประกาศเพิ่ม

	def hello(self, person='เพื่อน'): # ตั้งค่า default เป็นคำว่าเพื่อน ถ้าจะเปลี่ยนเป็นคำอื่น พิมพ์ลงไปตรงวงเล็บหลังฟังก์ชันได้เลย
		if person == 'เพื่อน':
			print('เฮ้ย! ว่ายังไง? มีขนมไหม?')
		else:
			print('รีบเดินหนีดีกว่า ไม่อยากคุย')

	def sawatdee(self):
		print('หวัดดี ชื่อ{}'.format(self.name))

	def myfather(self):
		print('รู้ไหม? ผมลูกใคร')
		print('ผมลูก{}'.format(self.parent))


class Teacher:

	def __init__(self,name,gender,subject):
		self.name = name 
		self.gender = gender
		self.subject = subject


	def teach(self):
		print('คุณครู{}กำลังสอนวิชา{}'.format(self.name,self.subject))

	


print('NAME:',__name__) # name ในที่นี้คือชื่อไฟล์
if __name__== '__main__': # ใส่เพื่อตรวจสอบว่าชื่อไฟล์นี้คือ main part ของโปรแกรมรึเปล่า ส่วนมากจะใช้เป็นส่วนเสริมมากกว่า ถ้าเป็นส่วนเสริมเวลา import ไปใช้ข้างนอกมันจะไม่รัน
	student1 = Student('สมชาย','14','ชาย')
	student2 = Student('สมศรี','14','หญิง')
	special_student = SpecialStudent('จ้อย','16','ชาย','นายก อบต.')

	teacher1 = Teacher('จอห์น','ชาย','ภาษาอังกฤษ')
	print(teacher1.name)
	print(teacher1.subject)

	print('---8.30 น.----')
	student1.sawatdee()
	student2.sawatdee()
	teacher1.teach()
	student1.study()
	student2.study()
	print('----8.45 น.---')
	special_student.sawatdee()
	special_student.hello('ครู')
	print('เดินไปที่โต๊ะตัวเอง')
	special_student.hello()
	print('ครู{}! ขอเกรดดีๆหน่อย'.format(teacher1.name))
	special_student.myfather()