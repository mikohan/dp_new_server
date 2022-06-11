from django.core.mail import send_mail

def test_mail():

    send_mail(
        'Subject here',
        'Here is the message.',
        'angara77@gmail.com',
        ['angara99@gmail.com'],
        fail_silently=False,
    )