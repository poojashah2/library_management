{
    'name' : 'library management',
    'version' : '15.0.0.1.0',
    'description' : 'library management module details',
    'depends' : [],
    'data' : [
        'security/ir.model.access.csv',
        'data/ir_sequence_book.xml',
        'views/book_author_info.xml',
        'views/book_details_info.xml',
        'views/register_books_info.xml',
        'views/issue_book_info.xml',
        'views/register_date_info.xml',
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}