import random
class Employee:
	id = "";
	firstName = "";
	lastName = "";
	sales = 0;
	manager = None;
	employeesManaging = [];

	def __init__(self, firstName, lastName, manager):
		self.firstName = firstName;
		self.lastName = lastName;
		self.sales = self.generateSalesNumber();
		self.manager = manager;
		self.id = self.generateId();

	def getFullName(self):
		return self.firstName + " " + self.lastName;

	def generateSalesNumber(self):
		return random.randrange(0, 99);

	def setMinManageEmployee(self, min):
		self.minManageEmployee = min;

	def setMaxManageEmployee(self, max):
		self.maxManageEmployee = max;

	def generateId(self):
		return self.firstName + "." + self.lastName + str(random.randrange(0,10));

	def addEmployeeToManage(self, employee):
		employee.manager = self;
		self.employeesManaging.append(employee);

	def __repr__(self):
		return self.getFullName();