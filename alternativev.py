import numpy as np

# Create an initial 1D array with a single "on" cell in the middle
rule_30 = [0, 0, 0, 1, 0, 0, 0]

# Create a 2D array to store the iterations of the rule
rule_30_grid = np.zeros((20, 7), dtype=int)

# Set the initial state as the first row of the grid
rule_30_grid[0, :] = rule_30

# Implement the rule 30 algorithm to compute the subsequent rows
for i in range(1, 20):
    for j in range(1, 6):
        left = rule_30_grid[i-1, j-1]
        center = rule_30_grid[i-1, j]
        right = rule_30_grid[i-1, j+1]

        # Rule 30: if the cell on the left, center, and right
        # are all either 0 or 1, the new cell is 0
        rule_30_grid[i, j] = 0 if (left + center + right) in [0, 3] else 1

# Print the final 2D grid
print(rule_30_grid)

#displaying thhe image
plt.imshow(matrix, cmap="binary")

# Turn off the axis labels
plt.axis("off")

# Show the plot
plt.show()