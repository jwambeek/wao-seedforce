{
    'name' : 'SeedForce',
    'version': '3.8',
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


    ],
    'installable': True,
    'application':True,
    'auto_install':False
}
