import poke_api
from tkinter import *
from tkinter import ttk
import os
import ctypes

# Get the path of the script and its parent directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
image_cache_dir = os.path.join(script_dir, 'images')

# Make the image cache folder if it does not exist
if not os.path.isdir(image_cache_dir):
    os.makedirs(image_cache_dir)

# Create the main window
root = Tk()
root.title("Pokémon Image Viewer")
root.minsize(525, 490)
root.resizable(False, False)

# Set the window icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('COMP593.PokeImageViewer')
icon_path = os.path.join(script_dir, "Poke-Ball.ico")
root.iconbitmap(icon_path)

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

img_poke = PhotoImage(file=os.path.join(script_dir, 'pokemon-logo.png'))
lbl_poke_image = ttk.Label(frame, image=img_poke)
lbl_poke_image.grid(row=0, column=0)

pokemon_name_list = poke_api.get_pokemon_names()
cbox_pokemon_names = ttk.Combobox(frame, values=pokemon_name_list, state='readonly')
cbox_pokemon_names.set("Select a Pokemon")
cbox_pokemon_names.grid(row=1, column=0, padx=10, pady=10)

def handle_poke_sel(event):

    pokemon_name = cbox_pokemon_names.get()
    
    image_path = poke_api.download_pokemon_artwork(pokemon_name, image_cache_dir)

    if image_path is not None:
        img_poke['file'] = image_path

cbox_pokemon_names.bind('<<ComboboxSelected>>', handle_poke_sel)

btn_set_desktop = ttk.Button(frame, text='Set as Desktop Image')
btn_set_desktop.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()