from __future__ import annotations

from typing import Optional

import telebot
# TMsgExt means TelebotMessageExtensions
from JTelebotUtils.Models.ChatTypes import ChatTypes


def isFromGroupOrPrivate(msg: telebot.types.Message) -> bool:
    return isFromPrivate(msg) or isFromGroup(msg)


def isFromGroup(msg: telebot.types.Message) -> bool:
    return msg.chat.type in [ChatTypes.SUPERGROUP, ChatTypes.GROUP]


def isFromPrivate(msg: telebot.types.Message) -> bool:
    return msg.chat.type == ChatTypes.PRIVATE


def isFromChannel(msg: telebot.types.Message) -> bool:
    return msg.chat.type == ChatTypes.CHANNEL


def isMsgTextStartsWith(msg: telebot.types.Message, template) -> bool:
    if msg.text:
        return msg.text.startswith(template)
    return False


def getCommandFromMsg(msg: telebot.types.Message) -> str:
    def unpack(text: str, length: Optional[int]) -> str:
        if '@' not in text[:length]:
            return text[:length]
        return text[:length].split('@')[0]

    command_length = msg.entities[0].length if '/' == msg.text[0] else None
    return unpack(msg.text, command_length)
