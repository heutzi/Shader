from array import array
import moderngl
import pygame
import sys

DEFAULT_SCREEN_SIZE = (800, 600)

pygame.init()
screen = pygame.display.set_mode(
    DEFAULT_SCREEN_SIZE,
    pygame.OPENGL | pygame.DOUBLEBUF
    )
display = pygame.Surface((DEFAULT_SCREEN_SIZE))
context = moderngl.create_context()
clock = pygame.time.Clock()
image = pygame.image.load('images/image.jpeg')
image = pygame.transform.scale(image, DEFAULT_SCREEN_SIZE)

quad_buffer = context.buffer(data=array('f', [
    # position (x,y) ; texture coord (u,v)
    # coordinates x, y in OpenGL go from -1 to +1
    # coordinates u, v in OpenGL go from 0 to +1
    # (u, v) coordinates are flipped to account for
    #    coordinates being reversed in pygame
    -1., +1., +0., +0.,  # left  - top
    +1., +1., +1., +0.,  # right - top
    -1., -1., +0., +1.,  # left  - bottom
    +1., -1., +1., +1.,  # right - bottom
]))


def open_shader(source_file: str) -> str:
    with open(source_file, 'r') as file:
        shader_code = file.read()
    return shader_code


vert_shader = open_shader('shader_vert.glsl')

frag_shader = open_shader('shader_frag.glsl')

program = context.program(vertex_shader=vert_shader,
                          fragment_shader=frag_shader)
render_object = context.vertex_array(
    program,
    [(quad_buffer, '2f 2f', 'vert', 'texcoord')]
    )


def surf_to_texture(surf: pygame.Surface) -> moderngl.Texture:
    tex = context.texture(surf.get_size(), 4)
    # defines interpollation
    tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
    # defines how the channels are mapped to each other
    tex.swizzle = 'BGRA'
    tex.write(surf.get_view('1'))
    return tex


t = 0.
while True:
    display.fill((0, 0, 0))
    # display.blit(img, pygame.mouse.get_pos())
    display.blit(image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    frame_tex = surf_to_texture(display)
    frame_tex.use(0)
    program['tex'] = 0
    program['time'] = t
    render_object.render(mode=moderngl.TRIANGLE_STRIP)

    pygame.display.flip()

    frame_tex.release()
    t += 1.
    clock.tick(60)
