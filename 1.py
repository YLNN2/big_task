import requests
import os
import pygame


class MapPic(object):
    def __init__(self):
        pass

    def ll(self):
        return [self.lon, self.lin]

    def change_spn(self, spn):
        self.spn = spn

    def get_map_request(self):
        pass


def load_map(mp):
    map_request = mp.get_map_request()

    response = requests.get(map_request)
    if not response:
        print('Error')
        print(f'HTTP error: {response}')
    else:
        map_file = "map.png"
        with open(map_file, 'wb+') as f:
            f.write(response.content)


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 450))

    map = MapPic()
    load_map(map)
    map_image = pygame.image.load("map.png")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(map_image, [0, 0])
        pygame.display.flip()

    os.remove("map.png")
    pygame.quit()


main()
