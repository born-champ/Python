class User:
	user_count = 0
	def __init__(self, name, age):
		self.name = name 
		self.__age = age
		User.user_count +=1

	def get_name(self):
		return self.name

	def get_age(self):
		return self.__age

	def set_gender(self, gender):
		self.gender = gender 
		return 
	def get_gender(self):
		return self.gender

	def get_first_name(self):
		return self.name.split(" ")[0]

	def get_last_name(self):
		return self.name.split(" ")[1]

	def create_user_name(self):
		return  self.name.split(" ")[0]+str(self.__age)

class Employee(User):
	employee_count=0

	def __init__(self, name, age, post):
		super().__init__()
		self.post = post
		Employee.employee_count+=1

	def get_post(self):
		return self.post

	def get_org(self):
		return self.org

	def set_org(self, org):
		self.org = org