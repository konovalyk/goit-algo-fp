import argparse
import math
import matplotlib.pyplot as plt


COLOR = "#a1493e"


def draw_line(ax, start: complex, end: complex, linewidth=1.6):
    ax.plot([start.real, end.real], [start.imag, end.imag], color=COLOR, linewidth=linewidth)


def draw_branch(ax,
                start: complex,
                length: float,
                angle_rad: float,
                depth: int,
                scale: float,
                branch_angle_rad: float,
                linewidth: float,
                pause: float):
    
    end = start + length * complex(math.cos(angle_rad), math.sin(angle_rad))
    draw_line(ax, start, end, linewidth=linewidth)
    if pause:
        plt.pause(pause)

    if depth <= 0:
        return

    
    child_len = length * scale
    draw_branch(ax, end, child_len, angle_rad + branch_angle_rad, depth - 1, scale, branch_angle_rad, linewidth, pause)
    draw_branch(ax, end, child_len, angle_rad - branch_angle_rad, depth - 1, scale, branch_angle_rad, linewidth, pause)


def main():
    parser = argparse.ArgumentParser(description="Recursive fractal tree (binary splits at ±angle, live lines)")
    parser.add_argument("--depth", "-d", type=int, default=10, help="Recursion depth")
    parser.add_argument("--linewidth", type=float, default=1.8, help="Line width for drawing")
    parser.add_argument("--speed", type=float, default=0.0008, help="Pause duration in seconds for live drawing")
    parser.add_argument("--size", type=float, default=3.0, help="Initial trunk length")
    parser.add_argument("--scale", type=float, default=0.7, help="Scale factor for branch length per level")
    args = parser.parse_args()

    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_aspect("equal")
    ax.axis("off")

    size = args.size
    angle_rad = math.radians(90.0) 
    branch_angle_rad = math.radians(45.0)


    start = complex(0.0, 0.0)
    end = start + size * complex(math.cos(angle_rad), math.sin(angle_rad))
    draw_line(ax, start, end, linewidth=args.linewidth)

    
    
    s = args.scale
    inv = max(1 - s, 1e-6)
    horiz = size * (s / inv)
    vert = size * (1 + s / inv)
    margin = 1.08
    ax.set_xlim(-horiz * margin, horiz * margin)
    ax.set_ylim(-size * 0.3, vert * margin)

    
    draw_branch(ax, end, size * args.scale, angle_rad + 0.0, args.depth - 1,
                args.scale, branch_angle_rad, args.linewidth, args.speed)

   
    plt.ioff()
    plt.show()


if __name__ == "__main__":
    main()
