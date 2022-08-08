# TelebotUtils

#### TelebotUtils is a Python module which contains all the needed and related to Telebot library util-functions. As a rule they are for internal JuicyBotsTelegram projects

### 👉 How to install TelebotUtils module
Run `pip3.X install git+https://github.com/JuicyBotsTelegram/TelebotUtils`


## Overview

### Extension functions for `telebot.types.Callback`:

```python
isCallDataStartsWith(call: telebot.types.CallbackQuery, template: str) -> bool: 
```

> https://github.com/JuicyBotsTelegram/TelebotUtils/blob/bcf52394bb1bc645937ac301bb76cbeb8867ee9d/JTelebotUtils/Extensions/TCallExt.py#L4-L5


### Extension functions for `telebot.types.Message`:

```python
isFromGroupOrPrivate(msg: telebot.types.Message) -> bool
isFromGroup(msg: telebot.types.Message) -> bool
isFromPrivate(msg: telebot.types.Message) -> bool
isFromChannel(msg: telebot.types.Message) -> bool
isMsgTextStartsWith(msg: telebot.types.Message, template) -> bool
getCommandFromMsg(msg: telebot.types.Message) -> str
```

> https://github.com/JuicyBotsTelegram/TelebotUtils/blob/bcf52394bb1bc645937ac301bb76cbeb8867ee9d/JTelebotUtils/Extensions/TMsgExt.py#L10-L39


### Extension function to `telebot.types.User`:

```python
makeFullName(first_name: str, last_name: str | None, user_name: str | None) -> str
makeFullNameTG(u: telebot.types.User) -> str
makeName(first_name: str, last_name: str | None) -> str
makeNameTG(u: telebot.types.User) -> str
```

> https://github.com/JuicyBotsTelegram/TelebotUtils/blob/bcf52394bb1bc645937ac301bb76cbeb8867ee9d/JTelebotUtils/Extensions/TUserExt.py#L8-L24

## Utils functions

```python
generateComparatorToCheckIfUserIsAdmin(admin_ids: list[int]) -> Callable[[types.Message], bool]
isTextCommand(bot_name: str) -> Callable[[types.Message, str | list[str], bool], bool]
cle(text: str)
cut_it(text: str, off=14, fill_with_symbol: str = ".")
vice_versa_of_01(int_0_or_1: int | str) -> int
```

> https://github.com/JuicyBotsTelegram/TelebotUtils/blob/bcf52394bb1bc645937ac301bb76cbeb8867ee9d/JTelebotUtils/Utils/__init__.py#L9-L51
