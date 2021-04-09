{
    'name' : 'SeedForce',
    'version': '3.16',
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
        #'views/website_form.xml',
        #'views/test_form.xml',
        #'views/sale_harvest_view.xml',
        'views/template.xml',
        'views/signup_template.xml'
        
         ],
    'installable': True,
    'application':True,
    'auto_install':False
}
