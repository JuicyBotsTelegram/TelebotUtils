# Licence ([Source](https://choosealicense.com/no-permission/))
This project **has no licence** so you have no permission from the creators of the software to use, modify, or share the software. Although a code host such as GitHub may allow you to view and fork the code, this does not imply that you are permitted to use, modify, or share the software for any purpose.

Your options:

- **Ask the maintainers nicely to add a license.** Unless the software includes strong indications to the contrary, lack of a license is probably an oversight. If the software is hosted on a site like GitHub, open an issue requesting a license and include a link to this site. If you’re bold and it’s fairly obvious what license is most appropriate, open a pull request to add a license – see “suggest this license” in the sidebar of the page for each license on this site (e.g., MIT).
- **Don’t use the software.** Find or create an alternative that is under an open source license.
- **Negotiate a private license.** Bring your lawyer.



# TelebotUtils

#### TelebotUtils is a Python module which contains all the needed and related to Telebot library util-functions. As a rule they are for internal JuicyBotsTelegram projects

### 👉 How to install TelebotUtils module
Run `pip3.X install git+https://github.com/JuicyBotsTelegram/TelebotUtils`


## Code Overview

### Utils Classes
> #### AnnotatedString helps to collect the strings and transform them via given markdown (HTML or markdown)
> https://github.com/JuicyBotsTelegram/TelebotUtils/blob/7a61e084b11ae19919d2d1b1c00975db8ffbe280/JTelebotUtils/TGTypes.py#L81-L111

### Extension functions for `telebot.types.Callback`:

> ```python
> isCallDataStartsWith(call: telebot.types.CallbackQuery, template: str) -> bool: 
> ```
>
> https://github.com/JuicyBotsTelegram/TelebotUtils/blob/bcf52394bb1bc645937ac301bb76cbeb8867ee9d/JTelebotUtils/Extensions/TCallExt.py#L4-L5


### Extension functions for `telebot.types.Message`:

> ```python
> isFromGroupOrPrivate(msg: telebot.types.Message) -> bool
> isFromGroup(msg: telebot.types.Message) -> bool
> isFromPrivate(msg: telebot.types.Message) -> bool
> isFromChannel(msg: telebot.types.Message) -> bool
> isMsgTextStartsWith(msg: telebot.types.Message, template) -> bool
> getCommandFromMsg(msg: telebot.types.Message) -> str
> ```
> 
> https://github.com/JuicyBotsTelegram/TelebotUtils/blob/bcf52394bb1bc645937ac301bb76cbeb8867ee9d/JTelebotUtils/Extensions/TMsgExt.py#L10-L39


### Extension function to `telebot.types.User`:

> ```python
> makeFullName(first_name: str, last_name: str | None, user_name: str | None) -> str
> makeFullNameTG(u: telebot.types.User) -> str
> makeName(first_name: str, last_name: str | None) -> str
> makeNameTG(u: telebot.types.User) -> str
> ```
> 
> https://github.com/JuicyBotsTelegram/TelebotUtils/blob/bcf52394bb1bc645937ac301bb76cbeb8867ee9d/JTelebotUtils/Extensions/TUserExt.py#L8-L24

## Utils functions

> ```python
> generateComparatorToCheckIfUserIsAdmin(admin_ids: list[int]) -> Callable[[types.Message], bool]
> isTextCommand(bot_name: str) -> Callable[[types.Message, str | list[str], bool], bool]
> cle(text: str)
> cut_it(text: str, off=14, fill_with_symbol: str = ".")
> vice_versa_of_01(int_0_or_1: int | str) -> int
> ```
> 
> https://github.com/JuicyBotsTelegram/TelebotUtils/blob/bcf52394bb1bc645937ac301bb76cbeb8867ee9d/JTelebotUtils/Utils/__init__.py#L9-L51
