{
    'name' : 'SeedForce',
    'version': '1.0',
    'Summary': '',
    'description': 'Pass the field value into sale order',
    'license': 'LGPL-3',
    'depends': [
        'account_accountant',
        'purchase',
        'account_consolidation',
        'website',
        'sale_management',
        'product',
    ],    
     'data': [
        'views/website_form.xml'
    ],
    'installable': True,
    'application':True,
    'auto_install':True
}
