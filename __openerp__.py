# -*- coding: utf-8 -*-
##############################################################################
#  COMPANY: BORN
#  AUTHOR: KIWI
#  EMAIL: arborous@gmail.com
#  VERSION : 1.0   NEW  2014/07/21
#  UPDATE : NONE
#  Copyright (C) 2011-2014 www.wevip.com All Rights Reserved
##############################################################################
{
    'name': '微信商城',
    'version': '1.0.1',
    'category': 'BORN',
    'sequence': 1,
    'summary': 'BORN',
    'description': """
          微信商城
    """,
    'author': 'BORN',
    'images': [],
    'depends': ['base','payment','product','sale','point_of_sale','born_member_card'],
    'data': [
        'born_weixin_shop.xml',
        'security/ir.model.access.csv',
    ],
    'css': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}