
{
    'name': 'Web Timesheet',
    'version': '16.0.1.0.0',
    'summary': """ Web Timesheet""",
    'description': """Web Timesheet""",
    'author': 'Mayuri Bharadva & Murendwa Ratshitimba',
    'version': '16.0.0.1.0',
    'category': 'Website',
    'depends': ['website', 'project', 'hr', 'timesheet_grid'],
    'data': [
        'views/templates.xml',
        'views/portal.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'web_timesheet/static/src/js/custom.js',
        ],
    },
    'licence': 'LGPL-3',
    'installable': True,
    'application': False,
    'images': ['static/description/banner.png'],
    'auto_install': False,
    'price': 50,
    'currency': "USD"
}
