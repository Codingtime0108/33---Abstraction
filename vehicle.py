class BMW():
    def parts(self):
        print("Has around 20,000 individual parts")

    def tyre(self):
        print("BMWs can use a variety of tire types and brands, including tubeless, tube, and run-flat tires.")

    def cost(self):
        print("As of today, the minimum cost of a new BMW is around $40,000")

class Lamborghini():
    def parts(self):
        print("A Lamborghini consists of thousands of individual parts")

    def tyre(self):
        print("Lamborghini models typically use Pirelli P Zero tires.")

    def cost(self):
        print("As of today, the minimum cost of a Lamborghini is around $221,506")

obj_bmw = BMW()
obj_lam = Lamborghini()

for country in (obj_bmw, obj_lam):
    country.parts()
    country.tyre()
    country.cost()