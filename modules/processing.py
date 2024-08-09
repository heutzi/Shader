import pygame
import moderngl


def open_shader(source_file: str) -> str:
    with open(source_file, 'r') as file:
        shader_code = file.read()
    return shader_code


def surf_to_texture(surf: pygame.Surface, context: moderngl.Context) \
        -> moderngl.Texture:
    tex = context.texture(surf.get_size(), 4)
    # defines interpollation
    tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
    # defines how the channels are mapped to each other
    tex.swizzle = 'BGRA'
    tex.write(surf.get_view('1'))
    return tex


def image_to_texture(image_file: str,
                     screen_size: tuple[int, int],
                     context: moderngl.Context) \
        -> moderngl.Texture:
    image = pygame.image.load(image_file)
    image = pygame.transform.scale(image, screen_size)
    print(image.get_size())
    tex = context.texture(screen_size, 3)
    tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
    tex.swizzle = 'BGR'
    tex.write(image.get_view('1'))
    return tex
