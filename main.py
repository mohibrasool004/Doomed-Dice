
def part_a():
    # Define original dice (Die A and Die B)
    die_A = [1, 2, 3, 4, 5, 6]
    die_B = [1, 2, 3, 4, 5, 6]

    # 1. Calculate total combinations:
    total_combinations = len(die_A) * len(die_B)
    print("Part A - Calculations:")
    print("1. Total number of combinations:")
    print("   Total combinations = 6 x 6 = {}".format(total_combinations))
    print()

    # 2. Generate a 6x6 matrix for all possible sums:
    print("2. 6x6 Matrix of Dice Sums:")
    matrix = []
    for a in die_A:
        row = []
        for b in die_B:
            row.append(a + b)
        matrix.append(row)
    
    # Display the matrix row by row
    for row in matrix:
        print(row)
    print()

    # 3. Calculate distribution of sums and their probabilities:
    sum_distribution = {}
    for a in die_A:
        for b in die_B:
            s = a + b
            sum_distribution[s] = sum_distribution.get(s, 0) + 1

    print("3. Distribution of sums and their probabilities:")
    for s in sorted(sum_distribution.keys()):
        frequency = sum_distribution[s]
        probability = frequency / total_combinations
        print("   Sum = {:2d}: Frequency = {:2d}, Probability = {:.4f}".format(s, frequency, probability))
    print()


def undoom_dice(die_A, die_B):

    # Return the Sicherman dice:
    new_die_A = [1, 2, 2, 3, 3, 4]  # Maximum value is 4, satisfying the condition for Die A.
    new_die_B = [1, 3, 4, 5, 6, 8]  # Die B can have faces with numbers greater than 6.
    return new_die_A, new_die_B

def part_b():
    # Original dice (for reference)
    die_A = [1, 2, 3, 4, 5, 6]
    die_B = [1, 2, 3, 4, 5, 6]

    print("Part B - Transforming the Dice (Undoom Dice):")
    new_die_A, new_die_B = undoom_dice(die_A, die_B)
    print("   New Die A (each face must have ≤ 4 spots):", new_die_A)
    print("   New Die B (faces may exceed 6 spots):", new_die_B)
    print()

    # Verify that the new dice yield the same sum distribution:
    total_combinations = len(new_die_A) * len(new_die_B)
    sum_distribution = {}
    for a in new_die_A:
        for b in new_die_B:
            s = a + b
            sum_distribution[s] = sum_distribution.get(s, 0) + 1

    print("   Distribution of sums with new dice:")
    for s in sorted(sum_distribution.keys()):
        frequency = sum_distribution[s]
        probability = frequency / total_combinations
        print("      Sum = {:2d}: Frequency = {:2d}, Probability = {:.4f}".format(s, frequency, probability))
    print()

def main():
    print("Welcome to The Doomed Dice Challenge!")
    print("---------------------------------------")
    
    # Execute Part A
    part_a()
    
    # Execute Part B
    part_b()

if __name__ == "__main__":
    main()
