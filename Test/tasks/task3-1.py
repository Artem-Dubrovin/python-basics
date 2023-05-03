import os
while True:
    link = input('Введите домен:\n')
    if 'https://' in link:
        link = 'www.' + link
        os.system('start ' + link)
    elif 'www.' in link:
        link = 'https://' + link
        os.system('start ' + link)
    else:
        link = 'https://www.' + link
        os.system('start ' + link)