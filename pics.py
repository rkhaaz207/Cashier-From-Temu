import pygame
import os

_img_pelanggan_list = []
_img_box = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_img_pelanggan_list():
    global _img_pelanggan_list
    if not _img_pelanggan_list:
        try:
            path1 = os.path.join(BASE_DIR, "assets", "customer.png")
            img1 = pygame.image.load(path1)
            _img_pelanggan_list.append(pygame.transform.scale(img1, (40, 40)))
        except FileNotFoundError:
            surf1 = pygame.Surface((40, 40))
            surf1.fill((255, 100, 100))
            _img_pelanggan_list.append(surf1)
        try:
            path2 = os.path.join(BASE_DIR, "assets", "customer2.png")
            img2 = pygame.image.load(path2)
            _img_pelanggan_list.append(pygame.transform.scale(img2, (40, 40)))
        except FileNotFoundError:
            surf2 = pygame.Surface((40, 40))
            surf2.fill((255, 200, 100))
            _img_pelanggan_list.append(surf2)
            
    return _img_pelanggan_list

def get_img_box():
    global _img_box
    if _img_box is None:
        try:
            path_gambar = os.path.join(BASE_DIR, "assets", "box.png")
            img = pygame.image.load(path_gambar)
            _img_box = pygame.transform.scale(img, (30, 30))
        except FileNotFoundError:
            _img_box = pygame.Surface((30, 30))
            _img_box.fill((100, 200, 100))
    return _img_box