# -*- coding: utf-8 -*-
"""
This is game variables.
Author: havelockz
"""

__author__ = "havelockz"

import time
import random
import threading

import pygame
import pygame.locals as gloc

import myplane
import enemy
import boss
import bullet
import supply
import sql

bg_size = width, height = 480, 700
destroy_images = {}
transitional_image = {}


def add_enemies(fn: str,
                num: int,
                *args: pygame.sprite.Group) -> None:
    global destroy_images
    for i in range(num):
        if fn not in destroy_images:
            if fn == "SmallEnemy":
                destroy_images[fn] = [
                        pygame.image.load('images/enemies/enemy1_down1.png')
                        .convert_alpha(),
                        pygame.image.load('images/enemies/enemy1_down2.png')
                        .convert_alpha(),
                        pygame.image.load('images/enemies/enemy1_down3.png')
                        .convert_alpha(),
                        pygame.image.load('images/enemies/enemy1_down4.png')
                        .convert_alpha()
                        ]
            elif fn == "MidEnemy":
                destroy_images[fn] = [
                        pygame.image.load('images/enemies/enemy2_down1.png')
                        .convert_alpha(),
                        pygame.image.load('images/enemies/enemy2_down2.png')
                        .convert_alpha(),
                        pygame.image.load('images/enemies/enemy2_down3.png')
                        .convert_alpha(),
                        pygame.image.load('images/enemies/enemy2_down4.png')
                        .convert_alpha()
                        ]
            elif fn == "BigEnemy":
                destroy_images[fn] = [
                        pygame.image.load('images/enemies/enemy3_down1.png')
                        .convert_alpha(),
                        pygame.image.load('images/enemies/enemy3_down2.png')
                        .convert_alpha(),
                        pygame.image.load('images/enemies/enemy3_down3.png')
                        .convert_alpha(),
                        pygame.image.load('images/enemies/enemy3_down4.png')
                        .convert_alpha(),
                        pygame.image.load('images/enemies/enemy3_down5.png')
                        .convert_alpha(),
                        pygame.image.load('images/enemies/enemy3_down6.png')
                        .convert_alpha()
                        ]
        e = eval("enemy.%s(bg_size, destroy_images[fn])" % fn)
        for group in args:
            if isinstance(group, pygame.sprite.Group):
                group.add(e)


