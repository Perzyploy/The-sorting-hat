# The sortig hat.py

class Wizard:
	def __init__(self,name,age,gender):
		self.name = name
		self.age = age 
		self.gender = gender

	def hello(self):
		print('สวัสดี ฉันชื่อ {} วันนี้ฉันจะมาคัดเลือกบ้านโดยหมวดคัดสรร'.format(self.name))



class Sortinghat:
	def __init__(self,color):
		self.color = color

	def random(self):
		if self.color == 'red':
			print('ไปบ้านกริฟฟินดอร์')
		elif self.color == 'green':
			print('ไปบ้านสลิธีริน')
		elif self.color == 'yellow':
			print('ไปบ้านฮัฟเฟิลพัฟ')
		elif self.color == 'blue':
			print('ไปบ้านเรเวนคลอ')
		else:
			print('คุณเป็นมักเกิล ไม่สามารถเข้าเรียนได้')


if __name__== '__main__':
	student1 = Wizard('Harry Potter','13','ชาย')
	student2 = Wizard('Lucius Malfoy','13','ชาย')
	student3 = Wizard('ลุงตู่','68','ชาย')

	color1 = Sortinghat('red')
	color2 = Sortinghat('green')
	color3 = Sortinghat('')

print('--------')
student1.hello()
color1.random()
print('--------')
student2.hello()
color2.random()
print('--------')
student3.hello()
color3.random()
