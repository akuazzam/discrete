# Subset Graph Visualization

This project generates a subset graph for a given list of elements and visualizes it. The graph uses directed edges to represent the relationships between subsets, and the empty set is displayed using the mathematical symbol (∅).

---

## Features

- Generates subsets for a given set of elements.
- Creates a directed graph illustrating subset relationships.
- Uses "∅" to represent the empty set.
- Visualizes the graph with `networkx` and `matplotlib`.

---

## Prerequisites

Before running the script, ensure the following are installed on your system:

1. **Python 3.12 or later**
2. The following Python libraries:
   - `networkx`
   - `matplotlib`

---

## Installation

### Clone or Download the Script

1. Download the script file `subset.py` to your local machine.
2. Save it in a directory you can access from the terminal.

---

### Install Dependencies

Open your terminal and run the following command to install the required Python libraries:

```bash
pip install networkx matplotlib
```

### Running the script
1. Navigate to the path where the script is saved
cd /path/to/your/script

## Usage

### Customize Input

The script uses `[1, 2, 3]` as the default input. To try a different input:

1. Open the `subset.py` file in any text editor.
2. Navigate to **line 55**, where the input list is defined:
   ```python
   elements = [1, 2, 3]  # input elements
   ```
   Note: The graph can get very messy for big inputs.

2. Run the script
python subset.py


