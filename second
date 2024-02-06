import os
import sys
import pygame
import requests

pygame.init()
def load_img(zoom):
    api_server = "http://static-maps.yandex.ru/1.x/"
    lon = "-3.70256"
    lat = "40.4165"
    params = {
        "ll": ",".join([lon, lat]),
        "l": "map",
        "z": str(zoom)
    }

    response = requests.get(api_server, params=params)

    if not response:
        print("Ошибка выполнения запроса:")
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))

    os.remove(map_file)


def main():
    zoom = 8
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if key[pygame.K_PAGEUP]:
                    if zoom != 21:
                        zoom += 1
                if key[pygame.K_PAGEDOWN]:
                    if zoom != 0:
                        zoom -= 1
        load_img(zoom)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
    
