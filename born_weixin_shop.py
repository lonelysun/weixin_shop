# -*- coding: utf-8 -*-
##############################################################################
#  COMPANY: BORN
#  AUTHOR: LIUHAO
#  EMAIL: arborous@gmail.com
#  VERSION : 2.0    2016/05/20
#  UPDATE : NONE
#  Copyright (C) 2011-2014 www.wevip.com All Rights Reserved
##############################################################################

import openerp
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


#标志分类
class born_shop_category(models.Model):
    _name = 'born.shop.category'

    @api.one
    @api.depends('image')
    def _make_local_url(self):
        for line in self:
            if self.image:
                domain=[('type','=','binary'),('res_field','=','image'),('res_model','=','born.shop.category'),('res_id','=',self.id)]
                attachment=self.env['ir.attachment'].search(domain,limit=1)
                if attachment:
                    server_url=openerp.tools.config['localhost_server_url']
                    image_url='%s%s' % (server_url,attachment.local_url)
                    line.image_url = image_url


    name = fields.Char(u'名称')
    image = fields.Binary(u'标志图片', attachment=True)
    image_url =  fields.Char(string=u'图片地址', compute='_make_local_url',multi='_make_local_url', help=u"图片地址")
    type = fields.Selection([('url', u'链接'),('product_ids',u'商品'),('category_ids',u'分类'),('content_ids',u'文章'),('function_ids',u'功能')], default='url',string=u'类型',help=u'类型')
    sequence = fields.Integer(u'排序')
    description = fields.Text(u'说明')

class born_ir_attachment(models.Model):
    _inherit = "ir.attachment"

    # 创建
    @api.model
    def create(self, vals):
        if vals.get('res_model') == 'born.shop.category':
            vals['public'] = True
        return super(born_ir_attachment, self).create(vals)




class born_shop_position(models.Model):
    _name = 'born.shop.position'

    name = fields.Char(u'名称')


class born_shop_template(models.Model):
    _name = 'born.shop.template'

    name = fields.Char(u'模版名')
    poistion_ids = fields.Many2many('born.shop.position',string=u'位置')
    color = fields.Selection([('blue', u'蓝色'),('red',u'红色'),('black',u'黑色'),('green',u'绿色')], default='blue',string=u'颜色主题',help=u'颜色主题')


class born_shop_model(models.Model):
    _name = 'born.shop.model'

    name = fields.Char(u'模块名')
    type = fields.Selection([('url', u'幻灯片'),('product_ids',u'文章'),('category_ids',u'产品'),('content_ids',u'分类'),('function_ids',u'功能')], default='url',string=u'类型',help=u'类型')
    category_ids = fields.Many2many('born.shop.category',string=u'内容')



class born_shop_config(models.Model):
    _name = 'born.shop.config'

    name = fields.Char(u'名称')
    template_id = fields.Many2one('born.shop.template',u'模版')
    position_model = fields.Many2many('position.model',string=u'模块位置')


class position_model(models.Model):
    _name = 'position.model'

    position_id = fields.Many2one('born.shop.position',u'位置')
    model_id = fields.Many2one('born.shop.model',u'模块')

class born_shop_nav(models.Model):
    _name = 'born.shop.nav'

    name = fields.Char(u'名称')
    sequence = fields.Integer(u'排序')
