# -*- coding: utf-8 -*-
# © <2016> <Cristian Salamea>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Conciliaciones Bancarias',
    'version': '10.0.1.0.0',
    'category': 'Generic Modules/Accounting',
    'license': 'AGPL-3',
    'depends': [
        'account',
    ],
    'author': 'Cristian Salamea <cristian.salamea@ayni.com.ec>',
    'website': 'http://www.ayni.com.ec',
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/sequence.xml'
    ]
}
