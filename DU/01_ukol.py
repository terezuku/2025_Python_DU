import math

# lokalita
class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

# nemovitost
class Property:
    def __init__(self, locality):
        self.locality = locality

# pozemek
class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
    
    def __str__(self):
        return f"Typ pozemku '{self.estate_type}' se nachází v lokalitě {self.locality.name}, má {self.area} m2 a jeho daň činí {self.calculate_tax()}. "

    # koeficienty
    coefficients = {"land": 0.85, "building site": 9, "forrest": 0.35, "garden": 2}

    def calculate_tax(self):
        if self.estate_type in self.coefficients:
            estate_coeff = self.coefficients[self.estate_type]

        tax = self.area * estate_coeff * self.locality.locality_coefficient
        return math.ceil(tax)

# byty, domy, stavby
class Residence(Property):
    def __init__(self, locality, area, commercial=False):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def __str__(self):
        if self.commercial==False:
            return f"Stavba se nachází v lokalitě {self.locality.name}, má {self.area} m2 a jeho daň činí {self.calculate_tax()}. "
        else:
            return f"Stavba se nachází v lokalitě {self.locality.name}, má {self.area} m2 a jeho daň činí {self.calculate_tax()}. Slouží ke komerčním účelům. "

    def calculate_tax(self):
        base_tax = self.area * self.locality.locality_coefficient * 15
        if self.commercial:
            base_tax = base_tax * 2
        return math.ceil(base_tax)

manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3)
estate1 = Estate(manetin, "land", 900)
residence1 = Residence(manetin, 120)
residence2 = Residence(brno, 90, commercial=True)

print(f"Daň za zemědělský pozemek v Manětíně činí: {estate1.calculate_tax()}.")
print(f"Daň za dům v Manětíně činí: {residence1.calculate_tax()}.")              
print(f"Daň za kancelář v Brně činí: {residence2.calculate_tax()}.")
print("*" * 50)
# bonus
print(estate1)
print(residence1)
print(residence2)
