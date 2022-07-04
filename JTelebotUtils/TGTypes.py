from __future__ import annotations

from abc import ABC
from typing import Optional


class TGFormats(ABC):
    MODE_MARKDOWN = 'markdown'
    MODE_HTML = 'html'

    def __init__(self, text: str):
        self._raw_text = text
        self._tagged_text = text

    @property
    def tagged_text(self):
        return self._tagged_text

    @property
    def raw_text(self):
        return self._raw_text

    def _set_tagged_text(self, tagged_text: str) -> TGFormats:
        self._tagged_text = tagged_text
        return self

    @property
    def mode(self) -> str: raise NotImplementedError()

    def _custom_tag(self, tag, text): raise NotImplementedError()
    def b(self): raise NotImplementedError()  # bold
    def strong(self): raise NotImplementedError()  # strong
    def i(self): raise NotImplementedError()  # italic
    def em(self): raise NotImplementedError()  # emphasized
    def code(self): raise NotImplementedError()  # code
    def s(self): raise NotImplementedError()  # strike
    def strike(self): raise NotImplementedError()  # strike
    def del_(self): raise NotImplementedError()  # delete
    def u(self): raise NotImplementedError()  # underlined
    def pre(self): raise NotImplementedError()  # preformat
    def url(self, url=None): raise NotImplementedError()  # url
    def url_mention(self, user_id): raise NotImplementedError()  # url_mention


class HTML(TGFormats):
    @property
    def mode(self) -> str: return self.MODE_HTML
    def _custom_tag(self, tag, text): return self._set_tagged_text(f"<{tag}>{text}</{tag}>")
    def b(self): return self._custom_tag("b", self.raw_text)
    def strong(self): return self._custom_tag("strong", self.raw_text)
    def i(self): return self._custom_tag("i", self.raw_text)
    def em(self): return self._custom_tag("em", self.raw_text)
    def code(self): return self._custom_tag("code", self.raw_text)
    def s(self): return self._custom_tag("s", self.raw_text)
    def strike(self): return self._custom_tag("strike", self.raw_text)
    def del_(self): return self._custom_tag("del", self.raw_text)
    def u(self): return self._custom_tag("u", self.raw_text)
    def pre(self): return self._custom_tag("pre", self.raw_text)
    def url(self, url=None): return self._set_tagged_text(f'<a href="{url}">{self.raw_text}</a>' if url else self.raw_text)
    def url_mention(self, user_id): return self.url(f"tg://user?id={user_id}")


class MDown(TGFormats):
    @property
    def mode(self) -> str: return self.MODE_MARKDOWN
    def _custom_tag(self, tag, text) -> MDown: return self._set_tagged_text(f"{tag}{text}{tag}")
    def b(self): return self._custom_tag("**", self.raw_text)
    def strong(self): return self._custom_tag("**", self.raw_text)
    def i(self): return self._custom_tag("_", self.raw_text)
    def em(self): return self._custom_tag("_", self.raw_text)
    def code(self): return self._custom_tag("`", self.raw_text)
    def s(self): return self._custom_tag("~~", self.raw_text)
    def strike(self): return self._custom_tag("~~", self.raw_text)
    def del_(self): return self._custom_tag("~~", self.raw_text)
    def u(self): return self
    def pre(self): return self._custom_tag("```", self.raw_text)
    def url(self, url=None): return self._set_tagged_text(f"[{self.raw_text}]({url})" if url else self.raw_text)
    def url_mention(self, user_id): return self.url(f"tg://user?id={user_id}")


class AnnotatedString:
    def __init__(self):
        self._parts: list[str | HTML | MDown] = list()
        self._first_found_tg_format_mode: Optional[str] = None

    @property
    def mode(self) -> Optional[str]:
        return self._first_found_tg_format_mode

    def clear_and_add(self, some_str: str | HTML | MDown) -> AnnotatedString:
        self._parts.clear()
        self._first_found_tg_format_mode = None
        return self.add(some_str)

    def add(self, some_str: str | HTML | MDown) -> AnnotatedString:
        if isinstance(some_str, (HTML, MDown)):
            if self._first_found_tg_format_mode is None:
                self._first_found_tg_format_mode = some_str.mode
            else:
                if self._first_found_tg_format_mode != some_str.mode:
                    raise ValueError(f"Cannot store different markdowns, {self._first_found_tg_format_mode} is used")
        self._parts.append(some_str)
        return self

    @property
    def raw_text(self) -> str:
        return "".join(part.raw_text if isinstance(part, TGFormats) else part for part in self._parts)

    @property
    def transformed(self) -> str:
        return "".join(part.tagged_text if isinstance(part, TGFormats) else part for part in self._parts)
