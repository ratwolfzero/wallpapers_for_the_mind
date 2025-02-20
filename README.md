# Wallpaper Pattern Generator

This Python script generates visually interesting wallpaper patterns based on a mathematical algorithm inspired by the "Circles" pattern. This pattern explores integer lattice points and is closely associated with the works of **A.K. Dewdney**, who popularized computational patterns through his *Scientific American* "Computer Recreations" column, and **E. Connett** from the University of Minnesota

## Historical Context

The "Circles" pattern is based on the equation `x^2 + y^2`, which defines a circle in the coordinate plane. By considering integer values of `x` and `y` and applying the modulo operator, circular patterns emerge. This method leads to concentric ring-like visuals, a concept explored by Dewdney.

## Algorithm

For each pixel in the grid, the script calculates `z = x^2 + y^2` and assigns a color based on the value of `z` using the modulo operator. This generates repeating patterns based on the distribution of squared sums, producing the distinctive "Circles" effect.

## Customization

You can adjust the following parameters:

- `WIDTH`, `HEIGHT`: Resolution of the generated image.
- `CORNER_A`, `CORNER_B`: Coordinates of the lower-left corner of the grid.
- `SIDE`: Side length of the square grid.
- `NUM_COLORS`: Number of distinct colors used in the pattern.

## Example

Varying the `NUM_COLORS` parameter will dramatically change the look of the pattern. Experiment with different values to see how the design evolves!

## Further Exploration

- Try different mathematical functions to create new patterns.
- Implement custom color palettes.
- Explore other pattern-generation algorithms in computer graphics and recreational mathematics.
