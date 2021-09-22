import Joeclass as jc


car1 = jc.Car("Honda", "civic", 2010)
cus1 = jc.Customer("smith","123 baylor ave", "999-999-9999")
serviceq = jc.ServiceQuote(800, 1500)

car1.set_model("challenger")
print(car1.get_make(), car1.get_model(), car1.get_year())

cus1.set_address("321 1st st")
print(cus1.get_name(),cus1.get_address(),cus1.get_phone())

print(serviceq.get_sales_tax())
serviceq.set_labor_charges(900)
print(serviceq.get_sales_tax())