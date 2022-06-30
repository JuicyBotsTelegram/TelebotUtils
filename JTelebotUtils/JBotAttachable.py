from __future__ import annotations

from typing import Callable

import telebot
from Extensions import TMsgExt
from JTelebotUtils.Utils import generateComparatorToCheckIfUserIsAdmin


class JBotAttachable:

    @classmethod
    def attachHandlers(cls, _bot: telebot.TeleBot):
        """
        Abstract method which helps to attach telebot handlers.
        Example:
            _bot.register_message_handler(cls.someFunction, func=lambda msg: msg.text.contains('carma_my_chat') and fromGroupPrivate(msg))
            _bot.register_callback_query_handler(cls.joinCarmaGameCall, func=lambda call: call_starts(call, 'game_carma_join'))
        """
        raise NotImplementedError()


class JBotEvaluator(JBotAttachable):
    evalPrefix: str = "C/"
    adminIds: list[int] = []
    isAdmin: Callable[[telebot.types.Message], bool] = generateComparatorToCheckIfUserIsAdmin(adminIds)

    @classmethod
    def __recreateIsAdmin(cls):
        cls.isAdmin = generateComparatorToCheckIfUserIsAdmin(cls.adminIds)

    @staticmethod
    def evalCommands(msg: telebot.types.Message, bot: telebot.TeleBot):
        try:
            splited_text = telebot.util.split_string(str(eval(msg.text[len(JBotEvaluator.evalPrefix):])), 3000)
            for text in splited_text:
                bot.send_message(msg.chat.id, text)
        except BaseException as e:
            bot.send_message(msg.chat.id, str(e))

    @classmethod
    def attachHandlers(cls, _bot: telebot.TeleBot) -> list[str]:
        """
        :param _bot:
        :returns: the list of accepted message commands for future setting it in bot via command bot#.set_my_commands
        """
        accepted_commands = list()
        _bot.register_message_handler(cls.evalCommands, func=lambda msg: TMsgExt.isMsgTextStartsWith(msg, cls.evalPrefix) and cls.isAdmin(msg))
        return accepted_commands

    @classmethod
    def attachHandlersWithProperties(cls, _bot: telebot.TeleBot, admin_ids: list[int]) -> list[str]:
        cls.adminIds = admin_ids
        cls.__recreateIsAdmin()
        return cls.attachHandlers(_bot)
