import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys
from patterns import patterns

def draw_pattern(ax):
    # draw an 8-block diamond
    patterns.draw_diamond(ax, 0, 0, 15)

def make_even(coords):
    new_coords = []
    for coord in coords:
        if coord % 2 == 1:
            if coord < 0:
                new_coords.append(coord - 1)
            else:
                new_coords.append(coord + 1)
    return new_coords

def draw(save_file):
    fig, ax = plt.subplots()

    draw_pattern(ax)

    xlimits = make_even(ax.get_xlim())
    ylimits = make_even(ax.get_ylim())
    ax.set_xticks(np.arange(xlimits[0], xlimits[1], 2.0))
    ax.set_yticks(np.arange(ylimits[0], ylimits[1], 2.0))
    ax.tick_params(axis="both", labelsize=0)
    ax.grid(True)

    if save_file is not None:
        fig.savefig(save_file);
    plt.show()

if __name__ == "__main__":
    save_file = None
    if len(sys.argv) > 1:
        save_file = sys.argv[1]
    draw(save_file)
