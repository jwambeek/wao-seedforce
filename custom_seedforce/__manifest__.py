{
    'name' : 'SeedForce',
    'version': '1.5',
    'Summary': '',
    'description': 'Pass the field value into sale order',
    'license': 'LGPL-3',
    'depends': [
        'account_accountant',
        'purchase',
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
