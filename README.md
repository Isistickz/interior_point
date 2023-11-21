# Interior Point Algorithm Project

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)

## Introduction

This project is an implementation of the Interior Point algorithm, which is used for solving linear  programming problems. The algorithm is designed to find the optimal solution to such problems.

## Features

- Solve linear programming problems.
- Provide detailed information on the value of the decision variables in each iteration that the program runs.
- Customizable parameters to fine-tune the algorithm, such as the accuracy and the initial point of the specific problem.

## Installation

To run this project, follow these steps:

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/khushpatel2002/optimization
   ```
2. Install the dependency
```bash
pip install numpy
```
3. cd into the folder and run the main.py
```bash
cd interior_point
python main.py
```
4. Follow the prompts of the program to enter the inputs. We make two fundamental assumptions about the LPPs you want to solve:
   - That they are in standard form already, i.e. all slack variables have been added already, where necessary
   - That they are maximization problems.

## Contributors
This project was a collaborative effort by the following team members:

- Israel Adewuyi
- Yehia Sobeh
- Egor Machnev
- Khush Patel
- Hadi Salloum
- Mike Tezin


## License
This project is licensed under the MIT License.
