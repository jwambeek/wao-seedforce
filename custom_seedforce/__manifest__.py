{
    'name' : 'SeedForce',
    'version': '0.1',
    'Summary': '',
    'description': 'Pass the field value into sale order',
    'license': 'LGPL-3',
    'depends': [
        'account_accountant',
        'account',
        'account_consolidation',
        'website_sale',
        'sale_management',
        'product',
    ],    
     'data': [
        #'views/mrp_view.xml',
        'views/website_form.xml'
    ],
    'installable': True,
    'application':True,
    'auto_install':True
}
