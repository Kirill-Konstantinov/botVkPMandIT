#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def stick():
    stickers = ['photo-193491601_457239061', 'photo-193491601_457239062', 'photo-193491601_457239063',
                'photo-193491601_457239064', 'photo-193491601_457239065', 'photo-193491601_457239066',
                'photo-193491601_457239067', 'photo-193491601_457239068', 'photo-193491601_457239069',
                'photo-193491601_457239070', 'photo-193491601_457239071', 'photo-193491601_457239072',
                'photo-193491601_457239073', 'photo-193491601_457239074', 'photo-193491601_457239075']

    sticker = random.randint(0, len(stickers)-1)

    try:
        return stickers[sticker]
    except:
        stick()