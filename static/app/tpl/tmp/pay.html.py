# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1434440634.12
_enable_loop = True
_template_filename = 'D:\\pywork\\odoo-0504\\born\\cart\\static\\defaultApp/views/pay.html'
_template_uri = 'pay.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        acquirers = context.get('acquirers', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\r\n\r\n<head>\r\n</head>\r\n\r\n\r\n<body>\r\n\r\n\t<div>\r\n\t\t<ul>\r\n')
        # SOURCE LINE 11
        for acquirer in acquirers:
            # SOURCE LINE 12
            __M_writer(u'       \t\t<li>\r\n       \t\t\r\n       \t\t <input value="')
            # SOURCE LINE 14
            __M_writer(unicode(acquirer.id))
            __M_writer(u'" type="radio" name="acquirer" />\r\n       \t\t<img class="media-object" style="width: 60px; display: inline-block;"\r\n                             title="')
            # SOURCE LINE 16
            __M_writer(unicode(acquirer.name))
            __M_writer(u'"\r\n                              src="/payment_')
            # SOURCE LINE 17
            __M_writer(unicode(acquirer.provider))
            __M_writer(u'/static/src/img/')
            __M_writer(unicode(acquirer.provider))
            __M_writer(u'_icon.png"/>\r\n                              <span>')
            # SOURCE LINE 18
            __M_writer(unicode(acquirer.name))
            __M_writer(u'</span>\r\n       \t\t</li>\r\n')
        # SOURCE LINE 21
        __M_writer(u'    \t</ul>\r\n\t</div>\r\n\t\r\n\r\n')
        # SOURCE LINE 25
        for acquirer in acquirers:
            # SOURCE LINE 26
            __M_writer(u'       \t\t<div id="')
            __M_writer(unicode(acquirer.id))
            __M_writer(u'" class="oe_sale_acquirer_button hidden pull-right">\r\n                        <div>\r\n                        ')
            # SOURCE LINE 28
            __M_writer(unicode(acquirer.button))
            __M_writer(u'\r\n                        </div>\r\n                        <div>\r\n                        ')
            # SOURCE LINE 31
            __M_writer(unicode(acquirer.pre_msg))
            __M_writer(u'\r\n                        </div>\r\n                        </div>\r\n')
        # SOURCE LINE 35
        __M_writer(u'   \r\n\t\r\n\t\r\n\t <t t-foreach="acquirers or []" t-as="acquirer">\r\n                      <div t-att-data-id="acquirer.id" class="oe_sale_acquirer_button hidden pull-right">\r\n                        <div t-raw="acquirer.button"/>\r\n                        <div t-field="acquirer.pre_msg"/>\r\n                      </div>\r\n                  </t>\r\n\t\r\n\t\r\n          \r\n\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


