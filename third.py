import os
import sys
import pygame
import requests

pygame.init()


def load_img(lon, lat, zoom):
    api_server = "http://static-maps.yandex.ru/1.x/"
    # lon = "-3.70256"
    # lat = "40.4165"
    params = {
        "ll": ",".join([str(lon), str(lat)]),
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
    lon = -3.70256
    lat = 40.4165
    zoom = 8
    delta = 360 // 4 ** (zoom//2)
    vr_lon, vr_lat = lon + 180, lat + 180
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
                if key[pygame.K_UP]:
                    vr_lat += delta
                    if vr_lat > 360 - 100*delta:
                        vr_lat = 360 - 100*delta
                    lat = vr_lat - 180
                if key[pygame.K_DOWN]:
                    vr_lat -= delta
                    if vr_lat < 100*delta:
                        vr_lat = 100*delta
                    lat = vr_lat - 180
                if key[pygame.K_LEFT]:
                    vr_lon -= delta
                    if vr_lon < 100 * delta:
                        vr_lon = 100 * delta
                    lon = vr_lon - 180
                if key[pygame.K_RIGHT]:
                    vr_lon += delta
                    if vr_lon > 360 - 100 * delta:
                        vr_lon = 360 - 100 * delta
                    lon = vr_lon - 180
        load_img(lon, lat, zoom)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
