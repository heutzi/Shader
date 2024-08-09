import pygame
import moderngl


def surf_to_texture(surf: pygame.Surface, context: moderngl.Context) \
        -> moderngl.Texture:
    tex = context.texture(surf.get_size(), 4)
    # defines interpollation
    tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
    # defines how the channels are mapped to each other
    tex.swizzle = 'BGRA'
    tex.write(surf.get_view('1'))
    return tex
