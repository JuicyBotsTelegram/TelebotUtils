from telebot import types
# TMsgExt means TelebotMessageExtensions
from JTelebotUtils.Models.ChatTypes import ChatTypes


def isFromGroup(msg: types.Message):
    return msg.chat.type in [ChatTypes.SUPERGROUP, ChatTypes.GROUP]


def isFromPrivate(msg: types.Message):
    return msg.chat.type == ChatTypes.PRIVATE


def isFromChannel(msg: types.Message):
    return msg.chat.type == ChatTypes.CHANNEL


