from __future__ import annotations

import telebot

from JTelebotUtils.Utils import cle


def makeFullName(first_name: str, last_name: str | None, user_name: str | None):
    last_name = ' '+last_name if last_name else ''
    user_name = ('(@'+user_name+')') if user_name else ''
    return cle(f'{first_name}{last_name}{user_name}')


def makeFullNameTG(u: telebot.types.User):
    return makeFullName(u.first_name, u.last_name, u.username)


def makeName(first_name: str, last_name: str | None):
    last_name = ' '+last_name if last_name else ''
    return cle(f'{first_name}{last_name}')


def makeNameTG(u: telebot.types.User):
    return makeName(u.first_name, u.last_name)
