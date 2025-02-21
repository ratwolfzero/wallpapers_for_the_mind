import numpy as np
import matplotlib.pyplot as plt

# Constants
WIDTH, HEIGHT = 400, 400  # Grid resolution
CORNER_A = -15  # Lower-left corner
CORNER_B = -25  # Lower-right corner
SIDE = 41  # Side length of the square grid
NUM_COLORS = 4  # Number of distinct colors


def compute_wallpaper(corner_a, corner_b, side, width, height, num_colors):
    """
    Function to compute a pattern based on squared sums with multiple colors.
    """
    colors = np.random.randint(0, 256, (num_colors, 3), dtype=np.uint8)  # Full 8-bit range

    x_scale = side / width
    y_scale = side / height

    x = corner_a + x_scale * np.arange(height)[:, np.newaxis] / width
    y = corner_b + y_scale * np.arange(width)

    z = x**2 + y**2
    color_indices = z % num_colors

    return colors[color_indices]


def plot_wallpaper(image, corner_a, side, corner_b):
    """Plot the generated wallpaper pattern."""
    plt.figure(figsize=(8, 8))
    plt.imshow(image, extent=[corner_a, corner_a +
               side, corner_b, corner_b + side])
    plt.axis('off')
    plt.show()


def main():
    """Main function to execute the wallpaper generation."""
    image = compute_wallpaper(CORNER_A, CORNER_B, SIDE,
                              WIDTH, HEIGHT, NUM_COLORS)
    plot_wallpaper(image, CORNER_A, SIDE, CORNER_B)


if __name__ == "__main__":
    main()
