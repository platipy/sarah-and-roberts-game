import pygame
import random
import sys

SIZE = (1920, 1080)


def clamp(value, lower, upper):
    return max(min(value, upper), lower)


def clamp2d(point, size):
    """
    >>> clamp2d((-1, -1), (10, 10))
    (0, 0)
    >>> clamp2d((-100, 100), (10, 10))
    (0, 10)
    """
    return (clamp(point[0], 0, size[0]), clamp(point[1], 0, size[1]))


def init():
    pygame.init()
    pygame.display.set_mode(SIZE)


def draw_cursor(surface, size_px, position, color):
    cursor = pygame.Surface((size_px, size_px))
    cursor.fill(color)
    surface.blit(cursor, clamp2d(position, (SIZE[0] - size_px, SIZE[1] - size_px)))


def main():
    init()
    sizes = range(3, 60, 7)
    size_idx = 0
    shift_held = False

    s = pygame.display.get_surface()
    draw_cursor(s, sizes[-1], (0, 0), (255, 255, 255))

    color_selector = 0
    color_inc = (
        random.randint(0, 256)
        + 256 ** 2
        + random.randint(0, 256)
        + 256
        + random.randint(0, 256)
    )
    drawing = True
    color_scheme = "random" if sys.argv[-1] == "random" else "gradient"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == ord('q'):
                return
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                size_idx = (size_idx + 1) % len(sizes)
            if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                drawing = not drawing
            if event.type == pygame.MOUSEMOTION and drawing:
                if pygame.key.get_mods() & pygame.KMOD_LCTRL:
                    color = (0, 0, 0)
                else:
                    if color_scheme == "random":
                        color = (
                            random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255),
                        )
                    else:
                        color = (
                            color_selector % (256 ** 3) >> 16,
                            color_selector % (256 ** 2) >> 8,
                            color_selector % 256,
                        )
                        color_selector += color_inc
                draw_cursor(s, sizes[size_idx], event.pos, color)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
                shift_held = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_LSHIFT:
                shift_held = False
            elif event.type == pygame.KEYUP and event.key == ord("c"):
                s.fill((0, 0, 0))
                draw_cursor(s, sizes[-1], (0, 0), (255, 255, 255))
            if shift_held:
                draw_cursor(s, sizes[size_idx], (0, 0), (0, 255, 0))
            pygame.display.update()
            pygame.display.flip()
            draw_cursor(s, sizes[-1], (0, 0), (255, 255, 255))


if __name__ == "__main__":
    main()
