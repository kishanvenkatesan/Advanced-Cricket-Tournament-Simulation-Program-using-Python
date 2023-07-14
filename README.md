# Advanced-Cricket-Tournament-Simulation-Program-using-Python

This project is a cricket tournament simulation program developed in Python. It allows you to simulate a cricket tournament with advanced level details, including player statistics, team management, match simulation, and commentary.

## Installation

1. Clone the project repository:

   ```bash
   git clone https://github.com/kishanvenkatesan/Advanced-Cricket-Tournament-Simulation-Program-using-Python
   ```

2. Navigate to the project directory:

   ```bash
   cd Advanced-Cricket-Tournament-Simulation-Program-using-Python
   ```

## Usage

1. Run the main.py file to start the cricket tournament simulation:

   ```bash
   python main.py
   ```

2. Follow the prompts and inputs to simulate the cricket tournament. The program will display the match commentary and summary, and announce the winner of the tournament.

## Project Structure

The project follows the following file structure:

```
cricket-tournament/
  ├── main.py
  ├── match.py
  ├── team.py
  ├── field.py
  ├── umpire.py
  ├── commentator.py
  ├── player.py
  └──  README.md
```

- `main.py`: The main entry point of the program that starts the cricket tournament simulation.
- `match.py`: Contains the `Match` class responsible for simulating an individual cricket match.
- `team.py`: Defines the `Team` class that represents a cricket team and includes methods for team management.
- `field.py`: Implements the `Field` class that contains factors affecting match probabilities, such as field size, pitch conditions, etc.
- `umpire.py`: Defines the `Umpire` class responsible for predicting outcomes, keeping track of scores, overs, and making decisions during the match.
- `commentator.py`: Implements the `Commentator` class that provides commentary for each ball and over during the match.
- `player.py`: Contains the `Player` class that represents a cricket player with various statistics and skills.
- `README.md`: This file, providing an overview of the project and instructions for usage.
- `requirements.txt`: Lists the required dependencies for the project.

## Contributing

Contributions to the project are welcome! If you have any ideas, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---
