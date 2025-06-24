# Pathfinding using Reinforcement Learning

This project demonstrates pathfinding in a grid environment using both the classic A\* algorithm and a Reinforcement Learning (RL) agent trained with PPO (Proximal Policy Optimization). It includes a Pygame-based GUI for interactive visualization and supports both manual and RL-based pathfinding.

## Features

- **A\* Algorithm**: Classic shortest-path search on a grid with obstacles.
- **Reinforcement Learning**: Train and test an RL agent to find paths using PPO.
- **Interactive GUI**: Visualize and edit the grid, place obstacles, start/end points, and watch the agent/pathfinding in action.
- **Customizable Grid**: Change grid size and obstacle placement.

## Project Structure

- [`a_star.py`](a_star.py): Implementation of the A\* pathfinding algorithm.
- [`Pathfinding_GUI.py`](Pathfinding_GUI.py): Pygame GUI for interactive pathfinding visualization.
- [`reinforcement_learning/environment.py`](reinforcement_learning/environment.py): Custom Gym environment for RL pathfinding.
- [`reinforcement_learning/RL_pathfinding.py`](reinforcement_learning/RL_pathfinding.py): Script to train the RL agent.
- [`reinforcement_learning/RL_testt.py`](reinforcement_learning/RL_testt.py): Script to test the trained RL agent.
- `model/`: Contains trained RL models.
- `requirement.txt`: Python dependencies.

## Installation

1. **Clone the repository**:

   ```sh
   git clone <repo-url>
   cd Pathfinding-using-RL
   ```

2. **Install dependencies**:

   ```sh
   pip install -r requirement.txt
   ```

   Make sure you have Python 3.8+ and [Pygame](https://www.pygame.org/), [Stable Baselines3](https://stable-baselines3.readthedocs.io/), [Gymnasium](https://gymnasium.farama.org/).

## Usage

### 1. Run the GUI

```sh
python Pathfinding_GUI.py
```

- Select either **A_STAR** or **RL** mode.
- Use the instructions to place obstacles, start, and end points.
- Press Enter to start pathfinding.

### 2. Train the RL Agent

```sh
python reinforcement_learning/RL_pathfinding.py
```

- This will train a PPO agent and save the model.

### 3. Test the RL Agent

```sh
python reinforcement_learning/RL_testt.py
```

- Loads the trained model and runs it in the environment.

## Requirements

- Python 3.8+
- Pygame
- numpy
- stable-baselines3
- gymnasium
- sb3-contrib

Install all dependencies with:

```sh
pip install -r requirement.txt
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgements

- [Stable Baselines3](https://github.com/DLR-RM/stable-baselines3)
- [Gymnasium](https://github.com/Farama-Foundation/Gymnasium)
