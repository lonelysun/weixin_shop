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

#MAKO
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEFAULT_THEME="app"
path = os.path.join(BASE_DIR, "static", DEFAULT_THEME)
base_lottery_path =  os.path.join(BASE_DIR, "static", "lottery")
tmp_path = os.path.join(path, "tmp")
lookup = TemplateLookup(directories=[path],output_encoding='utf-8',module_directory=tmp_path)
_logger = logging.getLogger(__name__)


class WeixinShop(http.Controller):

    @http.route(['/<string:db>/<string:cid>/wxshop'],  type='http', auth="none", csrf=False)
    def wxshop(self,db=None, cid=None,**post):
        request.session.db = db
        template = lookup.get_template('index.html')
        return template.render()



    #获取产品信息
    @http.route('/wxshop/products',  type='http', auth="none", csrf=False)
    def products(self, **post):
        data=[]

        category_id=post.get('category_id',0)
        domain=[('available_in_weixin','=',True)]
        if int(category_id)>0:
            domain += [('pos_categ_id', '=',int(category_id))]

        search_type=post.get('type',False)
        if search_type=='follow':
            follow_obj = request.registry.get('born.follow.product')
            follow_ids = follow_obj.search_read(request.cr, SUPERUSER_ID, [('openid','=',request.session.openid)], ['product_id'], context=request.context)
            p_ids=[x['product_id'] for x in follow_ids]
            domain+=[('id','in',p_ids)]

        product_obj = request.registry.get('product.product')
        product_ids = product_obj.search(request.cr, SUPERUSER_ID, domain, context=request.context)
        products=list(product_obj.browse(request.cr, SUPERUSER_ID,product_ids, context=request.context))
        for product in products:
            val={
                 'name':product.name,
                 'image_medium':product.image_medium,
                 'id':product.id,
                 'description':product.description  or '',
                 'lst_price':product.lst_price,
                 'sales_count':product.sales_count,
                 'time':product.time,
                 'pos_categ_id':product.pos_categ_id.id or '',
                 'pos_categ_name':product.pos_categ_id.name or '',
            }
            data.append(val)
        return json.dumps(data,sort_keys=True)

    #获取分类信息
    @http.route('/wxshop/category',  type='http', auth="none", csrf=False)
    def getCategory(self, **post):
        data=[]
        category_obj = request.registry.get('pos.category')
        product_obj = request.registry.get('product.product')
        categorys = list(category_obj.search_read(request.cr, SUPERUSER_ID, [('available_in_weixin','=',True)], ['id','name','image_medium','child_id','parent_id'], context=request.context))
        for category in categorys:
            count= product_obj.search_count(request.cr, SUPERUSER_ID, [('pos_categ_id','=',category['id']),
                                                                       ('is_on_shelve','=',True)], context=request.context)
            val={
                'name':category['name'],
                'id':category['id'],
                'image_medium':category['image_medium'],
                'child_id':category['child_id'],
                'parent_id':category['parent_id'],
                'count':count,
            }
            data.append(val)

        print categorys
        return json.dumps(data,sort_keys=True)


    #获取用户详细信息
    @http.route('/wxshop/account',  type='http', auth="none", csrf=False)
    def getAccount(self, **post):
        data={}

        if not request.session.openid :
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        domain=[('openid','=',request.session.openid)]
        obj_users = request.registry['born.weixin.users']

        user_ids = obj_users.search(request.cr, SUPERUSER_ID, domain, context=request.context)
        users=list(obj_users.browse(request.cr, SUPERUSER_ID,user_ids, context=request.context))
        for user in users:
            data={
                'id':user['id'],
                'nickname':user['nickname'],
                'realname':user['realname'] and user['realname'] or '',
                'mail':user['mail'] and user['mail'] or '',
                'phone':user['phone'] and user['phone'] or '',
            }
        return json.dumps(data,sort_keys=True)


    #获取收货地址列表
    @http.route('/wxshop/address',  type='http', auth="none", csrf=False)
    def getAddress(self, **post):
        data=[]

        return json.dumps(data,sort_keys=True)

    @http.route('/wxshop/saveAccount/<int:user_id>',  type='http', auth="none", csrf=False,methods=['POST'])
    def saveAccount(self, user_id,**post):

        _logger.info(post)
        if not request.session.openid :
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        obj_users = request.registry['born.weixin.users']
        user=obj_users.browse(request.cr, SUPERUSER_ID,user_id, context=request.context)

        user.realname=post.get('realname',False)
        user.mail=post.get('mail',False)
        user.phone=post.get('phone',False)
        user.write({'realname':user.realname,'mail':user.mail,'phone':user.phone})
        data={
            'id':user.id,
            'nickname':user.nickname,
            'realname':user.realname and user.realname or '',
            'mail':user.mail and user.mail or '',
            'phone':user.phone and user.phone or '',
        }
        return json.dumps(data,sort_keys=True)

    #获取产品详细信息
    @http.route('/wxshop/product/<int:product_id>',  type='http', auth="none", csrf=False)
    def product(self, product_id, **post):
        data=[]
        product_obj = request.registry.get('product.product')
        for product in product_obj.browse(request.cr, SUPERUSER_ID,product_id, context=request.context):
            images=[]
            for image in product.image_ids:
                val={
                    'image':image.image,
                    'name':image.name,
                }
                images.append(val)
            data={
                 'name':product.name,
                 'image_small':product.image_small,
                 'id':product.id,
                 'description':product.description  or '',
                 'lst_price':product.lst_price,
                 'sales_count':product.sales_count,
                 'qty':1,
                 'time':product.time,
                 'pos_categ_id':product.pos_categ_id.id or '',
                 'pos_categ_name':product.pos_categ_id.name or '',
                 'description_shop':product.description_shop  or '',
                 'images':images,
                 'description_notice':product.description_notice,
                 'virtual_available':product.virtual_available,
            }
        return simplejson.dumps(data,sort_keys=True)

    #添加到购物车
    @http.route('/wxshop/addCart',  type='http', auth="none", csrf=False,methods=['POST'])
    def addCart(self, **post):

        product_id=post.get('id',False)
        qty=post.get('qty',1)

        if not request.session.openid or not qty or not product_id:
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        cart_obj = request.registry.get('born.weixin.cart')
        product_ids = cart_obj.search(request.cr, SUPERUSER_ID, [('state','in',['draft','checkout']),('openid','=',request.session.openid),('product_id','=',int(product_id))], context=request.context)
        order_id = product_ids and product_ids[0] or False
        if order_id:
            cart=cart_obj.browse(request.cr, SUPERUSER_ID,order_id, context=request.context)
            cart_obj.write(request.cr, SUPERUSER_ID,order_id,{'qty':cart.qty+1},context=request.context)
        else:
            vals={
                 'openid':request.session.openid,
                 'product_id':product_id,
                 'qty':qty,
            }
            order_id= cart_obj.create(request.cr, SUPERUSER_ID,vals,context=request.context)
        return json.dumps(order_id,sort_keys=True)

    #添加关注
    @http.route('/wxshop/follow',  type='http', auth="none", csrf=False,methods=['POST'])
    def follow(self, **post):

        product_id=post.get('id',False)

        if not request.session.openid or not product_id:
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))
        product_id=int(product_id)
        follow_obj = request.registry.get('born.follow.product')
        product_ids = follow_obj.search(request.cr, SUPERUSER_ID, [('openid','=',request.session.openid),('product_id','=',int(product_id))], context=request.context)
        follow_id = product_ids and product_ids[0] or False
        if not follow_id:
            vals={
                 'openid':request.session.openid,
                 'product_id':product_id,
            }
            follow_id= follow_obj.create(request.cr, SUPERUSER_ID,vals,context=request.context)
        return json.dumps(follow_id,sort_keys=True)

    #修改购买数量
    @http.route('/wxshop/changeQty',  type='http', auth="none", csrf=False,methods=['POST'])
    def changeQty(self, **post):

        item_id=post.get('id',False)
        qty=post.get('qty',False)

        if not request.session.openid or not qty or not item_id:
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        category_obj = request.registry.get('born.weixin.cart')
        vals={
            'qty':qty,
        }
        oder= category_obj.write(request.cr, SUPERUSER_ID,int(item_id),vals,context=request.context)
        return json.dumps(oder,sort_keys=True)

    #删除购物车内产品
    @http.route('/wxshop/deleteItem',  type='http', auth="none", csrf=False,methods=['POST'])
    def deleteCartItem(self, **post):

        if not request.session.openid:
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        item_id=post.get('id',False)
        cart_obj = request.registry.get('born.weixin.cart')
        cart_obj.unlink(request.cr, SUPERUSER_ID,int(item_id),context=request.context)
        return json.dumps(item_id,sort_keys=True)

    #获取购物车内项目
    @http.route('/wxshop/carts',  type='http', auth="none", csrf=False)
    def getCarts(self, **post):
        data=[]

        if not request.session.openid:
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        cart_obj = request.registry.get('born.weixin.cart')
        cart_ids = cart_obj.search(request.cr, SUPERUSER_ID, [('openid','=',request.session.openid),('state','!=','finish')], context=request.context)
        carts=list(cart_obj.browse(request.cr, SUPERUSER_ID,cart_ids, context=request.context))
        for cart in carts:
            val={
                'id':cart.id,
                'product_id':cart.product_id.id ,
                'product_name':cart.product_id.name ,
                'qty':cart.qty,
                'lst_price':cart.product_id.lst_price,
                'image_small':cart.product_id.image_small,
                'description':cart.product_id.description,
                'sub_total':cart.product_id.lst_price*cart.qty,
                'checked':'true',
            }
            data.append(val)
        return json.dumps(data,sort_keys=True)

    #获取购物车内项目
    @http.route('/wxshop/cartsQty',  type='http', auth="none", csrf=False)
    def getCartsQty(self, **post):

        if not request.session.openid:
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        cart_obj = request.registry.get('born.weixin.cart')
        all_order_count= cart_obj.search_count(request.cr, SUPERUSER_ID, [('openid', '=', request.session.openid)], context=request.context)
        return json.dumps(all_order_count,sort_keys=True)

    #去结账生成订单信息
    @http.route('/wxshop/checkout',  type='http', auth="none", csrf=False)
    def checkout(self, **post):

        if not request.session.openid:
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        sale_order_obj = request.registry.get('sale.order')
        users_obj = request.registry.get('born.weixin.users')
        cart_obj = request.registry.get('born.weixin.cart')

        #根据OPENID获取用户的基本信息
        partner_id=False
        users_data = list(users_obj.search_read(request.cr, SUPERUSER_ID, [('openid','=',request.session.openid)], ['id','partner_id','nickname'],limit=1, context=request.context))
        if users_data:
            partner_id = users_data[0]['partner_id'][0]
        else:
            _logger.warning(u'未找到用户的基本信息，用户的openid为%s' % (request.session.openid))
            #partner_id=1
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        #获取购物车订单信息
        cart_ids = cart_obj.search(request.cr, SUPERUSER_ID, [('openid','=',request.session.openid),('state','!=','finish')], context=request.context)
        carts=list(cart_obj.browse(request.cr, SUPERUSER_ID,cart_ids, context=request.context))
        order_line=[]
        for cart in carts:
            line={
                'product_id':cart.product_id.id ,
                'product_uos_qty':cart.qty,
                'product_uom_qty':cart.qty,
            }
            order_line.append((0, False, line))

        order_no = "W"+request.registry.get('ir.sequence').get(request.cr, SUPERUSER_ID, 'sale.order') or '/'

        order_info={
            'origin':False,
            'openid':request.session.openid,
            'message_follower_ids':False,
            'categ_ids':False,
            'order_line':order_line,
            'picking_policy':'direct',
            'order_policy':'manual',
            'campaign_id':False,
            'carrier_id':False,
            'shop_id':False,
            'client_order_ref':u'微信商城订单',
            'partner_id': partner_id,
            'user_id':SUPERUSER_ID,
            'note':u'微信商城订单',
            'pricelist_id':1,
            'warehouse_id':1,
            'sale_category':'weixin',
            'partner_invoice_id': partner_id,
            'name':order_no,
        }

        #生成订单
        order_id=sale_order_obj.create(request.cr, SUPERUSER_ID,order_info,context=request.context)

        #计算是否有抽奖活动信息
        order=sale_order_obj.browse(request.cr, SUPERUSER_ID,order_id, context=request.context)
        spread_obj = request.registry.get('born.spread')
        day = time.strftime("%Y-%m-%d")
        domain=[('start_order_amount','<',order.amount_total)]
        domain += [('start_date', '<=',day)]
        domain += [('end_date', '>=',day)]
        domain += [('product_limit_ids', 'in',[x.product_id.id for x in order.order_line])]
        _logger.info(domain)
        spread_ids = spread_obj.search(request.cr, SUPERUSER_ID, domain, context=request.context)
        if spread_ids:
            spread_id=spread_ids[0]
            _logger.info(spread_id)
            sale_order_obj.write(request.cr, SUPERUSER_ID, order_id,{'spread_id':spread_id})

        #删除购物车内数据
        cart_obj.unlink(request.cr, SUPERUSER_ID,cart_ids,context=request.context)
        return json.dumps(order_id,sort_keys=True)

    #获取客户订单信息
    @http.route('/wxshop/orders',  type='http', auth="none", csrf=False)
    def getOrders(self, **post):
        data=[]

        order_id=post.get('order_id',0)
        state=post.get('state',False)

        if not request.session.openid:
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        domain=[('openid','=',request.session.openid)]

        if int(order_id)>0:
            domain += [('id', '=', int(order_id))]

        domain+=[('is_weixin_unlink','=',False)]
        if state and 'draft'==state:
            domain += [('state', 'in', ('draft','sent','waiting_date'))]
        elif 'payed'==state:
            domain += [('state', 'not in', ('draft','sent','cancel','waiting_date'))]
        elif 'cancel'==state:
            domain += [('state', '=', 'cancel')]

        order_obj = request.registry.get('sale.order')
        order_ids = order_obj.search(request.cr, SUPERUSER_ID, domain, context=request.context)
        orders=list(order_obj.browse(request.cr, SUPERUSER_ID,order_ids, context=request.context))
        for order in orders:
            order_line=[]
            for line in order.order_line:
                item={
                    'product_id':line.product_id.id ,
                    'image_small': line.product_id.image_small,
                    'product_name':line.product_id.name ,
                    'price_unit':line.price_unit ,
                    'price_subtotal':round(line.price_subtotal,2),
                    'product_uom_qty':line.product_uom_qty,
                    'description':line.product_id.description,
                }
                order_line.append(item)

            state_name=''
            state=''
            if order.state=='cancel':
                state='cancel'
                state_name=u'已取消'
            elif order.state in ['draft','sent','waiting_date']:
                state='draft'
                state_name=u'待付款'
            else:
                state='payed'
                state_name=u'已付款'
            if order.is_weixin_unlink:
                state='unlink'
                state_name=u'已删除'
            val={
                'id':order.id,
                'name':order.name,
                'state':state,
                'state_name':state_name,
                'order_line':order_line,
                'amount':order.amount_total,
                'amount_tax':order.amount_tax,
                'transaction_id':order.transaction_id,
                'is_lottery':order.is_lottery,
                'spread_id':order.spread_id.id,
                'spread_name':order.spread_id.name,
                'spread_description':order.spread_id.description,
            }
            data.append(val)
        return json.dumps(data,sort_keys=True)



    #获取奖品信息
    @http.route('/wxshop/coupons',  type='http', auth="none", csrf=False)
    def getCoupons(self,**post):
        data=[]

        order_id=post.get('orderId',0)
        if not request.session.openid:
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        domain=[('openid','=',request.session.openid)]
        if int(order_id)>0:
            domain += [('order_id', '=', int(order_id))]

        obj_result = request.registry['born.lottery.result']
        line_ids = obj_result.search(request.cr, SUPERUSER_ID, domain, context=request.context)
        for line in obj_result.browse(request.cr, SUPERUSER_ID,line_ids, context=request.context):
            val={
               'name':line.spread_id.name,
               'product_name':line.product_id.name,
               'order_name':line.order_id.name,
               'description':line.description,
               'create_date':line.create_date,
            }
            data.append(val)
        return json.dumps(data,sort_keys=True)


    #获取分类信息
    @http.route('/wxshop/categorys',  type='http', auth="none", csrf=False)
    def getCategorys(self, **post):
        data=[]
        category_obj = request.registry.get('pos.category')
        product_obj = request.registry.get('product.product')
        categorys = list(category_obj.search_read(request.cr, SUPERUSER_ID, [('available_in_weixin','=',True)],['id','name','image_medium','child_id','parent_id'], context=request.context))
        for category in categorys:
            product_data=[]
            product_ids = product_obj.search(request.cr, SUPERUSER_ID, [('available_in_weixin','=',True),('pos_categ_id','=',category['id']),('is_on_shelve','=',True)], limit=10,context=request.context)
            products=list(product_obj.browse(request.cr, SUPERUSER_ID,product_ids, context=request.context))
            for product in products:
                product_val={
                     'name':product.name,
                     'image_medium':product.image_medium,
                     'id':product.id,
                     'description':product.description  or '',
                     'lst_price':product.lst_price,
                     'time':product.time,
                     'sales_count':product.sales_count,
                     'pos_categ_id':product.pos_categ_id.id or '',
                     'pos_categ_name':product.pos_categ_id.name or '',
                }
                product_data.append(product_val)
            if product_data:
                val={
                    'name':category['name'],
                    'id':category['id'],
                    'image':category['image_medium'],
                    'child_id':category['child_id'],
                    'parent_id':category['parent_id'],
                    'items':product_data,
                }
                data.append(val)
        return json.dumps(data,sort_keys=True)
    #获取用户购买的产品信息
    @http.route('/wxshop/userProducts',  type='http', auth="none", csrf=False)
    def getUserProducts(self, **post):
        data=[]

        if not request.session.openid:
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        domain=[('openid','=',request.session.openid)]
        domain += [('state', 'not in', ('draft','sent','cancel','waiting_date'))]

        obj_order_line = request.registry['sale.order.line']
        order_obj = request.registry.get('sale.order')
        order_ids = order_obj.search(request.cr, SUPERUSER_ID, domain, context=request.context)

        if order_ids:
            line_ids = obj_order_line.search(request.cr, SUPERUSER_ID, [('order_id','in',order_ids)], context=request.context)
            for line in obj_order_line.browse(request.cr, SUPERUSER_ID,line_ids, context=request.context):
                val={
                   'name':line.product_id.name,
                   'id':line.id,
                   'product_id':line.product_id.id ,
                   'image_small':line.product_id.image_small,
                   'description':line.product_id.description  or '',
                   'description_notice':line.product_id.description_notice,
                   'product_uom_qty':line.product_uom_qty,
                   'price_unit':line.price_unit ,
                   'price_subtotal':round(line.price_subtotal,2),
                   'order_id':line.order_id.id ,
                   'order_name':line.order_id.name ,
                   'buy_date':line.order_id.create_date ,
                   'code':'9999881',
                   'transaction_id':line.order_id.transaction_id
                }
                data.append(val)
        return json.dumps(data,sort_keys=True)

    #获取客户基本资料
    @http.route('/wxshop/profile',  type='http', auth="none", csrf=False)
    def getProfile(self, **post):
        data={}
        if not request.session.openid:
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        obj_users = request.registry['born.weixin.users']
        obj_order = request.registry['sale.order']
        obj_order_line = request.registry['sale.order.line']
        obj_follow = request.registry['born.follow.product']
        obj_history = request.registry['born.browsing.history']

        user_ids = obj_users.search(request.cr, SUPERUSER_ID, [('openid', '=', request.session.openid)], context=request.context)
        if user_ids:

            #用户基本信息
            user = obj_users.browse(request.cr, SUPERUSER_ID,  user_ids[0])
            #获取订单数据
            all_order_count= obj_order.search_count(request.cr, SUPERUSER_ID, [('is_weixin_unlink','=',False),('openid', '=', request.session.openid)], context=request.context)
            draft_order_count= obj_order.search_count(request.cr, SUPERUSER_ID, [('is_weixin_unlink','=',False),('openid', '=', request.session.openid),('state', 'in', ('draft','sent','waiting_date'))], context=request.context)
            cancel_order_count= obj_order.search_count(request.cr, SUPERUSER_ID, [('is_weixin_unlink','=',False),('openid', '=', request.session.openid),('state', '=', 'cancel')], context=request.context)
            payed_order_count= obj_order.search_count(request.cr, SUPERUSER_ID, [('is_weixin_unlink','=',False),('openid', '=', request.session.openid),('state', 'not in', ('draft','sent','cancel','waiting_date'))], context=request.context)
            order_ids = obj_order.search(request.cr, SUPERUSER_ID, [('is_weixin_unlink','=',False),('openid','=',request.session.openid),('state', 'not in', ('draft','sent','cancel','waiting_date'))], context=request.context)
            all_product_count= obj_order_line.search_count(request.cr, SUPERUSER_ID, [('order_id', 'in', order_ids)], context=request.context)
            follow_count= obj_follow.search_count(request.cr, SUPERUSER_ID, [('openid', '=', request.session.openid)], context=request.context)
            browsing_count= obj_history.search_count(request.cr, SUPERUSER_ID, [('openid', '=', request.session.openid)], context=request.context)
            data={
                'nickname':user.nickname,
                'realname':user.realname,
                'phone':user.phone,
                'sex':user.sex,
                'image':user.image,
                'remark':user.remark,
                'all_order_count':all_order_count,
                'draft_order_count':draft_order_count,
                'payed_order_count':payed_order_count,
                'follow_count':follow_count,
                'all_product_count':all_product_count,
                'browsing_count':browsing_count,
                'cancel_order_count':cancel_order_count,
            }

        return json.dumps(data,sort_keys=True)

    #获取订单详细信息
    @http.route('/wxshop/order',  type='http', auth="none", csrf=False)
    def getOrder(self, **post):

        url=post.get('url',False)
        order_id = post.get('order_id',False)

        if not request.session.openid or not order_id:
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        order_line=[]
        order_obj = request.registry.get('sale.order')
        for order in order_obj.browse(request.cr, SUPERUSER_ID,int(order_id), context=request.context):
            for line in order.order_line:
                item={
                    'product_id':line.product_id.id ,
                    'image_small':line.product_id.image_small,
                    'product_name':line.product_id.name ,
                    'price_unit':line.price_unit ,
                    'price_subtotal':line.price_subtotal,
                    'product_uom_qty':line.product_uom_qty,
                    'description':line.product_id.description,
                }
                order_line.append(item)

        obj_account = request.registry['born.weixin.appconnect']
        pv = obj_account.get_jsapi_ticket(request.cr, SUPERUSER_ID, request.session.openid, context=request.context)

        if pv['ticket']=='' :
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        ticket= pv['ticket']
        temp={
          'jsapi_ticket':ticket,
          'url':url,
        }
        ret=self.sign(temp)

        #获取APPID
        appId=''
        payment_obj = request.registry.get('payment.acquirer')
        payment_ids = payment_obj.search_read(request.cr, SUPERUSER_ID, [('provider','=','weixin')], ['weixin_appid'],limit=1, context=request.context)
        if payment_ids:
            appId = payment_ids[0]['weixin_appid']

        state_name=''
        state=''
        if order.state=='cancel':
            state='cancel'
            state_name=u'已取消'
        elif order.state in ['draft','sent','waiting_date']:
            state='draft'
            state_name=u'待付款'
        else:
            state='payed'
            state_name=u'已付款'
        if order.is_weixin_unlink:
            state='unlink'
            state_name=u'已删除'

        order_info={
            'appId':appId,
            'timeStamp':ret['timestamp'],
            'nonceStr':ret['nonceStr'],
            'signature':ret['signature'],
            'amount':order.amount_total,
            'order_no':order.name,
            'amount_tax':order.amount_tax,
            'transaction_id':order.transaction_id,
            'spread_id':order.spread_id.id,
            'order_line':order_line,
            'state_name':state_name,
            'state':state,
        }
        _logger.info(order_info)
        return json.dumps(order_info,sort_keys=True)

    #更改订单信息
    @http.route('/wxshop/updateOrder',  type='http', auth="none", csrf=False)
    def updateOrder(self, **post):
        ret=False

        order_id=post.get('order_id',0)
        state=post.get('state',False)

        if not request.session.openid or int(order_id)<=0:
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        domain=[('openid','=',request.session.openid)]
        domain += [('id', '=', int(order_id))]

        order_obj = request.registry.get('sale.order')
        order_ids = order_obj.search(request.cr, SUPERUSER_ID, domain, context=request.context)
        if order_ids:
            if state in ('cancel','draft'):
                ret=order_obj.write(request.cr, SUPERUSER_ID, int(order_id),{'state':state})
            if state=='unlink':
                ret=order_obj.write(request.cr, SUPERUSER_ID, int(order_id),{'is_weixin_unlink':True})

        return json.dumps(ret,sort_keys=True)

    #获取产品详细信息
    @http.route('/wxshop/payment',  type='http', auth="none", csrf=False)
    def payment(self, **post):

        order_id = post.get('order_id',False)

        if not request.session.openid or not order_id:
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        order_obj = request.registry.get('sale.order')
        order= order_obj.browse(request.cr, SUPERUSER_ID,int(order_id), context=request.context)

        #获取微信支付方式
        payment_obj = request.registry.get('payment.acquirer')
        acquirer_ids = payment_obj.search(request.cr, SUPERUSER_ID, [('provider','=','weixin')], context=request.context)
        acquirers=list(payment_obj.browse(request.cr, SUPERUSER_ID,acquirer_ids, context=request.context))
        tx_values={}
        for acquirer in acquirers:
            partner_values = {}

            model = request.registry.get('payment.acquirer')
            cust_method_name = '%s_form_generate_values' % (acquirer.provider)
            tx_values={
                'body':order.partner_id.name,
                'out_trade_no':order.name,
                'notify_url':'/notify',
                'product_id':order.name,
                'trade_type':'JSAPI',
                'amount':order.amount_total,
                'openid':request.session.openid,
                'appid':'',
                'prepay_id':'',
                'dbname':request.cr.dbname,
            }
            if hasattr(model, cust_method_name):
                method = getattr(model, cust_method_name)
                partner_values, tx_values = method(request.cr, SUPERUSER_ID, acquirer.id, partner_values, tx_values, context=request.context)

        payment={
            'appId':tx_values['appid'],
            'timeStamp':int(time.time()),
            'nonceStr':self.__create_nonce_str(),
            'package':"prepay_id="+tx_values['prepay_id'],
            'signType':'MD5',
        }

        codestr = '&'.join(['%s=%s' % (key, payment[key]) for key in sorted(payment)])
        codestr= codestr+"&key="+tx_values['weixin_key']
        paySign= md5(codestr).hexdigest()
        payment['paySign']=paySign
        payment['prepay_id']=tx_values['prepay_id']
        return simplejson.dumps(payment,sort_keys=True)

    #微信回调接口
    @http.route('/notify', type='http', auth='none', methods=['POST'])
    def weixin_notify(self, **post):

        length = int(request.httprequest.environ['CONTENT_LENGTH'])
        data = request.httprequest.environ['wsgi.input'].read(length)
        json = {}
        for el in etree.fromstring(data):
            json[el.tag] = el.text

        dbname=json.get('attach',False)
        if not dbname:
            _logger.info(u'参数错误没有数据地址')
            return 'FAIL'
        ensure_db(dbname)

        weixin_key=''
        payment_obj = request.registry.get('payment.acquirer')
        payment_ids = payment_obj.search_read(request.cr, SUPERUSER_ID, [('provider','=','weixin')], ['weixin_key'],limit=1, context=request.context)
        if payment_ids:
            weixin_key = payment_ids[0]['weixin_key']

        _, prestr = util.params_filter(json)
        mysign = util.build_mysign(prestr, weixin_key, 'MD5')
        if mysign != json.get('sign'):
            _logger.info(u'签名错误')
            return 'FAIL'

        out_trade_no=json.get('out_trade_no')
        openid=json.get('openid')
        transaction_id=json.get('transaction_id')
        time_end=json.get('time_end')# 支付日期
        payment_date = datetime.datetime.strptime(time_end, "%Y%m%d%H%M%S")
        order_no=out_trade_no.split('_')[0]
        coupon_no=out_trade_no.split('_')[1]

        order_obj = request.registry.get('sale.order')
        domain=[('name','=',order_no),('openid','=',openid)]
        order_ids = order_obj.search(request.cr, SUPERUSER_ID, domain, context=request.context)

        if order_ids:
            ret=order_obj.write(request.cr, SUPERUSER_ID, order_ids[0],{'payment_date':payment_date,'state':'progress','out_trade_no':out_trade_no,'transaction_id':transaction_id})
            #生成优惠券信息
            order =order_obj.browse(request.cr, SUPERUSER_ID,order_ids[0], context=request.context)

            domain=[('openid','=',order.openid)]
            obj_users = request.registry['born.weixin.users']
            user_ids = obj_users.search(request.cr, SUPERUSER_ID, domain,limit=1, context=request.context)
            user=obj_users.browse(request.cr, SUPERUSER_ID,user_ids[0], context=request.context)

            #券内项目
            order_line=[]
            for line in order.order_line:
                item={
                    'product_id':line.product_id.id ,
                    'price_unit':line.price_unit ,
                    'qty':line.product_uom_qty,
                }
                order_line.append((0, 0, item))

            coupon_obj = request.registry.get('born.coupon')
            cous={
                  'no':'WX'+coupon_no,
                  #'source_type':'7',
                  'need_share':'2',
                  'state':'active',
                  'name':u'微信商城购买',
                  'amount':0,
                  'price':order.amount_total,
                  'discount':10.0,
                  'published_date':datetime.date.today(),
                  'active_date':datetime.date.today(),
                  'mobile':user.phone,
                  'mobile_display':user.phone,
                  'member_name':user.realname,
                  'partner_id':user.partner_id.id,
                  'is_push':False,
                  'remark':u'微信商城购买的服务',
                  'card_type':"2",
                  'product_ids':order_line
            }
            coupon_obj.create(request.cr, SUPERUSER_ID,cous,context=request.context)
            if ret:
                return 'SUCCESS'

        return 'FAIL'

    def __create_nonce_str(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

    #生成支付配置签名
    def sign(self,ret):
        data={
              'nonceStr':self.__create_nonce_str(),
              'timestamp':int(time.time()),
              'jsapi_ticket':ret['jsapi_ticket'],
              'url':ret['url'],
        }
        value = '&'.join(['%s=%s' % (key.lower(), data[key]) for key in sorted(data)])
        sign_str= hashlib.sha1(value).hexdigest()
        data['signature']=sign_str
        return data

    #活动抽奖
    @http.route('/lottery/<int:order_id>',  type='http', auth="none", csrf=False)
    def getLottery(self, order_id,**post):

        _logger.info(order_id)
        if not request.session.openid:
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        user_obj = request.registry['res.users']
        company=user_obj.browse(request.cr, SUPERUSER_ID,SUPERUSER_ID, context=request.context).company_id

        sale_order_obj = request.registry.get('sale.order')
        order=sale_order_obj.browse(request.cr, SUPERUSER_ID,int(order_id), context=request.context)
        _logger.info(order.is_lottery)

        tpl = Template(filename=base_lottery_path+'/v1/index.html')
        return tpl.render(company=company,index=1,order=order)

    #活动抽奖
    @http.route('/lotteryResult/<int:order_id>/<int:lottery>',  type='http', auth="none", csrf=False)
    def getLotteryResult(self,order_id,lottery, **post):

        data=False
        if not request.session.openid:
            werkzeug.exceptions.abort(werkzeug.utils.redirect("/except", 303))

        sale_order_obj = request.registry.get('sale.order')
        order=sale_order_obj.browse(request.cr, SUPERUSER_ID,int(order_id), context=request.context)
        if order.spread_id and order.spread_id.id >0 and not order.is_lottery:
            data=order.write({'is_lottery':True})
            #创建奖品
            result_obj = request.registry.get('born.lottery.result')
            spread_obj = request.registry.get('born.spread.product')
            all_order_count= result_obj.search_count(request.cr, SUPERUSER_ID, [('order_id','=',order.id),('openid', '=', request.session.openid)], context=request.context)
            if all_order_count<=0:
                spread_product_ids = spread_obj.search(request.cr, SUPERUSER_ID, [('spread_id','=',order.spread_id.id),('level','=',int(lottery))], context=request.context)
                products=list(spread_obj.browse(request.cr, SUPERUSER_ID,spread_product_ids, context=request.context))
                for product in products:
                    vals={
                        'order_id':order.id,
                        'spread_id':order.spread_id.id,
                        'openid':request.session.openid,
                        'product_id':product.product_id.id,
                        'description':u'您抽中了%s' % (product.name),
                        'state':'draft',
                    }
                    result_obj.create(request.cr, SUPERUSER_ID,vals,context=request.context)
                    _logger.info(u'抽奖完成生成奖品信息')
                    data=True
        return simplejson.dumps(data,sort_keys=True)