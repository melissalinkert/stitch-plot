import matplotlib
import matplotlib.pyplot as plt

class patterns:

    def threads(start, thread_count):
        coords = []
        for thread in range(0, thread_count + 1):
            coords.append(start + thread)
        return coords

    def draw_kloster(ax, x, y, rot):
        if rot == 0:
            ax.vlines(patterns.threads(x, 4), y, y + 4)
        elif rot == 90:
            ax.hlines(patterns.threads(y, 4), x, x + 4)

    def draw_diamond(ax, x, y, height):
        rotation = 0
        midpoint = (height + 1) / 2
        for y_block in range(0, height):
            real_y = y_block * 4
            if y_block == 0 or y_block == height - 1:
                patterns.draw_kloster(ax=ax, x=x, y=real_y + y, rot=rotation)
            elif y_block < midpoint:
                patterns.draw_kloster(ax=ax, x=real_y + x, y=real_y + y, rot=rotation)
                patterns.draw_kloster(ax=ax, x=-real_y + x, y=real_y + y, rot=rotation)
            else:
                real_x = 4 * ((midpoint - 1) - (y_block % (midpoint - 1)))
                patterns.draw_kloster(ax=ax, x=real_x + x, y=real_y + y, rot=rotation)
                patterns.draw_kloster(ax=ax, x=-real_x + x, y=real_y + y, rot=rotation)

            rotation = (rotation + 90) % 180

    threads = staticmethod(threads)
    draw_kloster = staticmethod(draw_kloster)
    draw_diamond = staticmethod(draw_diamond)
