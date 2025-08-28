
# Truck Loading Optimization with Genetic Algorithm

This project implements a genetic algorithm to optimize the loading of packages into trucks, aiming to maximize total profit while respecting space and weight constraints.

## Description

The user is prompted to input:
- The **total number of packages**, along with the **weight (Kg)**, **dimensions (length and width in meters)**, and **price (€)** of each package.
- The **total number of trucks**, along with each truck's **maximum weight capacity (Kg)** and **cabin dimensions (length and width in meters)**.

Using this input data, the program applies a genetic algorithm to determine the best way to load packages into trucks, in order to:
- Maximize the total value of delivered packages,
- Ensure that no truck exceeds its weight or space capacity.

The algorithm includes:
- Initial population generation (random loading configurations),
- A fitness function that rewards high total price and penalizes constraint violations,
- Selection of the best candidates,
- Crossover and mutation to generate new solutions,
- Iterative improvement over multiple generations.

## Features

- Fully interactive CLI interface for user input
- Dynamic handling of any number of packages and trucks
- Modular and customizable Python implementation
- Output of the most optimal configuration found

## Technologies Used

- Python 3
- Standard Python libraries (`random`, `input` functions)

## How to Run

Make sure you have Python 3 installed, then run:

```bash
python3 main.py
```

## Author  
**Christos Agelis**  
[GitHub Profile](https://github.com/cagelis)
