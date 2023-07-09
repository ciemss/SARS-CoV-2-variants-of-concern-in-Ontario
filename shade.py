import matplotlib.pyplot as plt
import numpy as np

def shade(*args, **kwargs):
    """
    SHADE Filled area linear plot.
    
    SHADE should be called using the same syntax as the built-in PLOT.
    
    SHADE(X,Y) plots vector Y versus vector X, filling the area under the
    curve. If either is a matrix, this function behaves like PLOT.
    
    SHADE(Y) plots the columns of Y versus their index.
    
    SHADE(X,Y,S) plots Y versus X using the line type, marker symbols and
    colors as specified by S. For more information on the line specifier S,
    see PLOT.
    
    SHADE(X1,Y1,X2,Y2,X3,Y3,...) combines the plots defined by
    the (X,Y) pairs.
    
    SHADE(X1,Y1,S1,X2,Y2,S2,X3,Y3,S3,...) combines the plots defined by
    the (X,Y,S) triples.
    
    SHADE(AX,...) plots into the axes with handle AX.
    
    H = SHADE(...) returns a column vector of handles to graphics objects.
    
    SHADE(...,Name,Value) specifies additional properties of the lines (see
    help for PLOT) or the filled areas (see below).
    """
    # Extract filling parameters, if present
    fill_type = kwargs.pop('FillType', None)
    fill_color = kwargs.pop('FillColor', None)
    fill_alpha = kwargs.pop('FillAlpha', 0.3)

    # Check if an axes object was specified
    if len(args) > 0 and isinstance(args[0], plt.Axes):
        ax = args[0]
        args = args[1:]
    else:
        ax = plt.gca()

    # Plot lines
    lines = ax.plot(*args, **kwargs)

    # Provide default filling params
    if fill_type is None:
        fill_type = [(1, 0)]

    # Validate fill color
    if fill_color is None:
        fill_color = [line.get_color() for line in lines]

    # Validate fill alpha
    if isinstance(fill_alpha, (int, float)):
        fill_alpha = [fill_alpha] * len(lines)

    # For each filling
    for (i, line), color, alpha in zip(enumerate(lines), fill_color, fill_alpha):
        x, y = line.get_data()
        ax.fill_between(x, y, color=color, alpha=alpha)

    return lines

# Example usage
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots()
shade(ax, x, y1, x, y2, FillColor=['red', 'blue'], FillAlpha=[0.3, 0.3])
plt.show()
