
class TGFormats(str):
    MODE_MARKDOWN = 'markdown'
    MODE_HTML = 'html'
    @classmethod
    def _custom_tag(cls, tag, text): raise NotImplementedError()
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
    @classmethod
    def _custom_tag(cls, tag, text): return f"<{tag}>{text}</{tag}>"
    def b(self): return self._custom_tag("b", self)
    def strong(self): return self._custom_tag("strong", self)
    def i(self): return self._custom_tag("i", self)
    def em(self): return self._custom_tag("em", self)
    def code(self): return self._custom_tag("code", self)
    def s(self): return self._custom_tag("s", self)
    def strike(self): return self._custom_tag("strike", self)
    def del_(self): return self._custom_tag("del", self)
    def u(self): return self._custom_tag("u", self)
    def pre(self): return self._custom_tag("pre", self)
    def url(self, url=None): return f'<a href="{url}">{self}</a>' if url else self
    def url_mention(self, user_id): return self.url(f"tg://user?id={user_id}")


class MDown(TGFormats):
    @classmethod
    def _custom_tag(cls, tag, text): return f"{tag}{text}{tag}"
    def b(self): return self._custom_tag("**", self)
    def strong(self): return self._custom_tag("**", self)
    def i(self): return self._custom_tag("_", self)
    def em(self): return self._custom_tag("_", self)
    def code(self): return self._custom_tag("`", self)
    def s(self): return self._custom_tag("~~", self)
    def strike(self): return self._custom_tag("~~", self)
    def del_(self): return self._custom_tag("~~", self)
    def u(self): return self
    def pre(self): return self._custom_tag("```", self)
    def url(self, url=None): return f"[{self}]({url})" if url else self
    def url_mention(self, user_id): return self.url(f"tg://user?id={user_id}")
