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


class Videogame:
    """This class represents a videogame."""

    def __init__(
        self,
        code: int,
        name: str,
        storytelling_creator: str,
        graphics_creator: str,
        category: str,
        price: float,
        year: int,
    ):
        self.code = code
        self.name = name
        self.price = price
        self.category = category
        self.graphics_creator = graphics_creator
        self.storytelling_creator = storytelling_creator
        self.year = year

    def get_price(self):
        """this method returns the price of the videogame"""
        return self.price

    def __str__(self):
        return f"Code: {self.code}, Name: {self.name}, Price: {self.price},\
             Category: {self.category}, Graphics Creator:\
             {self.graphics_creator}, Storytelling Creator:\
            {self.storytelling_creator}, Year: {self.year}"


class VideogameFactory:
    """This class represents a factory of videogames."""

    @staticmethod
    def modify_videogame(
        quality: str,
        videogame: Videogame,
    ):
        """this method modifies the price of a videogame according to its quality"""
        if quality == "standard":
            videogame.price = videogame.price
        elif quality == "high":
            videogame.price = videogame.price * 1.10
        return videogame
