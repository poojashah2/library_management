{
    'name': "Hotel Management",
    "summary":"",
    "description": "",
    "version": "15.0.0.0",
    "depends": ['contacts','mail'],
    "data": [
       'security/ir.model.access.csv',
       'data/ir_sequence_room_code.xml',
       'data/room_booked_mail_template.xml',
       'data/cancel_booking_mail_template.xml',
       'data/email_reminder_check_out_data.xml',
       'data/email_reminder_check_out_mail_template.xml',
       'views/hotel_details_view.xml',
       'views/hotel_room_view.xml',
       'views/hotel_room_booking_view.xml',
       'views/hotel_room_booking_line_view.xml',
       'wizard/confirmation_booking_wizard.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}