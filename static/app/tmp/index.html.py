# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463993948.484
_enable_loop = True
_template_filename = 'D:\\pywork\\odoo-9.0\\liuhao\\born_weixin_shop\\static\\app/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html >\n<head>\n    <title>\u5fae\u4fe1\u5546\u57ce</title>\n    <meta http-equiv="X-UA-Compatible" content="IE=edge" />\n    <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=0" />\n    <link href="/born_weixin_shop/static/src/css/font-awesome.min.css" rel="stylesheet" />\n    <link href="/born_weixin_shop/static/src/css/bootstrap.min.css" rel="stylesheet" />\n    <link href="/born_weixin_shop/static/src/css/weui.min.css" rel="stylesheet"/>\n    <link href="/born_weixin_shop/static/src/css/styles.css" rel="stylesheet" />\n    <link href="/born_weixin_shop/static/src/css/owl.carousel.css" rel="stylesheet" />\n\n</head>\n<body ontouchstart ng-app="shopApp" ng-cloak>\n\n    <div ng-view style="position:relative;" id="ng-view" ></div>\n\n    <div class=" navbar navbar-fixed-bottom bg-light lt b-t ng-scope" ui-view="footer" >\n\t\t<div class="row ng-scope" >\n\t\t    <nav>\n\t\t         <div class="footermenu" data-collapse="isCollapsed" >\n\t\t             <ul>\n\t\t                 <li> <a href="#/products"><i class="fa fa-home"></i><p>\u9996\u9875</p></a>  </li>\n\t\t                 <li> <a href="#/category"><i class="fa fa-tasks"></i><p>\u5206\u7c7b</p></a> </li>\n\t\t                 <li> <a href="#/cart" > <i class="fa fa-shopping-cart"></i><p>\u8d2d\u7269\u8f66</p></a> </li>\n\t\t                 <li> <a href="#/user"><i class="fa fa-user"></i><p>\u6211\u7684</p></a>  </li>\n\t\t             </ul>\n\t\t         </div>\n\t\t     </nav>\n\t\t</div>\n\t</div>\n\n    <!-- libraries -->\n    <script src="/born_weixin_shop/static/src/js/jweixin-1.0.0.js"></script>\n    <script src="/born_weixin_shop/static/src/js/jquery.js"></script>\n    <script src="/born_weixin_shop/static/src/js/angular.min1.3.js"></script>\n    <script src="/born_weixin_shop/static/src/js/angular-route1.3.min.js"></script>\n    <script src="/born_weixin_shop/static/src/js/ui-bootstrap-tpls-0.13.0.min.js"></script>\n    <script src="/born_weixin_shop/static/src/js/sanitize.js"></script>\n    <script src="/born_weixin_shop/static/src/js/angular-touch.js"></script>\n    <script src="/born_weixin_shop/static/src/js/owl.carousel.js"></script>\n    <script src="/born_weixin_shop/static/app/app.js"></script>\n    <script src="/born_weixin_shop/static/app/service/config.js"></script>\n    <script src="/born_weixin_shop/static/app/service/service.data.js"></script>\n    <script src="/born_weixin_shop/static/app/service/service.shop.js"></script>\n    <script src="/born_weixin_shop/static/app/controller/controller.carousel.js"></script>\n    <script src="/born_weixin_shop/static/app/controller/controller.home.js"></script>\n</body>\n</html>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"26": 20, "20": 1, "15": 0}, "uri": "index.html", "filename": "D:\\pywork\\odoo-9.0\\liuhao\\born_weixin_shop\\static\\app/index.html"}
__M_END_METADATA
"""
