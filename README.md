# The Doomed Dice Challenge

## Introduction
The Doomed Dice Challenge is a mathematical and probability-based problem where two six-sided dice (Die A and Die B) are rolled together, and their sum determines game outcomes. The challenge has two parts:

1. **Part A:** Compute total combinations, display sum distribution in a 6×6 matrix, and calculate probabilities of sums.
2. **Part B:** Modify the dice under constraints while maintaining the original sum probabilities.

## Features
- Computes all possible dice roll sums and their probabilities.
- Transforms dice values while preserving probability distribution.
- Ensures constraints: Die A cannot have more than 4 spots per face, and Die B can exceed 6 spots.

## Project Structure
```
TheDoomedDiceChallenge/
├── main.py               # Main execution script
├── README.md             # Project documentation
```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/TheDoomedDiceChallenge.git
   cd TheDoomedDiceChallenge
   ```
2. Ensure you have Python installed (Python 3.8+ recommended).
3. Install dependencies (if any) using:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the program using:
```sh
python main.py
```
The program will output:
- **Part A:** Dice roll combinations, sum distribution, and probabilities.
- **Part B:** Modified dice values that maintain original sum probabilities.

## Example Output
```
Welcome to The Doomed Dice Challenge!
---------------------------------------
Part A - Calculations:
1. Total number of combinations: 36

2. 6x6 Matrix of Dice Sums:
[2, 3, 4, 5, 6, 7]
...

3. Distribution of sums and their probabilities:
Sum = 2: Probability = 0.0278
...

Part B - Transforming the Dice (Undoom Dice):
New Die A: [1, 2, 2, 3, 3, 4]
New Die B: [1, 3, 4, 5, 6, 8]
```

## Constraints
- **Die A:** Maximum of 4 spots per face.
- **Die B:** Can have values greater than 6.
- **Probability of sums must remain unchanged.**

## License
This project is licensed under the MIT License.

## Author
Developed by **Mohib Rasool**.

---
Happy Coding! 🎲

