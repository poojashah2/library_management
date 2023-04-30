{
    'name' : 'parking management',
    'version' : '15.0.0.1.0',
    'description' : 'Parking Management module details',
    'depends' : [],
    'data' : [
        'security/ir.model.access.csv',
        'views/parking_info.xml',
        'views/book_parking.xml',
        'views/slot_info.xml',
        'views/security_info.xml',
        'views/vehicle_info.xml',
        'views/register_parking_info.xml',
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}