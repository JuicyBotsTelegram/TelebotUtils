from telebot import TeleBot

from JTelebotUtils.JBotAttachable import JBotAttachable


class JBotHolder(JBotAttachable):
    def __init__(self, bot: TeleBot, attach_handlers: bool):
        self.__bot: TeleBot = bot
        if attach_handlers:
            self.attachHandlers(bot)

    @property
    def bot(self) -> TeleBot: return self.__bot


