"""
# 🕹️ Arcade Video Game Machine CLI - Workshop 2 Solution

## 📂 Project Structure
This repository contains the solution to **Workshop 2** of the Software Modeling I course.
The project is a command-line interface (CLI) application that simulates the purchase 
and customization of arcade video game machines, with features like adjusting the quality 
and price of the games.

### Folder and File Breakdown

*machines.py*:
This file contains the classes for creating and customizing arcade machines using 
the Builder pattern. It includes machine types like DanceRevolution, ShootingMachine, 
and others. Each machine has attributes like name, color, and power consumption.

*videogames_catalog.py*:
This file manages the videogames catalog. It includes logic to handle different game 
quality settings (high or low) and adjusts their price accordingly, implemented 
through the Factory Pattern. It also ensures the videogame catalog follows the Singleton 
pattern so there is only one instance.

*main.py*:
This is the main execution file that handles the core interactions between customers and 
the arcade shop. Customers can purchase arcade machines, view and modify game quality, 
and finalize their purchase.
"""

📝 Notes

- This application is built using Python and follows object-oriented programming (OOP) principles.
- The design leverages the Builder, Factory, and Singleton patterns to ensure modularity, reusability, and maintainability.
- The Factory Pattern allows for price adjustment of videogames based on quality (high or low graphics).
- The Builder Pattern is used to construct various types of arcade machines step-by-step, allowing customization of each machine.
- The Singleton Pattern ensures that the videogame catalog is globally accessible and has a single instance throughout the application.

Example Usage:
Once the application is running, you can perform the following actions:

1. Purchase a specific arcade machine (e.g., Dance Revolution Machine).
2. Modify the quality of the games installed on the machine (high or low quality).
3. See the price adjustment based on the selected quality.

🧑‍💻 Authors
Julián David Pulido

"""
