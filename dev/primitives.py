def get_bus(num=None,endstations=None,timetable=None,timetable_weekends=None):
    obj = {
        'num':num,
        'endstations':endstations,
        'timetable':timetable,
        'timetable_weekends':timetable_weekends,
    }
    return obj

#Примерный вид запроса, или примерный вид одного из автобусов в BUS_DATA
#num = 1
#endstations = ['Куйбышева', 'Плеханова']
#timetable = [['10:23','12:30','21:12'],['9:23','11:30','20:12']]  #Отправление от ['Куйбышева','Плеханова']
#timetable_weekends = False # То же самое, только в выходной день
#my_obj = get_bus(num,endstations,timetable,timetable_weekends)
