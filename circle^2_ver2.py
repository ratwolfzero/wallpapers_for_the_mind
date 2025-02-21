import numpy as np
import matplotlib.pyplot as plt
import random

# Constants
WIDTH, HEIGHT = 400, 400  # Grid resolution
CORNER_A = -15  # Lower-left corner
CORNER_B = -25  # Lower-right corner
SIDE = 41  # Side length of the square grid
NUM_COLORS = 4  # Number of distinct colors

def compute_wallpaper(corner_a, corner_b, side, width, height, num_colors):
    """Compute a pattern based on squared sums with multiple colors."""
    # Generate random colors
    colors = np.random.randint(1, 256, (num_colors, 3), dtype=np.uint8)
    
    # Create a meshgrid for x and y coordinates
    x = corner_a + (side * np.arange(height)[:, np.newaxis] / width)
    y = corner_b + (side * np.arange(width) / height)
    
    # Compute squared sums
    z = x**2 + y**2
    
    # Determine color indices based on the squared sums
    color_indices = (z.astype(int) % num_colors).flatten()
    
    # Create the image using the color indices
    image = colors[color_indices].reshape(height, width, 3)

    return image

def plot_wallpaper(image, corner_a, side, corner_b):
    """Plot the generated wallpaper pattern."""
    plt.figure(figsize=(8, 8))
    plt.imshow(image, extent=[corner_a, corner_a + side, corner_b, corner_b + side])
    plt.axis('off')
    plt.show()

def main():
    """Main function to execute the wallpaper generation."""
    image = compute_wallpaper(CORNER_A, CORNER_B, SIDE, WIDTH, HEIGHT, NUM_COLORS)
    plot_wallpaper(image, CORNER_A, SIDE, CORNER_B)

if __name__ == "__main__":
    main()

