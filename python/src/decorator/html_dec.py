def fmakeHtmlTag(tag, *args, **kwds):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwds["css_class"]) \
                                     if "css_class" in kwds else ""
        def wrapped(*args, **kwds):
            return "<"+tag+css_class+">\n" \
                   + fn(*args, **kwds) + "\n</"+tag+">"
        return wrapped
    return real_decorator

@fmakeHtmlTag(tag="b", css_class="bold_css")
@fmakeHtmlTag(tag="i", css_class="italic_css")
def hello():
    return "hello world"

print(hello())

# 你觉得上面那个带参数的Decorator的函数嵌套太多了
# class式的 Decorator

class makeHtmlTagClass(object):

    def __init__(self, tag, css_class=""):
        self._tag = tag
        self._css_class = " class='{0}'".format(css_class) \
                                       if css_class !="" else ""

    def __call__(self, fn):
        def wrapped(*args, **kwargs):
            return "<" + self._tag + self._css_class+">\n"  \
                       + fn(*args, **kwargs) + "\n</" + self._tag + ">"
        return wrapped

@makeHtmlTagClass(tag="b", css_class="bold_css")
@makeHtmlTagClass(tag="i", css_class="italic_css")
def hello(name):
    return "Hello, {}".format(name)

print(hello("Hao Chen"))