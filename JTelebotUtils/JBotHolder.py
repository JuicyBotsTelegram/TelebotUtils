import telebot

from JTelebotUtils.JBotAttachable import JBotAttachable


class JBotHolder(JBotAttachable):
    def __init__(self, bot: telebot.TeleBot, attach_handlers: bool):
        self.__bot: telebot.TeleBot = bot
        if attach_handlers:
            self.attachHandlers(bot)

    @property
    def bot(self) -> telebot.TeleBot: return self.__bot


