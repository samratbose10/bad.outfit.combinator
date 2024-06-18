import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import numpy as np

# Define some color names and their hex values
colors = {
    "Red": "#FF0000", "Green": "#008000", "Blue": "#0000FF", "Yellow": "#FFFF00",
    "Purple": "#800080", "Orange": "#FFA500", "Pink": "#FFC0CB", "Brown": "#A52A2A",
    "Black": "#000000", "White": "#FFFFFF", "Gray": "#808080", "Cyan": "#00FFFF",
    "Magenta": "#FF00FF", "Lime": "#00FF00", "Maroon": "#800000", "Navy": "#000080",
    "Olive": "#808000", "Teal": "#008080", "Silver": "#C0C0C0", "Gold": "#FFD700",
    "Beige": "#F5F5DC", "Turquoise": "#40E0D0", "Lavender": "#E6E6FA", 
    "Coral": "#FF7F50", "Fuchsia": "#FF00FF"
}

# Function to generate a random color combination
def generate_ridiculous_color_combination():
    top_color_name = random.choice(list(colors.keys()))
    bottom_color_name = random.choice(list(colors.keys()))
    
    # Ensure both colors are different
    while bottom_color_name == top_color_name:
        bottom_color_name = random.choice(list(colors.keys()))

    return {
        "top": (top_color_name, colors[top_color_name]),
        "bottom": (bottom_color_name, colors[bottom_color_name])
    }

# Function to update the animation
def update(frame):
    if frame == 0:
        text.set_text("Thinking...")
    else:
        text.set_text("Thinking" + "." * (frame % 4))
    return text,

# Function to display the final color combination
def display_color_combination():
    combination = generate_ridiculous_color_combination()
    
    fig, ax = plt.subplots()
    ax.set_axis_off()
    fig.patch.set_facecolor('#f0f0f0')
    
    # Display the colors with shadows and borders
    shadow_offset = 0.02
    
    # Top color box
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
    
    # Bottom color box
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
    
    # Equal sign
    ax.text(0.5, 0.55, "=", ha='center', va='center', fontsize=20)
    
    # Load the image to replace the bad combination text
    image_path = 'C:/Users/Lenovo/Desktop/rid.color/download.png'
    img = Image.open(image_path)
    img.thumbnail((100, 100), Image.LANCZOS)
    img_arr = np.array(img)
    imagebox = OffsetImage(img_arr, zoom=1)
    ab = AnnotationBbox(imagebox, (0.5, 0.35), frameon=False)
    ax.add_artist(ab)
    
    plt.show()

# Function to start the process
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

# Run the process
start_process()
