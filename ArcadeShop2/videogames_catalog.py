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
from Videogames import Videogame
class VideogamesCatalog:
    """This class represents a catalog of videogames."""

    __instance = None

    @staticmethod
    def get_instance():
        """static method to get the instance of the class"""
        if VideogamesCatalog.__instance is None:
            VideogamesCatalog.__instance = VideogamesCatalog()
        return VideogamesCatalog.__instance

    def __init__(self):
        """private constructor to prevent the creation of new objects"""
        if VideogamesCatalog.__instance is not None:
            raise RuntimeError("This class is a singleton! Use getInstance() instead")
        else:
            super_mario = Videogame(1, "Super Mario Bros", "Shigeru Miyamoto", "Shigeru Miyamoto", "Platform", 60.0, 1985)
            the_legend_of_zelda = Videogame(2, "The Legend of Zelda", "Shigeru Miyamoto", "Shigeru Miyamoto", "Action-adventure", 70.0, 1986)
            donkey_kong = Videogame(3, "Donkey Kong", "Shigeru Miyamoto", "Shigeru Miyamoto", "Platform", 50.0, 1981)
            self.videogames = [super_mario, the_legend_of_zelda, donkey_kong]

    def add_videogame(self, videogame):
        """Adds a video game to the catalog."""
        self.videogames.append(videogame)

    def show_videogames(self):
        """this method shows the list of videogames"""
        for videogame in self.videogames:
            print(videogame)

    def search_videogame(self, code):
        """this method searches a video game by its code"""
        for videogame in self.videogames:
            if videogame.code == code:
                return videogame
        return None
