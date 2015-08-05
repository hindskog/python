class Product(object):
	price = 0
	count = 0
	vat = 0

	def price_with_vat(self):
		return self.price * self.count * self.vat




robot = Product()
robot.price = 900
robot.count = 2
robot.vat = 1.25

print robot.price_with_vat()

