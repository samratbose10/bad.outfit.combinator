import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches
import matplotlib.text as mtext
import time


colors = {
    "Red": "#FF0000", "Green": "#008000", "Blue": "#0000FF", "Yellow": "#FFFF00",
    "Purple": "#800080", "Orange": "#FFA500", "Pink": "#FFC0CB", "Brown": "#A52A2A",
    "Black": "#000000", "White": "#FFFFFF", "Gray": "#808080", "Cyan": "#00FFFF",
    "Magenta": "#FF00FF", "Lime": "#00FF00", "Maroon": "#800000", "Navy": "#000080",
    "Olive": "#808000", "Teal": "#008080", "Silver": "#C0C0C0", "Gold": "#FFD700",
    "Beige": "#F5F5DC", "Turquoise": "#40E0D0", "Lavender": "#E6E6FA", 
    "Coral": "#FF7F50", "Fuchsia": "#FF00FF"
}


def generate_ridiculous_color_combination():
    top_color_name = random.choice(list(colors.keys()))
    bottom_color_name = random.choice(list(colors.keys()))
    

    while bottom_color_name == top_color_name:
        bottom_color_name = random.choice(list(colors.keys()))

    return {
        "top": (top_color_name, colors[top_color_name]),
        "bottom": (bottom_color_name, colors[bottom_color_name])
    }


def update(frame):
    if frame == 0:
        text.set_text("Thinking...")
    else:
        text.set_text("Thinking" + "." * (frame % 4))
    return text,


def display_color_combination():
    combination = generate_ridiculous_color_combination()
    
    fig, ax = plt.subplots()
    ax.set_axis_off()
    fig.patch.set_facecolor('#f0f0f0')
    
 
    shadow_offset = 0.02
    

    top_box = patches.FancyBboxPatch((0.1, 0.6), 0.35, 0.2, boxstyle="round,pad=0.1", 
                                     ec="black", fc=combination["top"][1], 
                                     mutation_aspect=1, lw=2, zorder=2)
    top_box_shadow = patches.FancyBboxPatch((0.1 + shadow_offset, 0.6 - shadow_offset), 0.35, 0.2, 
                                            boxstyle="round,pad=0.1", ec="none", 
                                            fc="gray", mutation_aspect=1, zorder=1)
    ax.add_patch(top_box_shadow)
    ax.add_patch(top_box)
    ax.text(0.275, 0.65, combination["top"][0], ha='center', va='center', fontsize=12, 
            color='white' if combination["top"][0] in ['Black', 'Navy', 'Maroon'] else 'black')
    

    bottom_box = patches.FancyBboxPatch((0.55, 0.6), 0.35, 0.2, boxstyle="round,pad=0.1", 
                                        ec="black", fc=combination["bottom"][1], 
                                        mutation_aspect=1, lw=2, zorder=2)
    bottom_box_shadow = patches.FancyBboxPatch((0.55 + shadow_offset, 0.6 - shadow_offset), 0.35, 0.2, 
                                               boxstyle="round,pad=0.1", ec="none", 
                                               fc="gray", mutation_aspect=1, zorder=1)
    ax.add_patch(bottom_box_shadow)
    ax.add_patch(bottom_box)
    ax.text(0.725, 0.65, combination["bottom"][0], ha='center', va='center', fontsize=12, 
            color='white' if combination["bottom"][0] in ['Black', 'Navy', 'Maroon'] else 'black')
    
    ax.text(0.5, 0.55, "=", ha='center', va='center', fontsize=20)
    
    ax.text(0.5, 0.45, "Bad Combination!", ha='center', va='center', fontsize=15, color='red')
    
    plt.show()


def start_process():
    global text
    fig, ax = plt.subplots()
    ax.set_axis_off()
    fig.patch.set_facecolor('#f0f0f0')
    text = ax.text(0.5, 0.5, "Thinking...", ha='center', va='center', fontsize=20)
    
    ani = FuncAnimation(fig, update, frames=range(12), interval=250, repeat=False, blit=True)
    
    plt.show(block=False)
    plt.pause(3)
    plt.close(fig)
    
    display_color_combination()

start_process()
