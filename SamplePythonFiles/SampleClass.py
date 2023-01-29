class Employee():


	def __init__(self, first, last, pay, gender):

		self.first = first
		self.last = last
		self.pay = pay
		self.gender = gender
		print("*" * 80)


	def get_fullname(self):
		return f"Hallo! Ich bin {self.last}-{self.first}. Auf Wiedersehen."


	def get_email(self):
		if self.gender == 'Mann':
			return f"Mein email ist {self.first}.{self.last}@mercedes.com"
		elif self.gender == 'Frau':
			return f"Meine email ist {self.first}.{self.last}@mercedes.com"


if __name__ == '__main__':
	E1 = Employee('Benjamin', 'Bestle', 120000, 'Mann')
	print(E1.get_fullname())
	print(E1.get_email())

	E2 = Employee('Emily', 'Witte', 120000, 'Frau')
	print(E2.get_fullname())
	print(E2.get_email())