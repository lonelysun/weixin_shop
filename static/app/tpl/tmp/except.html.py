# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1434852224.816
_enable_loop = True
_template_filename = 'D:\\pywork\\odoo-0504\\born\\born_weixin_shop\\static\\defaultApp/views/except.html'
_template_uri = 'except.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\r\n<head></head>\r\n<body>\r\n<div>\r\n\r\n<h1>NOT FOUND</h1>\r\n</div>\r\n\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


