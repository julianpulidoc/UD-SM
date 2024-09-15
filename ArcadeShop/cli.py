"""
this module has th CLI of the arcade machine shop.

Author: Julian David Pulido Carreño <judpulidoc@udistrital.edu.co>

This file is part of ArcadeShop.

ArcadeShop is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
ArcadeShop is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
License for more details.
You should have received a copy of the GNU General Public License along with
ArcadeShop. If not, see <https://www.gnu.org/licenses/>.
"""

from ArcadeShop_classes import Machine, Videogame
from ArcadeShop_classes import (Prints, Material, Customer, Purchase,
VideogameCatalogue)

if __name__ == "__main__":
    # Create videogames
    game1 = Videogame(code="1", name="Super Mario Bros", Type="arcade")
    game2 = Videogame(code="2", name="Pac-man", Type="arcade")
    # Create a videogame catalogue
    catalogue = VideogameCatalogue(videogames=[game1, game2])
    # Create Materials
    carbonFiber = Material(name="Carbon Fiber", Type="Light", price=500)
    wood = Material(name="Wood", Type="Heavy", price=200)
    aluminium = Material(name="Aluminium", Type="Durable", price=300)
    # Create Prints
    printSF = Prints(name="Street Fighter", Type="Gamer", price=100)
    printMK = Prints(name="Mortal Kombat", Type="Gamer", price=100)
    printCF = Prints(name="Carbon Fiber", Type="Material", price=50)
    # Create a machine
    machine = Machine(elements=[])
    # Create a Purchase
    purchase = Purchase(customer=None, machine=None, total=0)


    menu = """ 
    1. Create a machine
    2. Salir \n
    """
    menu2 = """\nPlease select and option:
            1. see Video-Games
            2. select a Video-Game
            3.select a Material
            4. select a Print
            5. Finish Purchase
            6. Exit\n"""
    
    option = int(input(menu))
    while option != 2:
        if option == 1:
            inputOption = int(input(menu2))
            while inputOption != 6:
                if inputOption == 1:
                    print(catalogue)
                elif inputOption == 2:
                    code = input("Please enter the code of the videogame you want to add: ")
                    machine.set_elements(catalogue.get_videogame(code))
                elif inputOption == 3:
                    material =int(input("Please select the material you want to add: \n 1. Carbon Fiber \n 2. Wood\n 3. Aluminium \n"))
                    if material == 1:
                        machine.set_elements(carbonFiber)
                    elif material == 2:
                        machine.set_elements(wood)
                    elif material == 3:
                        machine.set_elements(aluminium)
                    else:
                        print("Please select a valid option")
                elif inputOption == 4:
                    printOption = int(input("Please select the print you want to add: \n 1. Street Fighter \n 2.Mortal Kombat \n 3. Carbon Fiber \n"))
                    if printOption == 1:
                        machine.set_elements(printSF)
                    elif printOption == 2:
                        machine.set_elements(printMK)
                    elif printOption == 3:
                        machine.set_elements(printCF)
                    else:
                        print("Please select a valid option")
                elif inputOption == 5:
                    print("please enter your information")
                    nameC = input("Name: ")
                    phoneC = input("Phone: ")
                    addressC = input("Address: ")
                    customer = Customer(name=nameC, phone=phoneC, address=addressC)
                    purchasef = Purchase(customer=customer, machine=machine, total=purchase.calculate_total(machine))
                    print("Successful purchase")
                    print(purchasef)
                    break
                else:
                    print("Please select a valid option")
                inputOption = int(input(menu2))
        else:
            print("Please select a valid option")
    
        option = int(input(menu))