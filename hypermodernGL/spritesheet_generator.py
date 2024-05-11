
import pygame as pg
import json
import os


def generate_spritesheets(path='assets/', valid_formats=['png', 'jpg', 'tiff']):

    tilable_sheets, entity_sheets = get_spritesheets()

    # Load tileable sheets
    for tilable_sheet in tilable_sheets.items():
        generate_from_tiles(tilable_sheet, path, valid_formats)

    # Load entity sheets
    for entity_sheet in entity_sheets.items():
        generate_from_entity(entity_sheet, path, valid_formats)


def get_spritesheets():

    # Loading could be laoded in from a json
    loading_etities = {
        'faces_sheet': {
            'faces': {'marker_colour': '#012E6F', 'colour_key': '#000000', 'filter': 'NEAREST', 'swizzle': 'BRGA', 'shader': 'default'},
        },
    }

    loading_tilable = {
        'coloured_tiles_sheet': {
            # In the format of tile.x, tile.y, num of tiles to be added to list
            'coloured_tiles': {'tile_format': '16;16;4', 'colour_key': '#000000', 'filter': 'NEAREST', 'swizzle': 'BRGA', 'shader': 'default'},
        },
    }

    return loading_tilable, loading_etities


def generate_from_tiles(data, path, valid_formats):
    
    name_of_file = data[0]
    data_of_file = data[1]
    
    surfaces = {}
    # Find the extention of the image file
    files = os.listdir(path)
    extention = None
    already_exists = False

    for file in files:
        file = file.split('.')
        if file[0] == name_of_file and (file[1] in valid_formats):
            extention = '.'+file[1]
        if file[0] == name_of_file and file[1] == 'json':
            already_exists = True

    if not extention:
        raise TypeError('There was no valid extention for the file to be loaded')

    sprite_sheet = pg.image.load(path+name_of_file+extention)
    size = pg.math.Vector2(sprite_sheet.get_size())

    for tile_set in data_of_file:

        surfaces[tile_set] = {'frames': []}
        tile_width, tile_height, tile_count = data_of_file[tile_set]['tile_format'].split(';')

        surfaces[tile_set]['colour_key'] = data_of_file[tile_set]['colour_key']
        surfaces[tile_set]['filter'] = data_of_file[tile_set]['filter']
        surfaces[tile_set]['swizzle'] = data_of_file[tile_set]['swizzle']
        surfaces[tile_set]['shader'] = data_of_file[tile_set]['shader']

        tile_size = pg.math.Vector2(int(tile_width), int(tile_height))
        current_pixel = pg.math.Vector2(0, 0)

        for _ in range(int(tile_count)):
            
            surfaces[tile_set]['frames'].append([*current_pixel, *tile_size])
            current_pixel.x += tile_size.x

            if current_pixel.x+1 > size.x:
                current_pixel.x = 0
                current_pixel.y += tile_size.y

                if current_pixel.y >= size.y:
                    break
            
            else:
                current_pixel.x += tile_size.x

    if already_exists:
        if not input('Do you want to override the last json file? y/n: ') == 'y':
            return

    with open(path+name_of_file+'.json','w') as sprite_sheet_json:
        
        json.dump(surfaces, sprite_sheet_json)


def generate_from_entity(data, path, valid_formats):

    name_of_file = data[0]
    data_of_file = data[1]
    
    surfaces = {}
    # Find the extention of the image file
    files = os.listdir(path)
    extention = None
    already_exists = False

    for file in files:
        file = file.split('.')
        if file[0] == name_of_file and (file[1] in valid_formats):
            extention = '.'+file[1]
        if file[0] == name_of_file and file[1] == 'json':
            already_exists = True

    if not extention:
        raise TypeError('There was no valid extention for the file to be loaded', name_of_file)

    sprite_sheet = pg.image.load(path+name_of_file+extention)
    size = pg.math.Vector2(sprite_sheet.get_size())

    for sprite_set in data_of_file:

        surfaces[sprite_set] = {'frames': []}
        marker_colour = hex_to_rgb(data_of_file[sprite_set]['marker_colour'])

        surfaces[sprite_set]['colour_key'] = data_of_file[sprite_set]['colour_key']
        surfaces[sprite_set]['swizzle'] = data_of_file[sprite_set]['swizzle']
        surfaces[sprite_set]['filter'] = data_of_file[sprite_set]['filter']
        surfaces[sprite_set]['shader'] = data_of_file[sprite_set]['shader']

        current_pixel = pg.math.Vector2(0, 0)
        seen_pixels = set()

        while current_pixel.y < size.y:

            # Go until the pointer hits the top right of the sprite
            if sprite_sheet.get_at(current_pixel) == marker_colour and tuple(current_pixel) not in seen_pixels:
                seen_pixels.add(tuple(current_pixel))

                # Save the topleft of the sprite
                old_pixel = current_pixel.copy()
                sprite_size = pg.math.Vector2(0, 0)

                # Find the top right
                current_pixel.x += 1
                while not sprite_sheet.get_at(current_pixel) == marker_colour:
                    current_pixel.x += 1
                seen_pixels.add(tuple(current_pixel))

                # Calculate the width of the sprite
                sprite_size.x = current_pixel.x - old_pixel.x - 1

                # Find the bottom right
                current_pixel.y += 1
                while not sprite_sheet.get_at(current_pixel) == marker_colour:
                    current_pixel.y += 1
                seen_pixels.add(tuple(current_pixel))

                # Calculate the height of the sprite
                sprite_size.y = current_pixel.y - old_pixel.y - 1
                surfaces[sprite_set]['size'] = str(sprite_size.x)+';'+str(sprite_size.y)


                seen_pixels.add((old_pixel.x, current_pixel.y))

                # Move the pointer back to where it started
                current_pixel.y = old_pixel.y
                current_pixel.x += 1

                # Save the data
                surfaces[sprite_set]['frames'].append([old_pixel.x + 1, old_pixel.y + 1, *sprite_size])

            else:
                current_pixel.x += 1

                if current_pixel.x >= size.x:
                    # Move pointer to next line
                    current_pixel.x = 0
                    current_pixel.y += 1

    # Check if the json file is going to be overriden
    if already_exists:
        if not input('Do you want to override the last json file? y/n: ') == 'y':
            return
        
    with open(path+name_of_file+'.json','w') as sprite_sheet_json:

        json.dump(surfaces, sprite_sheet_json)
            
def hex_to_rgb(hex_value):

    # Decide the starting index for each pair
    if hex_value[0] == '#':
        indices = (1, 3, 5)
    else:
        indices = (0, 2, 4)

    # Calculate the decimal value
    rgb = [int(hex_value[i:i+2], 16) for i in indices]
    return tuple(rgb)

#generate_spritesheets()
