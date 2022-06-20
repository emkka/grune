# -*- coding: utf-8 -*-

{
    'name': 'Website Product',
    'category': 'Website',
    'summary': 'Book Hotel Rooms Online',
    'website': 'https://www.odoo.com/page/website-builder',
    'version': '1.23',
    'author': 'Pragmatic TechSoft Pvt Ltd',
    'depends': ['web', 'website', 'website_sale_coupon', 'hotel_management', 'payment', 'website_sale', 'portal'],
    'description': """
        Book Rooms Online
         
        hotel_online Module used for select and book the hotel rooms online.\n
        It also allow user to pay the bill online

    """,
    'data': [

            'views/website_event_search.xml',
            'views/website_book_room.xml',
            'views/hotel_reservation.xml',
            'views/website_home.xml',
            'views/coupon_program.xml',
            'static/src/data/website_menu.xml',
    ],
    'demo': [

    ],
    'assets': {
        'web.assets_backend': [
            "/hotel_online/static/src/js/form_widgets.js",
        ],
        'web.assets_frontend': [
            "/hotel_online/static/src/js/bootstrap.min.js",
            "/hotel_online/static/lib/css/style.css" ,
            "/hotel_online/static/lib/css/datepicker1.css" ,
            "/hotel_online/static/lib/css/datepicker2.css" ,
            '/hotel_online/static/lib/slider/css/lightslider.css',
            "/hotel_online/static/lib/slider/css/lightbox.css",
            "/hotel_online/static/src/js/website_sale_validate.js",
            "/hotel_online/static/lib/slider/js/lightslider.js",
            "/hotel_online/static/lib/slider/js/test.js",
            "/hotel_online/static/lib/slider/js/new_js_file.js",
        ],
    },
    'installable': True,
    'license' : 'LGPL-3',
}
