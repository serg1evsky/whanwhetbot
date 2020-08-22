# Это файл настроек для whanwhetbot
# Код подкреплен коментариями,
# надеюсь вы всё поймёте)
# Места, в которых нужно поставить
# True или False я буду помечать "TF"

#import primitives

#[TF] Будет ли ваш модуль работать онлайн (т.е парсить работу сайта)
ONLINE = None

#[TF] Вы описываете расписание автобуса?
BUS = True

#Здесь вы указываете данные об транспорте. Подробнее в примитивах
BUS_DATA = []
#Soon trolleibus






def handshake():
    handshake = []
    if BUS:
        if BUS_DATA != []:
               handshake = {'bus':True, 'transport_info': BUS_DATA}
        else:
            handshake = 'Ошибка в сеттингс: Нет бас даты'
            exit()
    return handshake