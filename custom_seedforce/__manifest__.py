{
    'name' : 'SeedForce',
    'version': '4.11',
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
        #'views/contact_form.xml',
        #'views/signup_template.xml'
        
         ],
    'installable': True,
    'application':True,
    'auto_install':True
}
