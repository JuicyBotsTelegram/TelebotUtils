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

