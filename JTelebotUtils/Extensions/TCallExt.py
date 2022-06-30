import telebot


def isCallDataStartsWith(call: telebot.types.CallbackQuery, template: str) -> bool:
    return call.data.startswith(template)

