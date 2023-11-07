# Interior Point Algorithm Project

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)

## Introduction

This project is an implementation of the Interior Point algorithm, which is used for solving linear and quadratic programming problems. The algorithm is designed to find the optimal solution to such problems.

## Features

- Solve linear programming problems.
- Provide detailed information of the value of the decision variables in each iteration.
- Customizable parameters to fine-tune the algorithm, such as the accuracy and the initial point of the specific problem.

## Installation

To run this project, follow these steps:

1. Clone the repository to your local machine.
   ```bash
   https://github.com/Isistickz/interior_point
   ```
Install the required dependencies.
bash
Copy code
pip install -r requirements.txt
Usage
To use the Interior Point algorithm, import the relevant modules in your Python script.

Initialize the algorithm with your problem parameters and constraints.

Run the algorithm, and it will find the optimal solution to your problem.

python
Copy code
from interior_point import InteriorPointSolver

# Initialize the solver
solver = InteriorPointSolver(problem_parameters, constraints)

# Run the solver
result = solver.solve()
For more detailed information, refer to the project's documentation.

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
