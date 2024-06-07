# Birthday Paradox Simulation

This project simulates the Birthday Paradox, demonstrating the probability that in a group of a certain number of people, at least two will share the same birthday. The simulation runs multiple times to estimate this probability.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [License](#license)

## Introduction

The Birthday Paradox is a famous problem in probability theory. It states that in a group of just 23 people, there's a better than even chance that at least two people will have the same birthday. This project uses Python to simulate this scenario and calculate the probability.

## Prerequisites

- Python 3.x
- `tqdm` library for displaying a progress bar

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/birthday-paradox-simulation.git
    cd birthday-paradox-simulation
    ```

2. **Install the required dependencies:**
    ```sh
    pip3 install tqdm
    ```

## Usage

1. **Run the simulation:**
    ```sh
    python birthday_paradox.py
    ```

2. **Follow the prompts:**
    - Enter the number of birthdays to generate (maximum 100).
    - The program will simulate 1,000,000 groups of the specified number of people and display the probability of at least two people sharing the same birthday.

## Code Explanation

### `comparison(birthdayList)`

This function takes a list of birthdays and returns the number of duplicate birthdays.

### `simulation(numBirthdays)`

This function runs the simulation 1,000,000 times, generating random birthdays for the specified number of people and counting how of
