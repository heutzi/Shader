from array import array
import moderngl
import pygame
import sys

import modules.processing as proces

DEFAULT_SCREEN_SIZE = (600, 600)

pygame.init()

screen = pygame.display.set_mode(
    DEFAULT_SCREEN_SIZE,
    pygame.OPENGL | pygame.DOUBLEBUF
    )
display = pygame.Surface((DEFAULT_SCREEN_SIZE))
clock = pygame.time.Clock()
image = pygame.image.load('images/teacup.jpg')
image = pygame.transform.scale(image, DEFAULT_SCREEN_SIZE)

context = moderngl.create_context()

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


vert_shader = proces.open_shader('shader_vert.glsl')

frag_shader = proces.open_shader('shader_frag.glsl')

program = context.program(vertex_shader=vert_shader,
                          fragment_shader=frag_shader)
render_object = context.vertex_array(
    program,
    [(quad_buffer, '2f 2f', 'vert', 'texcoord')]
    )

tex_noise = proces.image_to_texture('images/blue_noise.jpg',
                                    DEFAULT_SCREEN_SIZE,
                                    context)

t = 0.
while True:
    display.fill((0, 0, 0))
    # display.blit(img, pygame.mouse.get_pos())
    display.blit(image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tex_image = proces.surf_to_texture(display, context)

    tex_image.use(0)
    program['tex_image'] = 0

    tex_noise.use(1)
    program['tex_noise'] = 1

    # program['time'] = t
    # program['screen_width'] = DEFAULT_SCREEN_SIZE[1]

    render_object.render(mode=moderngl.TRIANGLE_STRIP)

    pygame.display.flip()

    tex_image.release()
    t += 1.
    clock.tick(60)
