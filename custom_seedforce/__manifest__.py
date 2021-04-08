{
    'name' : 'SeedForce',
    'version': '5.0',
    'Summary': '',
    'description': 'Pass the field value into sale order',
    'license': 'LGPL-3',
    'depends': [
        'account_accountant',
        'purchase',
        'website',
        'contacts',
        'sale_management',
        'product',
    ],    
     'data': [
        'views/signup.xml',
        'views/saleorder_view.xml'


    ],
    'installable': True,
    'application':True,
    'auto_install':False
}
