from __future__ import annotations

import re
from typing import Callable

import telebot.types as types


def generateComparatorToCheckIfUserIsAdmin(admin_ids: list[int]) -> Callable[[types.Message], bool]:
    def isAdmin(msg: types.Message) -> bool:
        return msg.from_user.id in admin_ids
    return isAdmin


def isTextCommand(bot_name: str) -> Callable[[types.Message, str | list[str], bool], bool]:

    def it_cmd(msg: types.Message, command: str | list[str], use_bot_name: bool = False):
        if not msg.text: return False
        commands = [command] if isinstance(command, str) else command
        name = bot_name if use_bot_name else ''

        for command in commands:
            if msg.text.lower().startswith(f"/{command}{name}".lower()):
                return True
        return False

    return it_cmd


def cle(text: str):
    """Clears text from special symbols which caused errors"""
    return re.sub('[<*`•>]', '?', text)


def cut_it(text: str, off=14, fill_with_symbol: str = "."):
    if off:
        return text[:off].ljust(off + 2, fill_with_symbol) if len(text) > off else text
    return text


def vice_versa_of_01(int_0_or_1: int) -> int:
    """
    :param int_0_or_1: An integer that could be 0 or 1
    :return: returns the alternative variant. if inputed 0 -> 1 will be outputed
    """
    return abs(int(int_0_or_1) - 1)
