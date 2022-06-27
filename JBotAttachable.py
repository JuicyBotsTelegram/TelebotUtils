from typing import Callable, Dict

from telebot import TeleBot


class JBotAttachable:

    @staticmethod
    def __buildHandlerDict(handler, **filters): return {'function': handler, 'filters': filters}

    @classmethod
    def __addMsgHandler(cls, bot: TeleBot, handler: Callable, **filters: Dict):
        bot.add_message_handler(cls.__buildHandlerDict(handler, **filters))

    @classmethod
    def __addCallHandler(cls, bot: TeleBot, handler: Callable, **filters):
        bot.add_callback_query_handler(cls.__buildHandlerDict(handler, **filters))

    @classmethod
    def attachHandlers(cls, bot: TeleBot):
        """
        Abstract method which helps to attach telebot handlers.
        Example:
            bot.addMsgHandler(cls.someFunction, func=lambda msg: msg.text.contains('carma_my_chat') and fromGroupPrivate(msg))
            bot.addCallHandler(cls.joinCarmaGameCall, func=lambda call: call_starts(call, 'game_carma_join'))
        """

        raise NotImplementedError()

