# Создайте функцию send_email, которая принимает 2 обычных аргумента:
# message(сообщение), recipient(получатель) и 1 обязательно именованный
# аргумент со значением по умолчанию sender = "university.help@gmail.com".
# Если строки recipient и sender не содержит "@" или не оканчивается на
# ".com"/".ru"/".net", то вывести на экран(в консоль) строку: "Невозможно
# отправить письмо с адреса <sender> на адрес <recipient>".
# Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо
# самому себе!"
# Если же отправитель по умолчанию - university.help@gmail.com, то вывести
# сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
# В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо
# отправлено с адреса <sender> на адрес <recipient>."
# Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
# За один вызов функции выводится только одно и перечисленных уведомлений!
# Проверки перечислены по мере выполнения.

def bool(value)-> bool:
    pattern = [".com", ".ru", ".net", "@"]
    boolTmp = False
    for i in range(len(pattern) - 1):
        if (value.find(pattern[i]) != -1) and (value.count(pattern[len(pattern) - 1]) == 1):
            boolTmp = True

    return boolTmp

def sendEmail(message, recipient, sender = "university.help@gmail.com"):
    b1 = recipient == sender
    if bool(recipient) == False or bool(sender) == False:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif  recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")




sendEmail('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
sendEmail('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
sendEmail('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
sendEmail('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


