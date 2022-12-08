from datetime import datetime, timedelta
import re


def dict_for_celebrate(new_birthday_dict, period):

    # Створення словника, в якому позначено коли і кого привітати, починаючи з поточного дня

    happy_dict = {}

    for n_name, n_dat in new_birthday_dict.items():
        if 0 <= n_dat.day - datetime.now().day < period:
            happy_dict[n_name] = n_dat
    return happy_dict


def output_birthday(happy_dict):

    # Функція виводу днів тижня та іменинників зі словника
    week_days = []
    for i in range(1, 8):
        week_days.append((datetime.today()+timedelta(days=i)).strftime('%A'))
    celebrate_dict = {}

    for d in week_days:
        celebrate_list = []
        for name, date in happy_dict.items():
            if date.strftime('%A') == d:
                celebrate_list.append(name)
                celebrate_dict[d] = celebrate_list

    st = ''
    for day, name in celebrate_dict.items():
        some_names = ""
        for i in name:
            if name[-1] == i:
                some_names += i
            else:
                some_names += i + ', '
        st += "".join((day + ": " + some_names)) + '\n'

    return print(st)


def when_celebrate(birthday_dict):

    # Перетворення словника на словник з об'єктами datetime і міняються ДР, які в СБ і НД на др в ПН

    new_birthday_dict = {}
    for name, dat in birthday_dict.items():
        date = re.split("/", dat)
        birth = datetime(year=datetime.now().year, month=int(date[1]), day=int(date[0]))
        if birth.isocalendar()[2] == 7:
            birth = birth.replace(day=birth.day+1)
        if birth.isocalendar()[2] == 6:
            birth = birth.replace(day=birth.day+2)
        new_birthday_dict[name] = birth

    return new_birthday_dict


def get_birthday(birthdict):

    when_celebr = when_celebrate(birthdict)
    output_dict = dict_for_celebrate(when_celebr, 7)
    output_birthday(output_dict)


if __name__ == '__main__':
    birthday_dict = {
        "Yulia": "06/12/1996",
        'Yarpl': '07/12/1997',
        'Sunny': '26/12/2000',
        'Luk': '10/12/1995',
        'Sim': '12/12/1991',
        'Nok': '14/12/1994',
        'Kred': '13/12/1994',
        'Tim': '18/12/1997',
        'Kooc': '09/12/1997'
    }

    get_birthday(birthday_dict)
