# -*- coding: utf-8 -*-
##############################################################################
#  COMPANY: BORN
#  AUTHOR: LIUHAO
#  EMAIL: arborous@gmail.com
#  VERSION : 2.0    2016/05/20
#  UPDATE : NONE
#  Copyright (C) 2011-2014 www.wevip.com All Rights Reserved
##############################################################################

from openerp.osv import fields, osv
from openerp import models,fields,api
from openerp import _
import logging
import openerp.addons.decimal_precision as dp

_logger = logging.getLogger(__name__)

class born_sale_order(models.Model):
    _inherit = 'sale.order'

    sale_category = fields.Selection([('weixin', u'微信商城'),('online', u'在线销售'),('normal', u'普通销售'),], default='normal',string=u'状态',help=u'销售类型')
    is_weixin_unlick = fields.Boolean(u'微信删除订单',help=u"微信删除订单",default=False)
    openid = fields.Char('OPENID',size=255,help="OPENID")
    weixin_user_id = fields.Many2one('born.weixin.users',u'关注者',help=u"关注者")
    out_trade_no = fields.Char(u'微信对应订单号',size=255,help=u"微信对应订单号")
    transaction_id = fields.Char(u'微信支付流水号',size=255,help=u"微信支付流水号")
    is_lottery= fields.Boolean(u'是否已经抽奖', help=u'是否已经抽奖',default=False)
    spread_id = fields.Many2one('born.spread', u'活动编号')
    payment_date = fields.Datetime(u'付款日期' )
    
class born_weixin_cart(osv.osv):
    _name ="born.weixin.cart"
    _description = u"购物车"

    openid = fields.Char(u'OPENID',size=255,help=u"OPENID")
    product_id = fields.Many2one('product.product', u'产品', required=True, )
    qty = fields.Float(u'数量', digits=(6,2) )
    state = fields.Selection([
        ('draft', u'草稿'),
        ('checkout', u'结帐'),
        ('finish', u'完成'),
        ], u'状态', default='draft', help=u"状态", select=True)

    _order = 'id desc'

#关注的产品
class born_follow_product(osv.osv):
    _name = 'born.follow.product'

    product_id = fields.Many2one('product.product', u'产品',)
    openid = fields.Char(u'OPENID',size=255,help=u"OPENID")

class born_browsing_history(osv.osv):
    _name = 'born.browsing.history'

    product_id = fields.Many2one('product.product', u'产品',)
    openid = fields.Char(u'OPENID',size=255,help=u"OPENID")

#收货地址
class born_address(osv.osv):
    _name = 'born.address'

    user_name = fields.Char(u'收货人',size=255,help=u"收货人")
    phone = fields.Char(u'电话',size=255,help=u"电话")
    address = fields.Char(u'详细地址',size=255,help=u"详细地址")
    default = fields.Boolean(u'默认地址', help=u"默认地址")
    country_id = fields.Many2one('res.country', u'国家', ondelete='restrict')
    state_id = fields.Many2one("res.country.state", u'省', ondelete='restrict')
    area_id = fields.Many2one('res.country.state.area', u'市')
    subdivide_id= fields.Many2one('res.country.state.area.subdivide', u'区域', select=True, track_visibility='onchange')

#抽奖活动
class born_lottery(osv.osv):
    _name = 'born.lottery'

    name = fields.Char(u'名称',size=255,help=u"名称")
    path = fields.Char(u'文件夹名称',size=255,help=u"文件夹名称")
    image = fields.Binary(u"预览")
    level = fields.Integer(u'中奖等级', digits=(2,0))
    description = fields.Text(u'说明', )

#活动
class born_spread(osv.osv):
    _name = 'born.spread'

    name = fields.Char(u'名称',size=255,help=u"名称")
    lottery_id = fields.Many2one("born.lottery", u'抽奖方式')
    description = fields.Text(u'说明', )
    image = fields.Binary(u"展示图片")
    start_date = fields.Date(u'开始日期')
    end_date = fields.Date(u'结束日期')
    start_order_amount = fields.Float(u'最小订单金额',digits_compute=dp.get_precision('Account'),help=u"参加抽奖需要订单金额达到金额")
    product_ids = fields.One2many('born.spread.product', 'spread_id', u'奖品列表')
    product_limit_ids = fields.One2many('born.spread.limit.product', 'spread_id', u'必须购买以下产品后才能参与抽奖')

#奖品
class born_spread_product(osv.osv):
    _name = 'born.spread.product'

    product_id = fields.Many2one('product.product', u'产品',)
    spread_id = fields.Many2one("born.spread", u'活动')
    level = fields.Integer(u'中奖等级', digits=(2,0))
    invalid_date = fields.Date(u'失效日期')
    name = fields.Char(u'说明',size=255,help=u"名称",required=True,)

#参与抽奖限制
class born_spread_limit_product(osv.osv):
    _name = 'born.spread.limit.product'

    product_id = fields.Many2one('product.product', u'产品',)
    spread_id = fields.Many2one("born.spread", u'活动')

#奖品表
class born_lottery_result(osv.osv):
    _name = 'born.lottery.result'

    weixin_user_id = fields.Many2one('born.weixin.users', u'微信用户',)
    order_id = fields.Many2one('sale.order', u'订单',)
    spread_id = fields.Many2one('born.spread', u'活动')
    openid = fields.Char(u'OPENID',size=255,help=u"OPENID")
    state = fields.Selection([
       ('draft', u'未使用'),
       ('done', u'已使用'),
       ('invalid', u'已失效')
       ], u'状态',  help=u"状态", select=True)
    invalid_date = fields.Date(u'失效日期')
    product_id = fields.Many2one('product.product', u'奖品',)
    description = fields.Char(u'说明',size=255,help=u"说明")