def init_bullet(fn: pygame.sprite.Sprite,
                num: int,
                *args: tuple) -> list:
    bullets = []
    for i in range(num // len(args)):
        for each in args:
            bullets.append(fn(each, bg_size))
    return bullets


def init_boss(fn: str) -> pygame.sprite.Sprite:
    if fn not in destroy_images:
        if fn == "Boss_lv1":
            transitional_image[fn] = [
                    pygame.image.load('boss/lv1/1.png').convert_alpha(),
                    pygame.image.load('boss/lv1/2.png').convert_alpha(),
                    pygame.image.load('boss/lv1/3.png').convert_alpha(),
                    pygame.image.load('boss/lv1/4.png').convert_alpha(),
                    pygame.image.load('boss/lv1/5.png').convert_alpha(),
                    pygame.image.load('boss/lv1/6.png').convert_alpha(),
                    pygame.image.load('boss/lv1/7.png').convert_alpha(),
                    pygame.image.load('boss/lv1/8.png').convert_alpha(),
                    pygame.image.load('boss/lv1/9.png').convert_alpha(),
                    pygame.image.load('boss/lv1/10.png').convert_alpha(),
                    pygame.image.load('boss/lv1/11.png').convert_alpha(),
                    pygame.image.load('boss/lv1/12.png').convert_alpha(),
                    pygame.image.load('boss/lv1/13.png').convert_alpha(),
                    pygame.image.load('boss/lv1/14.png').convert_alpha(),
                    pygame.image.load('boss/lv1/15.png').convert_alpha(),
                    pygame.image.load('boss/lv1/16.png').convert_alpha(),
                    pygame.image.load('boss/lv1/17.png').convert_alpha(),
                    pygame.image.load('boss/lv1/18.png').convert_alpha(),
                    pygame.image.load('boss/lv1/19.png').convert_alpha(),
                    pygame.image.load('boss/lv1/20.png').convert_alpha(),
                    pygame.image.load('boss/lv1/21.png').convert_alpha(),
                    pygame.image.load('boss/lv1/22.png').convert_alpha(),
                    pygame.image.load('boss/lv1/23.png').convert_alpha(),
                    pygame.image.load('boss/lv1/23_1.png').convert_alpha(),
                    pygame.image.load('boss/lv1/23_2.png').convert_alpha(),
                    pygame.image.load('boss/lv1/23_3.png').convert_alpha(),
                    pygame.image.load('boss/lv1/24.png').convert_alpha(),
                    pygame.image.load('boss/lv1/25.png').convert_alpha(),
                    pygame.image.load('boss/lv1/26.png').convert_alpha(),
                    pygame.image.load('boss/lv1/27.png').convert_alpha(),
                    pygame.image.load('boss/lv1/28.png').convert_alpha(),
                    pygame.image.load('boss/lv1/29.png').convert_alpha(),
                    pygame.image.load('boss/lv1/30.png').convert_alpha(),
                    pygame.image.load('boss/lv1/31.png').convert_alpha(),
                    pygame.image.load('boss/lv1/32.png').convert_alpha(),
                    pygame.image.load('boss/lv1/33.png').convert_alpha()
                ]
            destroy_images[fn] = [
                    pygame.image.load('boss/lv1/end_1.png').convert_alpha(),
                    pygame.image.load('boss/lv1/end_2.png').convert_alpha(),
                    pygame.image.load('boss/lv1/end_3.png').convert_alpha(),
                    pygame.image.load('boss/lv1/end_4.png').convert_alpha(),
                    pygame.image.load('boss/lv1/end_5.png').convert_alpha(),
                    pygame.image.load('boss/lv1/end_6.png').convert_alpha(),
                    pygame.image.load('boss/lv1/end_7.png').convert_alpha(),
                    pygame.image.load('boss/lv1/end_8.png').convert_alpha(),
                    pygame.image.load('boss/lv1/end_9.png').convert_alpha(),
                    pygame.image.load('boss/lv1/end_10.png').convert_alpha(),
                    pygame.image.load('boss/lv1/end_11.png').convert_alpha(),
                    pygame.image.load('boss/lv1/end_12.png').convert_alpha(),
                    pygame.image.load('boss/lv1/end_13.png').convert_alpha(),
                    pygame.image.load('boss/lv1/end_14.png').convert_alpha(),
                    pygame.image.load('boss/lv1/end_15.png').convert_alpha(),
                    pygame.image.load('boss/lv1/end_16.png').convert_alpha(),
                    pygame.image.load('boss/lv1/end_17.png').convert_alpha(),
                    pygame.image.load('boss/lv1/end_18.png').convert_alpha(),
                    pygame.image.load('boss/lv1/end_19.png').convert_alpha()
                ]
        elif fn == "Boss_lv2":
            transitional_image[fn] = [
                    pygame.image.load('boss/lv2/1.png').convert_alpha(),
                    pygame.image.load('boss/lv2/2.png').convert_alpha(),
                    pygame.image.load('boss/lv2/4.png').convert_alpha(),
                    pygame.image.load('boss/lv2/5.png').convert_alpha(),
                    pygame.image.load('boss/lv2/6.png').convert_alpha(),
                    pygame.image.load('boss/lv2/8.png').convert_alpha(),
                    pygame.image.load('boss/lv2/9.png').convert_alpha(),
                    pygame.image.load('boss/lv2/10.png').convert_alpha(),
                    pygame.image.load('boss/lv2/11.png').convert_alpha(),
                    pygame.image.load('boss/lv2/12.png').convert_alpha(),
                    pygame.image.load('boss/lv2/13.png').convert_alpha(),
                    pygame.image.load('boss/lv2/14.png').convert_alpha(),
                    pygame.image.load('boss/lv2/15.png').convert_alpha(),
                    pygame.image.load('boss/lv2/16.png').convert_alpha(),
                    pygame.image.load('boss/lv2/17.png').convert_alpha(),
                    pygame.image.load('boss/lv2/18.png').convert_alpha(),
                    pygame.image.load('boss/lv2/19.png').convert_alpha(),
                    pygame.image.load('boss/lv2/20.png').convert_alpha(),
                    pygame.image.load('boss/lv2/21.png').convert_alpha(),
                    pygame.image.load('boss/lv2/22.png').convert_alpha(),
                    pygame.image.load('boss/lv2/23.png').convert_alpha(),
                    pygame.image.load('boss/lv2/24.png').convert_alpha(),
                    pygame.image.load('boss/lv2/24_1.png').convert_alpha(),
                    pygame.image.load('boss/lv2/24_2.png').convert_alpha(),
                    pygame.image.load('boss/lv2/24_3.png').convert_alpha(),
                    pygame.image.load('boss/lv2/25.png').convert_alpha(),
                    pygame.image.load('boss/lv2/26.png').convert_alpha(),
                    pygame.image.load('boss/lv2/27.png').convert_alpha(),
                    pygame.image.load('boss/lv2/28.png').convert_alpha(),
                    pygame.image.load('boss/lv2/29.png').convert_alpha(),
                    pygame.image.load('boss/lv2/30.png').convert_alpha(),
                    pygame.image.load('boss/lv2/31.png').convert_alpha(),
                    pygame.image.load('boss/lv2/32.png').convert_alpha()
                ]
            destroy_images[fn] = [
                    pygame.image.load('boss/lv2/end_1.png').convert_alpha(),
                    pygame.image.load('boss/lv2/end_2.png').convert_alpha(),
                    pygame.image.load('boss/lv2/end_3.png').convert_alpha(),
                    pygame.image.load('boss/lv2/end_4.png').convert_alpha(),
                    pygame.image.load('boss/lv2/end_5.png').convert_alpha(),
                    pygame.image.load('boss/lv2/end_6.png').convert_alpha(),
                    pygame.image.load('boss/lv2/end_7.png').convert_alpha(),
                    pygame.image.load('boss/lv2/end_8.png').convert_alpha(),
                    pygame.image.load('boss/lv2/end_9.png').convert_alpha(),
                    pygame.image.load('boss/lv2/end_10.png').convert_alpha(),
                    pygame.image.load('boss/lv2/end_11.png').convert_alpha(),
                    pygame.image.load('boss/lv2/end_12.png').convert_alpha(),
                    pygame.image.load('boss/lv2/end_13.png').convert_alpha(),
                    pygame.image.load('boss/lv2/end_14.png').convert_alpha(),
                    pygame.image.load('boss/lv2/end_15.png').convert_alpha(),
                    pygame.image.load('boss/lv2/end_16.png').convert_alpha(),
                    pygame.image.load('boss/lv2/end_17.png').convert_alpha(),
                    pygame.image.load('boss/lv2/end_18.png').convert_alpha(),
                    pygame.image.load('boss/lv2/end_19.png').convert_alpha()
                ]
        elif fn == "Boss_lv3":
            transitional_image[fn] = [
                    pygame.image.load('boss/lv3/1.png').convert_alpha(),
                    pygame.image.load('boss/lv3/2.png').convert_alpha(),
                    pygame.image.load('boss/lv3/4.png').convert_alpha(),
                    pygame.image.load('boss/lv3/5.png').convert_alpha(),
                    pygame.image.load('boss/lv3/6.png').convert_alpha(),
                    pygame.image.load('boss/lv3/8.png').convert_alpha(),
                    pygame.image.load('boss/lv3/9.png').convert_alpha(),
                    pygame.image.load('boss/lv3/10.png').convert_alpha(),
                    pygame.image.load('boss/lv3/11.png').convert_alpha(),
                    pygame.image.load('boss/lv3/12.png').convert_alpha(),
                    pygame.image.load('boss/lv3/13.png').convert_alpha(),
                    pygame.image.load('boss/lv3/14.png').convert_alpha(),
                    pygame.image.load('boss/lv3/15.png').convert_alpha(),
                    pygame.image.load('boss/lv3/16.png').convert_alpha(),
                    pygame.image.load('boss/lv3/17.png').convert_alpha(),
                    pygame.image.load('boss/lv3/18.png').convert_alpha(),
                    pygame.image.load('boss/lv3/19.png').convert_alpha(),
                    pygame.image.load('boss/lv3/20.png').convert_alpha(),
                    pygame.image.load('boss/lv3/20_1.png').convert_alpha(),
                    pygame.image.load('boss/lv3/20_2.png').convert_alpha(),
                    pygame.image.load('boss/lv3/20_3.png').convert_alpha(),
                    pygame.image.load('boss/lv3/21.png').convert_alpha(),
                    pygame.image.load('boss/lv3/22.png').convert_alpha(),
                    pygame.image.load('boss/lv3/23.png').convert_alpha(),
                    pygame.image.load('boss/lv3/24.png').convert_alpha(),
                    pygame.image.load('boss/lv3/25.png').convert_alpha(),
                    pygame.image.load('boss/lv3/26.png').convert_alpha(),
                    pygame.image.load('boss/lv3/27.png').convert_alpha(),
                    pygame.image.load('boss/lv3/28.png').convert_alpha()
                ]
            destroy_images[fn] = [
                    pygame.image.load('boss/lv3/end_1.png').convert_alpha(),
                    pygame.image.load('boss/lv3/end_2.png').convert_alpha(),
                    pygame.image.load('boss/lv3/end_3.png').convert_alpha(),
                    pygame.image.load('boss/lv3/end_4.png').convert_alpha(),
                    pygame.image.load('boss/lv3/end_5.png').convert_alpha(),
                    pygame.image.load('boss/lv3/end_6.png').convert_alpha(),
                    pygame.image.load('boss/lv3/end_7.png').convert_alpha(),
                    pygame.image.load('boss/lv3/end_8.png').convert_alpha(),
                    pygame.image.load('boss/lv3/end_9.png').convert_alpha(),
                    pygame.image.load('boss/lv3/end_10.png').convert_alpha(),
                    pygame.image.load('boss/lv3/end_11.png').convert_alpha(),
                    pygame.image.load('boss/lv3/end_12.png').convert_alpha(),
                    pygame.image.load('boss/lv3/end_13.png').convert_alpha(),
                    pygame.image.load('boss/lv3/end_14.png').convert_alpha(),
                    pygame.image.load('boss/lv3/end_15.png').convert_alpha(),
                    pygame.image.load('boss/lv3/end_16.png').convert_alpha(),
                    pygame.image.load('boss/lv3/end_17.png').convert_alpha(),
                    pygame.image.load('boss/lv3/end_18.png').convert_alpha(),
                    pygame.image.load('boss/lv3/end_19.png').convert_alpha()
                ]
    return eval("boss.%s(bg_size, transitional_image[fn], destroy_images[fn])"
                % fn)


def change_music(boss_appear: bool = False, play: bool = True) -> None:
    if not boss_appear:
        pygame.mixer.music.load('sound/game_music.ogg')
    else:
        if random.choice([True, False]):
            pygame.mixer.music.load('sound/base.ogg')
        else:
            pygame.mixer.music.load('sound/jungle.ogg')
    if play:
        pygame.mixer.music.play(-1)


def inc_speed(target: pygame.sprite.Group, inc: int) -> None:
    for each in target:
        each.speed += inc


def kill_enemies(group: pygame.sprite.Group) -> None:
    for each in group:
        if each.rect.bottom > 0:
            each.active = False


def init(game):
    game.me = myplane.MyPlane(bg_size)
    change_music()

    game.bullets = None
    game.update = False

    game.level = 1

    game.supply_time = time.time()
    game.SUPPLY_TIME = gloc.USEREVENT

    game.is_double = False

    game.score = 0
    game.record_score = sql.Sql.get_score()

    game.recorded = False

    game.paused = False
    if not hasattr(game, "pause_nor_image"):
        game.pause_nor_image = pygame.image.load(
                'images/pause_nor.png').convert_alpha()
        game.pause_pressed_image = pygame.image.load(
                'images/pause_pressed.png').convert_alpha()
        game.resume_nor_image = pygame.image.load(
                'images/resume_nor.png').convert_alpha()
        game.resume_pressed_image = pygame.image.load(
                'images/resume_pressed.png').convert_alpha()
        game.paused_rect = game.pause_nor_image.get_rect()
        game.paused_rect.left = width - game.paused_rect.width - 10
        game.paused_rect.top = 10
    game.paused_image = game.pause_nor_image

    game.switch_image = True

    game.delay = 100

    # 生命条数
    game.life_num = 3

    game.start = True

    game._help = False

    game.transition = False
    game.trans_delay = 12
    game.trans_num = 0

    game.boss_lv = 0
    game.boss_appear = False

    if not hasattr(game, "bullet_supply"):
        game.bullet_supply = supply.Bullet_Supply(game.bg_size)
        game.bomb_supply = supply.Bomb_Supply(game.bg_size)
        game.bullet_update = supply.Bullet_Update(game.bg_size)
        game.medical_supply = supply.Medical_supply(game.bg_size)
        game.SUPPLY_TIME = gloc.USEREVENT
    pygame.time.set_timer(game.SUPPLY_TIME, 0)

    if not hasattr(game, "DOUBLE_BULLET_TIME"):
        game.DOUBLE_BULLET_TIME = gloc.USEREVENT + 1
    pygame.time.set_timer(game.DOUBLE_BULLET_TIME, 0)

    game.score_font = pygame.font.Font('font/font.ttf', 36)

    if not hasattr(game, "pause_nor_iamge"):
        game.pause_nor_image = pygame.image.load(
                'images/pause_nor.png').convert_alpha()
        game.pause_pressed_image = pygame.image.load(
                'images/pause_pressed.png').convert_alpha()
        game.resume_nor_image = pygame.image.load(
                'images/resume_nor.png').convert_alpha()
        game.resume_pressed_image = pygame.image.load(
                'images/resume_pressed.png').convert_alpha()
        game.paused_rect = game.pause_nor_image.get_rect()
        game.paused_rect.left = width - game.paused_rect.width - 10
        game.paused_rect.top = 10
        game.pause_restart = pygame.image.load(
                'images/restart.png').convert_alpha()
        game.pause_restart_rect = game.pause_restart.get_rect()
        game.pause_restart_rect.left, game.pause_restart_rect.top = 130, 300
        game.pause_quit = pygame.image.load('images/quit.png').convert_alpha()
        game.pause_quit_rect = game.pause_quit.get_rect()
        game.pause_quit_rect.left, game.pause_quit_rect.top = 310, 300
    game.paused_image = game.pause_nor_image

    if not hasattr(game, "INVINCIBLE_TIME"):
        game.INVINCIBLE_TIME = gloc.USEREVENT + 2
    pygame.time.set_timer(game.INVINCIBLE_TIME, 0)

    if not hasattr(game, "author_font"):
        game.title_image = pygame.image.load('images/start/title.png')\
            .convert_alpha()
        game.title_image_rect = game.title_image.get_rect()
        game.title_image_rect.left = (width - game.title_image_rect.width) // 2
        game.title_image_rect.top = (height // 3) - 40

        game.start_image = pygame.image.load('images/start/start.png')\
            .convert_alpha()
        game.start_rect = game.start_image.get_rect()
        game.start_rect.left = (width - game.start_rect.width) // 2
        game.start_rect.top = 413

        game.help_image = pygame.image.load('images/start/help.png')\
            .convert_alpha()
        game.help_rect = game.help_image.get_rect()
        game.help_rect.left = (width - game.help_rect.width) // 2
        game.help_rect.top = 463

        game.exit_image = pygame.image.load('images/start/exit.png')\
            .convert_alpha()
        game.exit_rect = game.exit_image.get_rect()
        game.exit_rect.left = (width - game.exit_rect.width) // 2
        game.exit_rect.top = 513

        game.author_font = pygame.font.Font('font/msyh.ttf', 20)
        game.author_text = game.author_font.render(
                'directed by : havelockz', True, game.WHITE)
        game.author_text_rect = game.author_text.get_rect()
        game.author_text_rect.left = width - game.author_text_rect.width - 10
        game.author_text_rect.top = height - game.author_text_rect.height - 10

    if not hasattr(game, "gameover_font"):
        game.gameover_font = pygame.font.Font('font/font.ttf', 48)
        game.again_image = pygame.image.load('images/start/again.png')\
            .convert_alpha()
        game.again_rect = game.again_image.get_rect()
        game.gameover_image = pygame.image.load('images/start/gameover.png')\
            .convert_alpha()
        game.gameover_rect = game.gameover_image.get_rect()


class Initializer(threading.Thread):
    def __init__(self, game):
        threading.Thread.__init__(self)
        self.game = game

    def run(self):
        self.game.enemies = pygame.sprite.Group()
        self.game.small_enemies = pygame.sprite.Group()
        add_enemies("SmallEnemy", 15,
                    self.game.small_enemies, self.game.enemies)
        self.game.mid_enemies = pygame.sprite.Group()
        add_enemies("MidEnemy", 4, self.game.mid_enemies, self.game.enemies)
        self.game.big_enemies = pygame.sprite.Group()
        add_enemies("BigEnemy", 2, self.game.big_enemies, self.game.enemies)

        self.game.bullet1_index = 0
        self.game.BULLET1_NUM = 4
        self.game.bullet1 = init_bullet(
                bullet.Bullet1, self.game.BULLET1_NUM, (240, 1000))

        self.game.bullet2_index = 0
        self.game.BULLET2_NUM = 8
        self.game.bullet2 = init_bullet(
                bullet.Bullet2,
                self.game.BULLET2_NUM,
                (240, 1000))

        self.game.bullet3_index = 0
        self.game.BULLET3_NUM = 4
        self.game.bullet3 = init_bullet(
                bullet.Bullet3, self.game.BULLET3_NUM, (240, 1000))

        self.game.bullet4_index = 0
        self.game.BULLET4_NUM = 8
        self.game.bullet4 = init_bullet(
                bullet.Bullet4,
                self.game.BULLET4_NUM,
                (240, 1000))

        self.game.boss_now = None
        self.game.boss_group = pygame.sprite.Group()
        self.game.boss_lv1 = init_boss("Boss_lv1")
        self.game.boss_lv2 = init_boss("Boss_lv2")
        self.game.boss_lv3 = init_boss("Boss_lv3")
        self.game.boss_group.add(self.game.boss_lv1, self.game.boss_lv2,
                                 self.game.boss_lv3)

        self.game.boss_bullet = None
        self.game.boss_bullet_index = 0
        self.game.BOSS_BULLET_NUM = 4
        self.game.boss_bullet_1 = init_bullet(
                bullet.Boss_bullet_lv1,
                self.game.BOSS_BULLET_NUM,
                self.game.boss_lv1.rect.midbottom)
        self.game.boss_bullet_2 = init_bullet(
                bullet.Boss_bullet_lv2,
                self.game.BOSS_BULLET_NUM,
                self.game.boss_lv2.rect.midbottom)
        self.game.boss_bullet_3 = init_bullet(
                bullet.Boss_bullet_lv3,
                self.game.BOSS_BULLET_NUM,
                self.game.boss_lv3.rect.midbottom)
