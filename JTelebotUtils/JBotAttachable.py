from __future__ import annotations

import telebot


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

