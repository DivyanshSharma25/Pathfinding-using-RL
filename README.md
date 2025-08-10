
<div id="top"></div>

<div align="center">
  <h3 align="center"> Pathfinding using Reinforcement Learning</h3>

  <p align="center">
  <!-- UPDATE -->
    <i> Pathfinding in 5x5 grid using Reinforcement Learning </i>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
<summary>Table of Contents</summary>

- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)
  - [Maintainer(s)](#maintainers)
  - [creators(s)](#creators)
- [Additional documentation](#additional-documentation)

</details>


<!-- ABOUT THE PROJECT -->
## About The Project
<!-- UPDATE -->

This project demonstrates pathfinding in a grid environment using both the classic A\* algorithm and a Reinforcement Learning (RL) agent trained with PPO (Proximal Policy Optimization). It includes a Pygame-based GUI for interactive visualization and supports both manual and RL-based pathfinding.
### Features

- **A\* Algorithm**: Classic shortest-path search on a grid with obstacles.
- **Reinforcement Learning**: Train and test an RL agent to find paths using PPO.
- **Interactive GUI**: Visualize and edit the grid, place obstacles, start/end points, and watch the agent/pathfinding in action.
- **Customizable Grid**: Change grid size and obstacle placement.
### Project Structure

- [`a_star.py`](a_star.py): Implementation of the A\* pathfinding algorithm.
- [`Pathfinding_GUI.py`](Pathfinding_GUI.py): Pygame GUI for interactive pathfinding visualization.
- [`reinforcement_learning/environment.py`](reinforcement_learning/environment.py): Custom Gym environment for RL pathfinding.
- [`reinforcement_learning/RL_pathfinding.py`](reinforcement_learning/RL_pathfinding.py): Script to train the RL agent.
- [`reinforcement_learning/RL_testt.py`](reinforcement_learning/RL_testt.py): Script to test the trained RL agent.
- `model/`: Contains trained RL models.
- `requirement.txt`: Python dependencies.
<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started

To set up a local instance of the application, follow the steps below.

### Prerequisites
The following dependencies are required to be installed for the project to function properly:
<!-- UPDATE -->
* Python >= 3.8

<p align="right">(<a href="#top">back to top</a>)</p>

### Installation

_Now that the environment has been set up and configured to properly compile and run the project, the next step is to install and configure the project locally on your system._
<!-- UPDATE -->
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


<!-- USAGE EXAMPLES -->
## Usage
<!-- UPDATE -->
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

<p align="right">(<a href="#top">back to top</a>)</p>

## Contact

### Maintainer(s)

The currently active maintainer(s) of this project.

<!-- UPDATE -->
- [Divyansh Sharma](https://github.com/DivyanshSharma25)

### Creator(s)

Honoring the original creator(s) and ideator(s) of this project.

<!-- UPDATE -->
- [Divyansh Sharma](https://github.com/DivyanshSharma25)

<p align="right">(<a href="#top">back to top</a>)</p>

## Additional documentation

  - [License](/LICENSE)
  - [Contribution Guidelines](/.github/CONTRIBUTING.md)

<p align="right">(<a href="#top">back to top</a>)</p>


