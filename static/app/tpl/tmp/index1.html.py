# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1435149925.152
_enable_loop = True
_template_filename = 'D:\\pywork\\odoo-0504\\born\\born_weixin_shop\\static\\defaultApp/views/index1.html'
_template_uri = 'index1.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        company = context.get('company', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html>\n<html ng-app="shopApp">\n<head>\n    <title>')
        # SOURCE LINE 4
        __M_writer(unicode(company.name))
        __M_writer(u'</title>\n    <meta http-equiv="X-UA-Compatible" content="IE=edge" />\n    <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=0" />\n    \n    \n    <link href="/born_weixin_shop/static/src/css/bootstrap.css" rel="stylesheet" />\n    <link href="/born_weixin_shop/static/src/css/bootstrap-theme.min.css" rel="stylesheet" />\n    <link href="/born_weixin_shop/static/src/css/animations.css" rel="stylesheet" />\n    <link href="/born_weixin_shop/static/src/css/styles.css" rel="stylesheet" />\n    <link href="/born_weixin_shop/static/src/css/picture.css" rel="stylesheet" />\n    \n    <script src="http://res.wx.qq.com/open/js/jweixin-1.0.0.js"></script>\n    \n</head>\n<body ng-cloak>\n\t <nav class="container1">\n         <div class="footermenu" data-collapse="isCollapsed" ng-controller="NavbarController as vm">\n             <ul menu-highlighter highlight-class-name="active">\n                 <li><a href="#/products"><img src="/born_weixin_shop/static/src/img/home.png"><p>\u9996\u9875</p></a></li>\n                 <li><a href="#/cart" >\n\t\t          \t<img src="/born_weixin_shop/static/src/img/i_cart.png">\n\t\t          \t<p>\u8d2d\u7269\u8f66</p>\n\t\t          </a></li>\n                 <li><a href="#/user">\n          \t<img src="/born_weixin_shop/static/src/img/i_me.png">\n          \t<p>\u6211\u7684</p>\n          </a></li>\n             </ul>\n         </div>\n     </nav>\n    <div style="margin-bottom:50px;">\n        <div ng-view id="ng-view" ></div>\n    </div>\n\t\n    <!-- 3rd party libraries -->\n    <script src="/born_weixin_shop/static/src/js/angular.min1.3.js"></script>\n    <script src="/born_weixin_shop/static/src/js/angular-route1.3.min.js"></script>\n    <script src="/born_weixin_shop/static/src/js/angular-animate1.3.min.js"></script>\n    <script src="/born_weixin_shop/static/src/js/ui-bootstrap-tpls-0.13.0.min.js"></script>\n    <script src="/born_weixin_shop/static/src/js/tweenMax.min.js"></script>\n    <script src="/born_weixin_shop/static/src/js/breeze.min.js"></script>\n    <script src="/born_weixin_shop/static/src/js/breeze.angular.js"></script>\n    <script src="/born_weixin_shop/static/src/js/sanitize.js"></script>\n    \n    <script src="born_weixin_shop/static/defaultApp/wc.directives/directives/wcOverlay.js"></script>\n    <script src="born_weixin_shop/static/defaultApp/wc.directives/directives/menuHighlighter.js"></script>\n    <script src="born_weixin_shop/static/defaultApp/app.js"></script>\n    <script src="born_weixin_shop/static/defaultApp/animations/listAnimations.js"></script>\n    <script src="born_weixin_shop/static/defaultApp/directives/wcUnique.js"></script>\n    <script src="born_weixin_shop/static/defaultApp/services/config.js"></script>\n    <script src="born_weixin_shop/static/defaultApp/services/authService.js"></script>\n    <script src="born_weixin_shop/static/defaultApp/services/httpInterceptors.js"></script>\n    <script src="born_weixin_shop/static/defaultApp/services/dataService.js"></script>\n    <script src="born_weixin_shop/static/defaultApp/services/modalService.js"></script>\n    <script src="born_weixin_shop/static/defaultApp/services/productsService.js"></script>\n    \n    <script src="born_weixin_shop/static/defaultApp/controllers/products/productController.js"></script>\n    <script src="born_weixin_shop/static/defaultApp/controllers/products/prodctDetailController.js"></script>\n  \t<script src="born_weixin_shop/static/defaultApp/controllers/navbarController.js"></script>\n  \t<script src="born_weixin_shop/static/defaultApp/controllers/carouselController.js"></script>\n  \t<script src="born_weixin_shop/static/defaultApp/controllers/cart/cartController.js"></script>\n  \t<script src="born_weixin_shop/static/defaultApp/controllers/cart/checkoutController.js"></script>\n  \t<script src="born_weixin_shop/static/defaultApp/controllers/user/userController.js"></script>\n</body>\n</html>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


