from __future__ import annotations


class CallbackDataGenerator(str):
    '''
    A class which generates string via calling the not existed attributes, for example:
    Setup default splitter "_"

    And try to get the result:

    gen = CallbackDataGenerator()
    result = gen.box.game.click.arg("123456789")
    print(result) # "box_game_click_message_123456789"


    This is useful to generate the same callback data objects

    '''
    default_splitter = "_"

    def __getattr__(self, item: str) -> CallbackDataGenerator:
        return self.arg(item)

    def arg(self, argument: object) -> CallbackDataGenerator:
        if self.__len__() == 0:
            return self.__new(str(argument))
        return self.__new(self + self.default_splitter + str(argument))

    @classmethod
    def __new(cls, o: object) -> CallbackDataGenerator:
        return cls(o)

