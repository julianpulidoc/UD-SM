"""
this module has the classes that represent the elements of an arcade machine and
a shop arcade machine. 

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
from abc import ABC

class AbstractCustomElements(ABC):
    """
    This class represents the behavior of an abstract element of an arcade
    machine.
    """
    def __init__(self, name:str, Type:str):
        """
        This method initializes the attributes of the class.
        """
        self.name = name
        self.Type = Type

    def get_name(self) -> str:
        """
        this method returns the name of the element.

        Returns:
            A string with the name of the element.
        """
        return self.name

    
    def get_type(self) -> str:
        """
        this method returns the type of the element.

        Returns:
            A string with the type of the element.
        """
        return self.Type


    def set_name(self, name:str):
        """
        this method sets the name of the element.

        Args:  
            name (str): The name of the element.
        """
        self.name = name


    
    def set_type(self, Type:str):
        """
        this method sets the type of the element.
        
        Args:
            Type (str): The type of the element.
        """
        self.Type = Type

    def __str__(self):
        """
        this method returns a string representation of the object.
        """
        return f"Name: {self.name}, Type: {self.Type}"

class Videogame(AbstractCustomElements):
    """
    This class represents a videogame in an arcade machine.
    """
    def __init__(self, code:int, name: str, Type: str):
        """
        this method initializes the attributes of the class.
        """
        self.code = code
        super().__init__(name, Type)
    
    def get_code(self) -> int:
        """
        this method returns the code of the videogame.

        Returns:
            An integer with the code of the videogame.
        """
        return self.code
    
    def set_code(self, code:int):
        """
        this method sets the code of the videogame.

        Args:
            code (int): The code of the videogame.
        """
        self.code = code
    
    def __str__(self):
        """
        this method returns a string representation of the object.
        """
        return f"Name: {self.name}, Type: {self.Type}, Code: {self.code}"

class Prints(AbstractCustomElements):

    def __init__ (self, name: str, Type: str, price:float):
        """
        this method initializes the attributes of the class.
        """
        self.price = price
        super().__init__(name, Type)

    def get_price(self) -> float:
        """
        this method returns the price of the prints.

        Returns:
            A float with the price of the prints.
        """
        return self.price
    
    def set_price(self, price:float):
        """
        this method sets the price of the prints.

        Args:
            price (float): The price of the prints.
        """
        self.price = price
    
    def __str__(self):
        """
        this method returns a string representation of the object.
        """
        return f"Name: {self.name}, Type: {self.Type}, Price: {self.price}" 
    
class Material(AbstractCustomElements):
    
    def __init__(self, name: str, Type: str, price: float):
        """
        this method initializes the attributes of the class.
        """
        self.price = price
        super().__init__(name, Type)

    def get_price(self) -> float:
        """
        this method returns the price of the prints.

        Returns:
            A float with the price of the prints.
        """
        return self.price
    
    def set_price(self, price:float):
        """
        this method sets the price of the prints.

        Args:
            price (float): The price of the prints.
        """
        self.price = price
    
    def __str__(self):
        """
        this method returns a string representation of the object.
        """
        return f"Name: {self.name}, Type: {self.Type}, Price: {self.price}" 

class Machine():
    """
    This class represents an arcade machine.
    """
    def __init__(self, elements:list):
        """
        this method initializes the attributes of the class.
        """
        self.elements = elements

    def set_elements(self, element:AbstractCustomElements):
        """
        this method adds an element to the machine.

        Args:
            element (AbstractCustomElements): The element to add.
        """
        self.elements.append(element)
    
    def get_elements(self) -> list:
        """
        this method returns the elements of the machine.

        Returns:
            A list with the elements of the machine.
        """
        return self.elements
    
    def __str__(self):
        """
        this method returns a string representation of the object.
        """
        elements = "machine elements:\n"
        for element in self.elements:
            elements += f"{element}\n"
        return elements
    
class Customer():

    def __init__(self, name:str, phone:str, address: str):
        """
        this method initializes the attributes of the class.
        """
        self.name = name
        self.phone = phone
        self.address = address
    
    def get_name(self) -> str:
        """
        this method returns the name of the customer.

        Returns:
            A string with the name of the customer.
        """
        return self.name
    
    def get_phone(self) -> str:
        """
        this method returns the phone of the customer.

        Returns:
            A string with the phone of the customer.
        """
        return self.phone
    
    def get_address(self) -> str:
        """
        this method returns the address of the customer.

        Returns:
            A string with the address of the customer.
        """
        return self.address
    
    def set_name(self, name:str):
        """
        this method sets the name of the customer.

        Args:
            name (str): The name of the customer.
        """
        self.name = name
    
    def set_phone(self, phone:str):
        """
        this method sets the phone of the customer.

        Args:
            phone (str): The phone of the customer.
        """
        self.phone = phone
    
    def set_address(self, address:str):
        """
        this method sets the address of the customer.

        Args:
            address (str): The address of the customer.
        """
        self.address = address

    def __str__(self):
        """
        this method returns a string representation of the object.
        """
        return f"Name: {self.name}, Phone: {self.phone}, Address: {self.address}"

class Purchase():
    """
    This class represents a purchase in the arcade shop.
    """

    def __init__(self, customer:Customer, machine:Machine, total:float):
        """
        this method initializes the attributes of the class.
        """
        self.customer = customer
        self.machine = machine
        self.total = total
    
    def calculate_total(self, machinef:Machine) -> float:
        """
        this method calculates the total of the purchase.

        Args:
            machinef (Machine): The machine with the elements of the purchase.

        Returns:
            A float with the total of the purchase.
        """
        total = 0
        for element in machinef.get_elements():
            if isinstance(element, Prints):
                total += element.get_price()
            elif isinstance(element, Material):
                total += element.get_price()
        return total
    def __str__(self) -> str:
        """
        this method returns a string representation of the object.
        """
        return f"Customer: {self.customer},\n Machine: {self.machine},\n Total: {self.total}"

class VideogameCatalogue():
    """
    this class represents the videogame catalogue.
    """
    def __init__(self, videogames:list):
        """
        this method initializes the attributes of the class.
        """
        self.videogames = videogames
    
    def set_videogames(self, videogame:Videogame):
        """
        this method adds a videogame to the catalogue.

        Args:
            videogame (Videogame): The videogame to add.
        """
        self.videogames.append(videogame)
    
    def get_videogame(self, codeGame:int) -> Videogame:
        """
        this method returns the videogames of the catalogue.

        Returns:
            A list with the videogames of the catalogue.
        """
        for videogame in self.videogames:
            if videogame.get_code() == codeGame:
                return videogame
            else:
                return None
    
    def __str__(self):
        """
        this method returns a string representation of the object.
        """
        videogames = "videogame catalogue:\n"
        for videogame in self.videogames:
            videogames += f"{videogame}\n"
        return videogames
    