# -*- coding: utf-8 -*-
##############################################################################
#  COMPANY: BORN
#  AUTHOR: KIWI
#  EMAIL: arborous@gmail.com
#  VERSION : 1.0   NEW  2014/07/21
#  UPDATE : NONE
#  Copyright (C) 2011-2014 www.wevip.com All Rights Reserved
##############################################################################

import os
import time
import json
import logging
import random
import string
import datetime
import simplejson
import werkzeug.utils
from mako import exceptions
from openerp.http import request
from openerp import SUPERUSER_ID
from openerp.addons.web import http
from mako.lookup import TemplateLookup
from lxml import etree
from openerp.addons.born_weixin_shop.models import util
from mako.template import Template

_logger = logging.getLogger(__name__)


class WeixinShopMod(http.Controller):


    def _check(self):
        return True

    #获取头部展示图片
    @http.route('/<string:db>/<string:cid>/wxshop_get_carousel',type='http', auth="none", csrf=False)
    def getCarousel(self, db=None,cid=None, **post):

        if not db or not cid:
            return json.dumps({'errcode': 1, 'errmsg': u'参数错误', 'data': {}})

        request.session.db = db
        position=post.get('position','mobile_top')
        domain=[('company_id','=',int(cid)),('type','=','carousel'),('position', '=',position)]

        carousel_obj = request.env['born.carousel']
        carousels = carousel_obj.sudo().search(domain, limit=1)

        items=[]
        result={}
        for carousel in carousels:
            for item in carousel.item_ids:
                val={
                     'image_url':item.image_url,
                     'title':item.title or '',
                     'link_url':item.link_url,
                }
                items.append(val)
            result={
                'interval':carousel.interval,
                'items':items,
            }

        print result
        return json.dumps({'errcode': 0, 'errmsg': '111', 'data': result})

    # 获取联系我们信息
    @http.route('/<string:db>/<string:cid>/wxshop_get_contact', type='http', auth="none", csrf=False)
    def getContact(self, db=None, cid=None, **post):

        if not db or not cid:
            return json.dumps({'errcode': 1, 'errmsg': u'参数错误', 'data': {}})

        request.session.db = db
        company_obj = request.env['res.company']
        company = company_obj.sudo().browse(int(cid))
        if not company:
            return json.dumps({'errcode': 1, 'errmsg': u'参数错误', 'data': {}})
        data={
            'company_name':company.name  or '',
            'company_phone': company.phone  or '',
            'company_address': company.contact_address  or '',
            'brand':company.brand  or '',
            'note': company.note or '',
        }
        return json.dumps({'errcode': 0, 'errmsg': '', 'data': data})



    #获取导航栏
    @http.route('/<string:db>/<string:cid>/wxshop_get_nav',type='http', auth="none", csrf=False)
    def getNav(self, db=None, **post):

        request.session.db = db
        position=post.get('position','mobile_top')
        domain=[('type','=','function_ids')]
        # domain += [('position', '=',position)]

        model_obj = request.env['born.shop.model']
        models = model_obj.sudo().search(domain, limit=1)
        print(models)
        items=[]
        result={}
        for model in models:
            for item in model.category_ids:
                val={
                    'image_url':item.image_url,
                    'name':item.name,
                    'sequence':item.sequence,
                    'link_url':'',
                }
                items.append(val)
            result={
                'items':items,
            }
        print result
        return json.dumps(result)