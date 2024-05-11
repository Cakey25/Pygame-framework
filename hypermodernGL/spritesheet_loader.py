
import pygame as pg
import moderngl as mgl
import json
import os
import array
#import numba
import config

WINDOWSIZE = config.WINDOWSIZE

#def write_quad_buffer(rect, corners, sprites):
#
#        topleft = self.calc_uvs((rect[0], rect[1]))
#        bottomright = self.calc_uvs((rect[0]+rect[2], rect[1]+rect[3]))
#
#        self.shaders[sprites][1].write(data=array.array('f', [
#        
#            topleft[0],     topleft[1],     corners[0], corners[1],
#            bottomright[0], topleft[1],     corners[2], corners[3],
#            topleft[0],     bottomright[1], corners[4], corners[5],
#            bottomright[0], bottomright[1], corners[6], corners[7],
#        ]))

#@numba.njit
def calc_uvs(point):
    return (2*(point[0] / WINDOWSIZE[0]) - 1, 2*(1 - (point[1] / WINDOWSIZE[1])) - 1)



def load_spritesheets(ctx, app, path='assets/'):

    files = os.listdir(path)    
    textures = dict()
    shaders = dict()

    for file in files:
        
        file_split = file.split('.')
        if len(file) == 1:
            textures_recursion, shaders_recursion = load_spritesheets(
                ctx=ctx,
                app=app,
                path=path+file_split[0]+'/'
            )
            textures.update(textures_recursion)
            shaders.update(shaders_recursion)

        elif file_split[1] == 'json':
            textures_cutout, shaders_cutout = save_textures_shaders(
                ctx=ctx,
                path=path,
                app=app,
                file=file
            )
            textures.update(textures_cutout)
            shaders.update(shaders_cutout)

            # return  dict(str(): dict(str(): list(texture_objects), str(): str())) # Things after the first key are metadata
            # return  textures{'name for frames': dict{'frames': [frames], 'colourkey': '#000000'}}

    return textures, shaders


def save_textures_shaders(ctx, path, file, app, shader_path = 'shaders/'):

    with open(path+file, 'r') as json_file:
        spritesheet_data = json.load(json_file)

    spritesheet = pg.image.load(path+file.split('.')[0]+'.png').convert_alpha()
    textures_cutout = dict()
    loaded_shaders = dict()


    for sprite_set in spritesheet_data:

        frames = []
        textures_cutout[sprite_set] = dict()
        size = (0, 0)

        for data in spritesheet_data[sprite_set]['frames']:

            # Create the pygame surface
            surf = pg.surface.Surface((data[2], data[3]), pg.SRCALPHA)
            surf.blit(spritesheet, (0, 0), data)
            # Create the opengl texture
            size = surf.get_size()
            tex = ctx.texture(size, 4, surf.get_view('1'))

            if spritesheet_data[sprite_set]['filter'] == 'NEAREST':
                tex.filter = (mgl.NEAREST, mgl.NEAREST)
            else:
                raise TypeError(f'No valid sampler set for {sprite_set}')
            
            tex.swizzle = spritesheet_data[sprite_set]['swizzle']
            
            frames.append(tex)

        if sprite_set not in loaded_shaders:

            #with open(shader_path+spritesheet_data[sprite_set]['shader']+'/vert_shader.vert', 'r') as vert_shader:
            #    vertex_shader = vert_shader.read()
            #    
            #with open(shader_path+spritesheet_data[sprite_set]['shader']+'/frag_shader.frag', 'r') as frag_shader:
            #    fragment_shader = frag_shader.read()
            
            #shader = ctx.program(vertex_shader = vertex_shader, fragment_shader = fragment_shader)
            quad_buffer = ctx.buffer(data=array.array('f', [0.0] * 16))
            
            # Maybe make it so that more quad buffers are generated at the start but it is not important right now
            topleft =  (-size[0] / 2, size[1] / 2)
            bottomright = (size[0] / 2, -size[1] / 2)

            #print(topleft, bottomright)

            quad_buffer.write(data=array.array('f', [
        
                topleft[0],     topleft[1],     0.0, 0.0,
                bottomright[0], topleft[1],     1.0, 0.0,
                topleft[0],     bottomright[1], 0.0, 1.0,
                bottomright[0], bottomright[1], 1.0, 1.0,
            ]))


            render_object = ctx.vertex_array(app.shader_programs.quad_shader, [(quad_buffer, '2f 2f', 'vert', 'texcoord')])
            

            loaded_shaders[sprite_set] = [app.shader_programs.quad_shader, render_object, quad_buffer]

        
        textures_cutout[sprite_set]['frames'] = frames
        textures_cutout[sprite_set]['colour_key'] = spritesheet_data[sprite_set]['colour_key']
        textures_cutout[sprite_set]['shader'] = spritesheet_data[sprite_set]['shader']

    return textures_cutout, loaded_shaders


# Create a function that opens image files if the extention is valid