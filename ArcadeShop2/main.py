from machines import Director, MachineBuilder, DanceRevolutionBuilder, ClassicalArcadeBuilder, ShootingMachineBuilder, RacingMachineBuilder, VirtualRealityBuilder
from Videogames import VideogameFactory
from videogames_catalog import VideogamesCatalog

class Customer:
    """This class represents a customer in the application."""
    def __init__(self, name: str, address: str):
        self.__name = name
        self.__address = address

    def set_name(self, name: str):
        """This method sets the name of the customer."""
        self.__name = name

    def set_address(self, address: str):
        """This method sets the address of the customer."""
        self.__address = address

    def __str__(self):
        return f"Name: {self.__name}, Address: {self.__address}"


class Purchase:
    """This class represents the behavior of a purchase in the application."""

    def __init__(self, machine: MachineBuilder, customer: Customer, catalog:VideogamesCatalog, total: float):
        self.__machine = machine
        self.__customer = customer
        self.__total = total
        self.__videogames = catalog.get_instance()

    Menu = "1. Buy Machine\n 2.Show machines\n 3.Exit"

    def select_material(self):
        """This method allows the customer to select the material of the machine."""
        print("Choose the material of the machine:\n 1. Wood\n 2. Aluminium\n 3. Carbon fiber")
        option = int(input())
        if option == 1:
            self.__machine.set_material("wood")
            print("Material selected")
        elif option == 2:
            self.__machine.set_material("aluminium")
            print("Material selected")
        elif option == 3:
            self.__machine.set_material("carbon fiber")
            print("Material selected")
        else:
            print("Invalid option")
    
    def buy_machine(self):
        """This method allows the customer to buy a machine."""

        print("Choose the predefined machine:\n 1. Dance Revolution\
               2. Classical Arcade\n 3. Shotting machine\n 4. Racing machine\
              \n5. Virtual Reality")
        option = int(input())
        if option == 1:
            director = Director(DanceRevolutionBuilder())
            self.__machine = director.make()
            self.select_material()
            self.add_videogame_to_machine()
            self.calculate_atributes_machine()
            self.calculate_total()
            self.__machine.set_color(input("Insert the color of the machine:"))
            self.__machine.set_name(input("Insert the name of the machine:"))
        elif option == 2:
            director = Director(ClassicalArcadeBuilder())
            self.__machine = director.make()
            self.select_material()
            self.add_videogame_to_machine()
            self.calculate_atributes_machine()
            self.calculate_total()
            self.__machine.set_color(input("Insert the color of the machine:"))
            self.__machine.set_name(input("Insert the name of the machine:"))
        elif option == 3:
            director = Director(ShootingMachineBuilder())
            self.__machine = director.make()
            self.select_material()
            self.add_videogame_to_machine()
            self.calculate_atributes_machine()
            self.calculate_total()
            self.__machine.set_color(input("Insert the color of the machine:"))
            self.__machine.set_name(input("Insert the name of the machine:"))
        elif option == 4:
            director = Director(RacingMachineBuilder())
            self.__machine = director.make()
            self.select_material()
            self.add_videogame_to_machine()
            self.calculate_atributes_machine()
            self.calculate_total()
            self.__machine.set_color(input("Insert the color of the machine:"))
            self.__machine.set_name(input("Insert the name of the machine:"))
        elif option == 5:
            director = Director(VirtualRealityBuilder())
            self.__machine = director.make()
            self.select_material()
            self.add_videogame_to_machine()
            self.calculate_atributes_machine()
            self.calculate_total()
            self.__machine.set_color(input("Insert the color of the machine:"))
            self.__machine.set_name(input("Insert the name of the machine:"))
        else:
            print("Invalid option")
        

    
    def calculate_atributes_machine(self):
        """This method calculates the attributes of the machine\
            according to the material of the machine."""
        if self.__machine.material == "wood":
            self.__machine.set_base_price(self.__machine.get_base_price() * 0.95)
            self.__machine.set_weight(self.__machine.get_weight() * 1.1)
            self.__machine.set_power_consumption(self.__machine.get_power_consumption() * 1.15) 
        elif self.__machine.material == "aluminium":
            self.__machine.set_base_price(self.__machine.get_base_price() * 1.10)
            self.__machine.set_weight(self.__machine.get_weight() * 0.95)
        elif self.__machine.material == "carbon fiber":
            self.__machine.set_base_price(self.__machine.get_base_price() * 1.20)
            self.__machine.set_weight(self.__machine.get_weight() * 0.85)
            self.__machine.set_power_consumption(self.__machine.get_power_consumption() * 0.9)
        
    def calculate_total(self):
        """This method calculates the total of the purchase."""
        for videogame in self.__machine.get_videogames():
            self.__total += videogame.get_price()
        self.__total += self.__machine.get_total_price()
        return self.__total
    
    
    def add_videogame_to_machine(self):
        """This method adds a videogame to the machine."""
        self.__videogames.show_videogames()
        code = int(input("Insert the code of the videogame:"))
        if self.__videogames.search_videogame(code) is not None:
            print("Choose the quality of the videogame: 1. Standard 2. High")
            quality = int(input())
            if quality == 1:
                self.__machine.add_videogame(VideogameFactory.modify_videogame("standard", self.__videogames.search_videogame(code)))
            elif quality == 2:
                self.__machine.add_videogame(VideogameFactory.modify_videogame("high", self.__videogames.search_videogame(code)))
            else:
                print("Invalid option")

    
    def __str__(self):
        return f"Customer: {self.__customer}, Machine: {self.__machine},\
                 Total: {self.__total}"



class Main:
    @staticmethod
    def run():
        # Crear el catálogo de videojuegos
        videogames_catalog = VideogamesCatalog()

        # Crear un cliente
        customer = Customer("John Doe", "123 Main St")

        # Crear una compra
        purchase = Purchase(None, customer, videogames_catalog, 0.0)

        # Ejecutar la compra
        purchase.buy_machine()

        # Mostrar la compra final
        print(purchase)


if __name__ == "__main__":
    Main.run()