# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463458130.463689
_enable_loop = True
_template_filename = '/opt/odoo-dianshang/born/born_weixin_shop/static/app/views/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html ng-app="shopApp">\n<head>\n    <title>\u5fae\u4fe1\u5546\u57ce</title>\n    <meta http-equiv="X-UA-Compatible" content="IE=edge" />\n    <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=0" />\n    <link href="/born_weixin_shop/static/src/css/styles.css" rel="stylesheet" />\n\n</head>\n<body ng-cloak>\n\t\n\t<!-- content -->\n    <div ng-view id="ng-view" ></div>\n\n    \n    <!-- 3rd party libraries -->\n    <script src="/born_weixin_shop/static/src/js/jweixin-1.0.0.js"></script>\n    <script src="/born_weixin_shop/static/src/js/angular.min1.3.js"></script>\n    <script src="/born_weixin_shop/static/src/js/angular-route1.3.min.js"></script>\n    <script src="/born_weixin_shop/static/src/js/sanitize.js"></script>\n\n    <script src="born_weixin_shop/static/app/app.js"></script>\n\n    <script src="born_weixin_shop/static/app/service/config.js"></script>\n    <script src="born_weixin_shop/static/app/service/service.data.js"></script>\n    <script src="born_weixin_shop/static/app/service/service.shop.js"></script>\n\n    <script src="born_weixin_shop/static/app/controller/controller.index.js"></script>\n\n</body>\n</html>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"26": 20, "20": 1, "15": 0}, "uri": "index.html", "filename": "/opt/odoo-dianshang/born/born_weixin_shop/static/app/views/index.html"}
__M_END_METADATA
"""
