
class Customer:

    def __init__(self, nam, add, phon):
        self.__name = nam
        self.__address = add
        self.__phone = phon

    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_phone(self, phone):
        self.__phone = phone
    
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_phone(self):
        return self.__phone

class Car:
    def __init__(self, mak, mod, yea):
        self.__make = mak
        self.__model = mod
        self.__year = yea

    def set_make(self, make):
        self.__make = make
    def set_model(self, mod):
        self.__model = mod
    def set_year(self, y):
        self.__year = y

    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year

class ServiceQuote:
    def __init__(self, pcharge, lcharge):
        self.__parts_charges = pcharge
        self.__labor_charges = lcharge
        self.__sales_tax = 0

    def set_parts_charges(self, pchar):
        self.__parts_charges = pchar
    def set_labor_charges(self,lcharge):
        self.__labor_charges = lcharge

    def get_parts_charges(self):
        return self.__parts_charges
    def get_labor_charges(self):
        return self.__labor_charges
    def get_sales_tax(self):
        val = float(self.__parts_charges + self.__labor_charges)*.08
        return val

    def get_total_charges(self):
        total = self.__sales_tax + self.__labor_charges + self.__parts_charges
        return total