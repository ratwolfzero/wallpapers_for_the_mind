# Wallpaper Pattern Generator: Circle² (***Wallpaper for the mind***)

## Circle²

This Python script generates visually stunning wallpaper patterns using the Circle² algorithm, inspired by the work of John E. Connett. The algorithm, originally introduced in A.K. Dewdney's "Computer Recreations" column in Scientific American (September 1986), explores the mathematical properties of integer lattice points and the equation z = x² + y².

## About Circle²

The Circle² algorithm visualizes the distribution of squared sums (z = x² + y²) for integer coordinates (x, y). By assigning colors based on the properties of z, the algorithm creates concentric circular patterns. This script uses the modulo operator to generate repeating color bands, a common technique in procedural pattern generation.

## How It Works

A grid of pixels is defined by WIDTH and HEIGHT.
For each pixel, the coordinates (x, y) are mapped to the equation z = x² + y².
The value of z is used to assign a color, typically via z % NUM_COLORS, creating repeating patterns.
Customization

## Adjust the following parameters to create unique designs:

- WIDTH, HEIGHT: Resolution of the image.
- CORNER_A, CORNER_B: Lower-left corner of the grid.
- SIDE: Side length of the grid.
- NUM_COLORS: Number of colors in the palette.

## Example

Varying the `NUM_COLORS` parameter will dramatically change the look of the pattern. Experiment with different values to see how the design evolves!

## Further Exploration

- Try different mathematical functions to create new patterns.
- Implement custom color palettes.
- Explore other pattern-generation algorithms in computer graphics and recreational mathematics.
