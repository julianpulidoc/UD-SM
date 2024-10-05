"""
this module has the classes that represent the machines of an arcade shop with a builder pattern.

Author: Julian David Pulido Carreño <judpulidoc@udistrital.edu.co>

This file is part of ArcadeShop2.

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

from abc import ABC, abstractmethod
from typing import List
from Videogames import Videogame


# ===================== Machines =====================#
class DanceRevolution:
    """A Dance Revolution machine."""

    def __init__(self):
        self.__name = None
        self.__color = None
        self.__material = None
        self.__dimensions = None
        self.__weight = None
        self.__power_consumption = None
        self.__memory = None
        self.__base_price = None
        self.__videogames = None
        self.__processor = None
        self.__difficulties = None
        self.__arrows = None
        self.__controls_price = None

    def get_total_price(self) -> float:
        """Get the total price of the machine."""
        return self.__base_price + self.__controls_price

    def set_name(self, name: str):
        """Set the name of the machine."""
        self.__name = name

    def set_color(self, color: str):
        """Set the color of the machine."""
        self.__color = color

    def set_material(self, material: str):
        """Set the material of the machine."""
        self.__material = material

    def set_dimensions(self, dimensions: str):
        """Set the dimensions of the machine."""
        self.__dimensions = dimensions

    def set_weight(self, weight: float):
        """Set the weight of the machine."""
        self.__weight = weight

    def get_weight(self) -> float:
        """Get the weight of the machine."""
        return self.__weight

    def set_power_consumption(self, power_consumption: float):
        """Set the power consumption of the machine."""
        self.__power_consumption = power_consumption

    def get_power_consumption(self) -> float:
        """Get the power consumption of the machine."""
        return self.__power_consumption

    def set_memory(self, memory: str):
        """Set the memory of the machine."""
        self.__memory = memory

    def set_base_price(self, base_price: float):
        """Set the base price of the machine."""
        self.__base_price = base_price

    def get_base_price(self) -> float:
        """Get the base price of the machine."""
        return self.__base_price

    def set_videogames(self, videogame: Videogame):
        """Set the videogames of the machine."""
        self.__videogames.append(videogame)

    def get_videogames(self) -> List[Videogame]:
        """Get the videogames of the machine."""
        return self.__videogames

    def set_processor(self, processor: str):
        """Set the processor of the machine."""
        self.__processor = processor

    def set_difficulties(self, difficulties: List[str]):
        """Set the difficulties of the machine."""
        self.__difficulties = difficulties

    def set_arrows(self, arrows: str):
        """Set the arrows of the machine."""
        self.__arrows = arrows

    def set_controls_price(self, controls_price: float):
        """Set the controls price of the machine."""
        self.__controls_price = controls_price

    def __str__(self):
        return f"Name: {self.__name}\nColor: {self.__color}\n\
                Material: {self.__material}\nDimensions: {self.__dimensions}\n\
                Weight: {self.__weight}\nPower Consumption:\
                {self.__power_consumption}\nMemory: {self.__memory}\nBase Price:\
                {self.__base_price}\nVideogames: {self.__videogames}\nProcessor:\
                {self.__processor}\nDifficulties: {self.__difficulties}\nArrows:\
                {self.__arrows}\nControls Price: {self.__controls_price}\n\
                 Total Price: {self.get_total_price()}"


class ClassicalArcade:
    """A classical arcade machine."""

    def __init__(self):
        self.__name = None
        self.__color = None
        self.__material = None
        self.__dimensions = "2m x 1.5m x 1.65m"
        self.__weight = 70
        self.__power_consumption = 160
        self.__memory = "2GB"
        self.__base_price = 900
        self.__videogames = []
        self.__processor = "Axon 3"
        self.__vibration = "brrrr"
        self.__record_alert = "You are the best!"

    def get_total_price(self) -> float:
        """Get the total price of the machine."""
        return self.__base_price

    def set_name(self, name: str):
        """Set the name of the machine."""
        self.__name = name

    def set_color(self, color: str):
        """Set the color of the machine."""
        self.__color = color

    def set_material(self, material: str):
        """Set the material of the machine."""
        self.__material = material

    def set_dimensions(self, dimensions: str):
        """Set the dimensions of the machine."""
        self.__dimensions = dimensions

    def set_weight(self, weight: float):
        """Set the weight of the machine."""
        self.__weight = weight

    def get_weight(self) -> float:
        """Get the weight of the machine."""
        return self.__weight

    def set_power_consumption(self, power_consumption: float):
        """Set the power consumption of the machine."""
        self.__power_consumption = power_consumption

    def get_power_consumption(self) -> float:
        """Get the power consumption of the machine."""
        return self.__power_consumption

    def set_memory(self, memory: str):
        """Set the memory of the machine."""
        self.__memory = memory

    def set_base_price(self, base_price: float):
        """Set the base price of the machine."""
        self.__base_price = base_price

    def get_base_price(self) -> float:
        """Get the base price of the machine."""
        return self.__base_price

    def set_videogames(self, videogame: Videogame):
        """Set the videogames of the machine."""
        self.__videogames.append(videogame)

    def get_videogames(self) -> List[Videogame]:
        """Get the videogames of the machine."""
        return self.__videogames

    def set_processor(self, processor: str):
        """Set the processor of the machine."""
        self.__processor = processor

    def set_vibration(self, vibration: str):
        """Set the vibration of the machine."""
        self.__vibration = vibration

    def set_record_alert(self, record_alert: str):
        """Set the record alert of the machine."""
        self.__record_alert = record_alert

    def __str__(self):
        return f"Name: {self.__name}\nColor: {self.__color}\n\
                Material: {self.__material}\nDimensions: {self.__dimensions}\n\
                Weight: {self.__weight}\nPower Consumption:\
                {self.__power_consumption}\nMemory: {self.__memory}\nBase Price:\
                {self.__base_price}\nVideogames: {self.__videogames}\nProcessor:\
                {self.__processor}\nVibration: {self.__vibration}\nRecord Alert:\
                {self.__record_alert}\nTotal Price: {self.get_total_price()}"


class VirtualReality:
    """A virtual reality machine."""

    def __init__(self):
        self.__name = None
        self.__color = None
        self.__material = None
        self.__dimensions = "2m x 1.5m x 1.65m"
        self.__weight = 100
        self.__power_consumption = 160
        self.__memory = "6GB"
        self.__base_price = 1300
        self.__videogames = []
        self.__processor = "Axon 7"
        self.__glasses_type = "VR"
        self.__glasses_price = 200
        self.__glasses_resolution = "1080p"

    def get_total_price(self) -> float:
        """Get the total price of the machine."""
        return self.__base_price + self.__glasses_price

    def set_name(self, name: str):
        """Set the name of the machine."""
        self.__name = name

    def set_color(self, color: str):
        """Set the color of the machine."""
        self.__color = color

    def set_material(self, material: str):
        """Set the material of the machine."""
        self.__material = material

    def set_dimensions(self, dimensions: str):
        """Set the dimensions of the machine."""
        self.__dimensions = dimensions

    def set_weight(self, weight: float):
        """Set the weight of the machine."""
        self.__weight = weight

    def get_weight(self) -> float:
        """Get the weight of the machine."""
        return self.__weight

    def set_power_consumption(self, power_consumption: float):
        """Set the power consumption of the machine."""
        self.__power_consumption = power_consumption

    def get_power_consumption(self) -> float:
        """Get the power consumption of the machine."""
        return self.__power_consumption

    def set_memory(self, memory: str):
        """Set the memory of the machine."""
        self.__memory = memory

    def set_base_price(self, base_price: float):
        """Set the base price of the machine."""
        self.__base_price = base_price

    def get_base_price(self) -> float:
        """Get the base price of the machine."""
        return self.__base_price

    def set_videogames(self, videogame: Videogame):
        """Set the videogames of the machine."""
        self.__videogames.append(videogame)

    def get_videogames(self) -> List[Videogame]:
        """Get the videogames of the machine."""
        return self.__videogames

    def set_processor(self, processor: str):
        """Set the processor of the machine."""
        self.__processor = processor

    def set_glasses_type(self, glasses_type: str):
        """Set the glasses type of the machine."""
        self.__glasses_type = glasses_type

    def set_glasses_price(self, glasses_price: float):
        """Set the glasses price of the machine."""
        self.__glasses_price = glasses_price

    def set_glasses_resolution(self, glasses_resolution: str):
        """Set the glasses resolution of the machine."""
        self.__glasses_resolution = glasses_resolution

    def __str__(self):
        return f"Name: {self.__name}\nColor: {self.__color}\n\
                Material: {self.__material}\nDimensions: {self.__dimensions}\n\
                Weight: {self.__weight}\nPower Consumption:\
                {self.__power_consumption}\nMemory: {self.__memory}\nBase Price:\
                {self.__base_price}\nVideogames: {self.__videogames}\nProcessor:\
                {self.__processor}\nGlasses Type: {self.__glasses_type}\nGlasses Price:\
                {self.__glasses_price}\nGlasses Resolution: {self.__glasses_resolution}\n\
                Total Price: {self.get_total_price()}"


class ShootingMachine:
    """A shooting machine."""

    def __init__(self):
        self.__name = None
        self.__color = None
        self.__material = None
        self.__dimensions = "2m x 1.5m x 1.65m"
        self.__weight = 100
        self.__power_consumption = 160
        self.__memory = "4GB"
        self.__base_price = 1300
        self.__videogames = []
        self.__processor = "Axon 7"
        self.__gun_joystick = "Pistol"
        self.__gun_price = 120
        self.__vibration = "brrrr"

    def get_total_price(self) -> float:
        """Get the total price of the machine."""
        return self.__base_price + self.__gun_price

    def set_name(self, name: str):
        """Set the name of the machine."""
        self.__name = name

    def set_color(self, color: str):
        """Set the color of the machine."""
        self.__color = color

    def set_material(self, material: str):
        """Set the material of the machine."""
        self.__material = material

    def set_dimensions(self, dimensions: str):
        """Set the dimensions of the machine."""
        self.__dimensions = dimensions

    def set_weight(self, weight: float):
        """Set the weight of the machine."""
        self.__weight = weight

    def get_weight(self) -> float:
        """Get the weight of the machine."""
        return self.__weight

    def set_power_consumption(self, power_consumption: float):
        """Set the power consumption of the machine."""
        self.__power_consumption = power_consumption

    def get_power_consumption(self) -> float:
        """Get the power consumption of the machine."""
        return self.__power_consumption

    def set_memory(self, memory: str):
        """Set the memory of the machine."""
        self.__memory = memory

    def set_base_price(self, base_price: float):
        """Set the base price of the machine."""
        self.__base_price = base_price

    def get_base_price(self) -> float:
        """Get the base price of the machine."""
        return self.__base_price

    def set_videogames(self, videogame: Videogame):
        """Set the videogames of the machine."""
        self.__videogames.append(videogame)

    def get_videogames(self) -> List[Videogame]:
        """Get the videogames of the machine."""
        return self.__videogames

    def set_processor(self, processor: str):
        """Set the processor of the machine."""
        self.__processor = processor

    def set_gun_joystick(self, gun_joystick: str):
        """Set the gun joystick of the machine."""
        self.__gun_joystick = gun_joystick

    def set_gun_price(self, gun_price: float):
        """Set the gun price of the machine."""
        self.__gun_price = gun_price

    def set_vibration(self, vibration: str):
        """Set the vibration of the machine."""
        self.__vibration = vibration

    def __str__(self):
        return f"Name: {self.__name}\nColor: {self.__color}\n\
                Material: {self.__material}\nDimensions: {self.__dimensions}\n\
                Weight: {self.__weight}\nPower Consumption:\
                {self.__power_consumption}\nMemory: {self.__memory}\nBase Price:\
                {self.__base_price}\nVideogames: {self.__videogames}\nProcessor:\
                {self.__processor}\nGun Joystick: {self.__gun_joystick}\nGun Price:\
                {self.__gun_price}\nVibration: {self.__vibration}\nTotal Price:\
                {self.get_total_price()}"


class RacingMachine:
    """A racing machine."""

    def __init__(self):
        self.__name = None
        self.__color = None
        self.__material = None
        self.__dimensions = "2m x 1.5m x 1.65m"
        self.__weight = 75
        self.__power_consumption = 150
        self.__memory = "4GB"
        self.__base_price = 1000
        self.__videogames = []
        self.__processor = "Axon 5"
        self.__sound = "Vroom"
        self.__steering_wheel = "Logitech"
        self.__joystick_price = 150

    def get_total_price(self) -> float:
        """Get the total price of the machine."""
        return self.__base_price + self.__joystick_price

    def set_name(self, name: str):
        """Set the name of the machine."""
        self.__name = name

    def set_color(self, color: str):
        """Set the color of the machine."""
        self.__color = color

    def set_material(self, material: str):
        """Set the material of the machine."""
        self.__material = material

    def set_dimensions(self, dimensions: str):
        """Set the dimensions of the machine."""
        self.__dimensions = dimensions

    def set_weight(self, weight: float):
        """Set the weight of the machine."""
        self.__weight = weight

    def get_weight(self) -> float:
        """Get the weight of the machine."""
        return self.__weight

    def set_power_consumption(self, power_consumption: float):
        """Set the power consumption of the machine."""
        self.__power_consumption = power_consumption

    def get_power_consumption(self) -> float:
        """Get the power consumption of the machine."""
        return self.__power_consumption

    def set_memory(self, memory: str):
        """Set the memory of the machine."""
        self.__memory = memory

    def set_base_price(self, base_price: float):
        """Set the base price of the machine."""
        self.__base_price = base_price

    def get_base_price(self) -> float:
        """Get the base price of the machine."""
        return self.__base_price

    def set_videogames(self, videogame: Videogame):
        """Set the videogames of the machine."""
        self.__videogames.append(videogame)

    def get_videogames(self) -> List[Videogame]:
        """Get the videogames of the machine."""
        return self.__videogames

    def set_processor(self, processor: str):
        """Set the processor of the machine."""
        self.__processor = processor

    def set_sound(self, sound: str):
        """Set the sound of the machine."""
        self.__sound = sound

    def set_steering_wheel(self, steering_wheel: str):
        """Set the steering wheel of the machine."""
        self.__steering_wheel = steering_wheel

    def set_joystick_price(self, joystick_price: float):
        """Set the joystick price of the machine."""
        self.__joystick_price = joystick_price

    def __str__(self):
        return f"Name: {self.__name}\nColor: {self.__color}\n\
                Material: {self.__material}\nDimensions: {self.__dimensions}\n\
                Weight: {self.__weight}\nPower Consumption:\
                {self.__power_consumption}\nMemory: {self.__memory}\nBase Price:\
                {self.__base_price}\nVideogames: {self.__videogames}\nProcessor:\
                {self.__processor}\nSound: {self.__sound}\nSteering Wheel:\
                {self.__steering_wheel}\nJoystick Price: {self.__joystick_price}\n\
                Total Price: {self.get_total_price()}"


# ===================== Builders =====================#
class MachineBuilder(ABC):
    """An abstract builder for machines."""
    @abstractmethod
    def build_name(self):
        pass

    @abstractmethod
    def build_color(self):
        pass

    @abstractmethod
    def build_material(self):
        pass

    @abstractmethod
    def build_dimensions(self):
        pass

    @abstractmethod
    def build_weight(self):
        pass

    @abstractmethod
    def build_power_consumption(self):
        pass

    @abstractmethod
    def build_memory(self):
        pass

    @abstractmethod
    def build_base_price(self):
        pass

    @abstractmethod
    def build_videogames(self):
        pass

    @abstractmethod
    def build_processor(self):
        pass

    @abstractmethod
    def get_product(self):
        pass


# ===================== Concrete Builders =====================#
class DanceRevolutionBuilder(MachineBuilder):
    """A builder for Dance Revolution machines."""

    def __init__(self):
        self.dance_revolution = DanceRevolution()

    def build_name(self):
        self.dance_revolution.set_name("")

    def build_color(self):
        self.dance_revolution.set_color("")

    def build_material(self):
        self.dance_revolution.set_material("")

    def build_dimensions(self):
        self.dance_revolution.set_dimensions("2m x 1.5m x 1.65m")

    def build_weight(self):
        self.dance_revolution.set_weight(75)

    def build_power_consumption(self):
        self.dance_revolution.set_power_consumption(500)

    def build_memory(self):
        self.dance_revolution.set_memory("4GB")

    def build_base_price(self):
        self.dance_revolution.set_base_price(1500)

    def build_videogames(self):
        """Build the videogames of the machine."""
        self.dance_revolution.set_videogames([])

    def build_processor(self):
        """Build the processor of the machine."""
        self.dance_revolution.set_processor("Axon 7")

    def build_difficulties(self):
        """Build the difficulties of the machine."""
        self.dance_revolution.set_difficulties("Easy, Medium, Hard")

    def build_arrows(self):
        """Build the arrows of the machine."""
        self.dance_revolution.set_arrows("Up, Down, Left, Right")

    def build_controls_price(self):
        """Build the controls price of the machine."""
        self.dance_revolution.set_controls_price(200)

    def get_product(self) -> DanceRevolution:
        return self.dance_revolution


class ClassicalArcadeBuilder(MachineBuilder):
    """A builder for classical arcade machines."""

    def __init__(self):
        self.classical_arcade = ClassicalArcade()

    def build_name(self):
        self.classical_arcade.set_name("")

    def build_color(self):
        self.classical_arcade.set_color("")

    def build_material(self):
        self.classical_arcade.set_material("")

    def build_dimensions(self):
        self.classical_arcade.set_dimensions("2m x 1.5m x 1.65m")

    def build_weight(self):
        self.classical_arcade.set_weight(75)

    def build_power_consumption(self):
        self.classical_arcade.set_power_consumption(100)

    def build_memory(self):
        self.classical_arcade.set_memory("2GB")

    def build_base_price(self):
        self.classical_arcade.set_base_price(900)

    def build_videogames(self):
        self.classical_arcade.set_videogames([])

    def build_processor(self):
        self.classical_arcade.set_processor("Axon 3")

    def build_vibration(self):
        """Build the vibration of the machine."""
        self.classical_arcade.set_vibration("brrrr")

    def build_record_alert(self):
        """Build the record alert of the machine."""
        self.classical_arcade.set_record_alert("You are the best!")

    def get_product(self):
        return self.classical_arcade


class VirtualRealityBuilder(MachineBuilder):
    """A builder for virtual reality machines."""

    def __init__(self):
        self.virtual_reality = VirtualReality()

    def build_name(self):
        self.virtual_reality.set_name("")

    def build_color(self):
        self.virtual_reality.set_color("")

    def build_material(self):
        self.virtual_reality.set_material("")

    def build_dimensions(self):
        self.virtual_reality.set_dimensions("2m x 1.5m x 1.65m")

    def build_weight(self):
        self.virtual_reality.set_weight(100)

    def build_power_consumption(self):
        self.virtual_reality.set_power_consumption(160)

    def build_memory(self):
        self.virtual_reality.set_memory("6GB")

    def build_base_price(self):
        self.virtual_reality.set_base_price(1300)

    def build_videogames(self):
        self.virtual_reality.set_videogames([])

    def build_processor(self):
        self.virtual_reality.set_processor("Axon 7")

    def build_glasses_type(self):
        """Build the glasses type of the machine."""
        self.virtual_reality.set_glasses_type("VR")

    def build_glasses_price(self):
        """Build the glasses price of the machine."""
        self.virtual_reality.set_glasses_price(200)

    def build_glasses_resolution(self):
        """Build the glasses resolution of the machine."""
        self.virtual_reality.set_glasses_resolution("1080p")

    def get_product(self):
        return self.virtual_reality


class ShootingMachineBuilder(MachineBuilder):
    """A builder for shooting machines."""

    def __init__(self):
        self.shooting_machine = ShootingMachine()

    def build_name(self):
        self.shooting_machine.set_name("")

    def build_color(self):
        self.shooting_machine.set_color("")

    def build_material(self):
        self.shooting_machine.set_material("")

    def build_dimensions(self):
        self.shooting_machine.set_dimensions("2m x 1.5m x 1.65m")

    def build_weight(self):
        self.shooting_machine.set_weight(100)

    def build_power_consumption(self):
        self.shooting_machine.set_power_consumption(160)

    def build_memory(self):
        self.shooting_machine.set_memory("4GB")

    def build_base_price(self):
        self.shooting_machine.set_base_price(1300)

    def build_videogames(self):
        self.shooting_machine.set_videogames([])

    def build_processor(self):
        self.shooting_machine.set_processor("Axon 7")

    def build_gun_joystick(self):
        """Build the gun joystick of the machine."""
        self.shooting_machine.set_gun_joystick("Pistol")

    def build_gun_price(self):
        """Build the gun price of the machine."""
        self.shooting_machine.set_gun_price(120)

    def build_vibration(self):
        """Build the vibration of the machine."""
        self.shooting_machine.set_vibration("brrrr")

    def get_product(self):
        return self.shooting_machine


class RacingMachineBuilder(MachineBuilder):
    """A builder for racing machines."""

    def __init__(self):
        self.racing_machine = RacingMachine()

    def build_name(self):
        self.racing_machine.set_name("")

    def build_color(self):
        self.racing_machine.set_color("")

    def build_material(self):
        self.racing_machine.set_material("")

    def build_dimensions(self):
        self.racing_machine.set_dimensions("2m x 1.5m x 1.65m")

    def build_weight(self):
        self.racing_machine.set_weight(75)

    def build_power_consumption(self):
        self.racing_machine.set_power_consumption(150)

    def build_memory(self):
        self.racing_machine.set_memory("4GB")

    def build_base_price(self):
        self.racing_machine.set_base_price(1000)

    def build_videogames(self):
        self.racing_machine.set_videogames([])

    def build_processor(self):
        self.racing_machine.set_processor("Axon 5")

    def build_sound(self):
        """Build the sound of the machine."""
        self.racing_machine.set_sound("Vroom")

    def build_steering_wheel(self):
        """Build the steering wheel of the machine."""
        self.racing_machine.set_steering_wheel("Logitech")

    def build_joystick_price(self):
        """Build the joystick price of the machine."""
        self.racing_machine.set_joystick_price(150)

    def get_product(self):
        return self.racing_machine


# ===================== Director =====================#
class Director:
    """A director for building machines."""

    def __init__(self, builder: MachineBuilder):
        self.builder = builder

    def make(self):
        """Make a machine using the builder."""
        self.builder.build_name()
        self.builder.build_color()
        self.builder.build_material()
        self.builder.build_dimensions()
        self.builder.build_weight()
        self.builder.build_power_consumption()
        self.builder.build_memory()
        self.builder.build_base_price()
        self.builder.build_videogames()
        self.builder.build_processor()
        return self.builder.get_product()
