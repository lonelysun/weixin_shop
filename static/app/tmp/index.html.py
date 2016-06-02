# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1464254476.232
_enable_loop = True
_template_filename = 'D:\\pywork\\odoo-9.0\\liuhao\\born_weixin_shop\\static\\app/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\r\n<html lang="en" data-ng-app="app" ng-controller="AppCtrl">\r\n<head>\r\n  <meta charset="utf-8" />\r\n  <title>{{app.title}}</title>\r\n  <meta name="description" content="Angularjs, Html5, Music, Landing, 4 in 1 ui kits package" />\r\n  <meta name="keywords" content="AngularJS, angular, bootstrap, admin, dashboard, panel, app, charts, components,flat, responsive, layout, kit, ui, route, web, app, widgets" />\r\n  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />\r\n  <link rel="stylesheet" href="/born_weixin_shop/static/libs/jquery/bootstrap/dist/css/bootstrap.css" type="text/css" />\r\n  <link rel="stylesheet" href="/born_weixin_shop/static/libs/assets/font-awesome/css/font-awesome.min.css" type="text/css" />\r\n    <link rel="stylesheet" href="/born_weixin_shop/static/app/css/app.css" type="text/css" />\r\n</head>\r\n<body >\r\n\r\n  <div  id="app" class="app app-header-fixed  "  ui-view></div>\r\n\r\n  <script src="/born_weixin_shop/static/libs/jquery/jquery/dist/jquery.js"></script>\r\n  <script src="/born_weixin_shop/static/libs/angular/angular/angular.js"></script>\r\n  <script src="/born_weixin_shop/static/libs/angular/angular-animate/angular-animate.js"></script>\r\n  <script src="/born_weixin_shop/static/libs/angular/angular-cookies/angular-cookies.js"></script>\r\n  <script src="/born_weixin_shop/static/libs/angular/angular-messages/angular-messages.js"></script>\r\n  <script src="/born_weixin_shop/static/libs/angular/angular-resource/angular-resource.js"></script>\r\n  <script src="/born_weixin_shop/static/libs/angular/angular-sanitize/angular-sanitize.js"></script>\r\n  <script src="/born_weixin_shop/static/libs/angular/angular-touch/angular-touch.js"></script>\r\n  <script src="/born_weixin_shop/static/libs/angular/angular-ui-router/release/angular-ui-router.js"></script>\r\n  <script src="/born_weixin_shop/static/libs/angular/ngstorage/ngStorage.js"></script>\r\n  <script src="/born_weixin_shop/static/libs/angular/angular-bootstrap/ui-bootstrap-tpls.js"></script>\r\n  <script src="/born_weixin_shop/static/libs/angular/oclazyload/dist/ocLazyLoad.js"></script>\r\n  <script src="/born_weixin_shop/static/app/js/app.js"></script>\r\n  <script src="/born_weixin_shop/static/app/js/config.js"></script>\r\n  <script src="/born_weixin_shop/static/app/js/config.lazyload.js"></script>\r\n  <script src="/born_weixin_shop/static/app/js/config.router.js"></script>\r\n  <script src="/born_weixin_shop/static/app/js/services/service.shop.js"></script>\r\n  <script src="/born_weixin_shop/static/app/js/services/ui-load.js"></script>\r\n  <script src="/born_weixin_shop/static/app/js/main.js"></script>\r\n  <!--\r\n  <script src="/born_weixin_shop/static/app/js/app.min.js"></script>\r\n    -->\r\n\r\n\r\n  <script src="/born_weixin_shop/static/app/js/directives/mod.directive.js"></script>\r\n\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"26": 20, "20": 1, "15": 0}, "uri": "index.html", "filename": "D:\\pywork\\odoo-9.0\\liuhao\\born_weixin_shop\\static\\app/index.html"}
__M_END_METADATA
"""
