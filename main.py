class Door():

    DOOR_STATUS_ON = True
    DOOR_STATUS_OFF = False
    DOOR_LOKER_ON = True
    DOOR_LOKER_OFF = False

    def __init__(self, door_status):
        self.door_status = door_status
        self.door_loker = self.DOOR_LOKER_ON
        self.exit = 'выход'

    def door_status_new(self):
        if self.door_status == self.DOOR_STATUS_ON:
            print('Ваша дверь открыта')
        else:
            print('Ваша дверь закрыта')

    def door_close(self):
        if self.door_status == self.DOOR_STATUS_OFF:
            if self.door_loker == self.DOOR_LOKER_ON:
             print('Дверь нельзя закрыть так как она уже закрыта')
            else:
             print('Дверь нельзя закрыть так как она заперта на замок')
        else:
            if self.door_loker == self.DOOR_LOKER_ON:
                self.door_status = self.DOOR_STATUS_OFF
                print('Дверь закрыта')

    def door_open(self):
        if self.door_status == self.DOOR_STATUS_OFF:
            if self.door_loker == self.DOOR_LOKER_ON:
                self.door_status = self.DOOR_LOKER_ON
                print('Дверь открыта')
            else:
                print('Дверь нельзя открыть, так как она закрыта на замок')
        else:
            if self.door_status == self.DOOR_STATUS_ON:
                if self.door_loker == self.DOOR_LOKER_OFF:
                    print('Дверь нельзя открыть, она закрыта на замок')
                else:
                     print('Дверь нельзя открыть она уже открыта')

    def loker_open(self):
        if self.door_loker == self.DOOR_LOKER_ON:
            if self.door_status == self.DOOR_STATUS_OFF:
                print('Дверь нельзя отпереть, так как дверь не заперта')
            else:
                print('Дверь нельзя отпереть, так как дверной замок открыт и дверь открыта')
        else:
            if self.door_loker == self.DOOR_LOKER_OFF:
                if self.door_status == self.DOOR_STATUS_OFF:
                    self.door_loker = self.DOOR_LOKER_ON
                    print('Дверной замок открыт')
                else:
                    print('Дверь нельзя отпереть, так как дверной замок открыт')


    def loker_close(self):
        if self.door_loker == self.DOOR_LOKER_OFF:
            if self.door_status == self.DOOR_STATUS_ON:
                print('Дверь нельзя запереть так как она открыта')
            else:
                print('Дверь нельзя запереть так как она уже заперта')
        else:
            if self.door_loker == self.DOOR_LOKER_ON:
                if self.door_status == self.DOOR_STATUS_OFF:
                    self.door_loker = self.DOOR_LOKER_OFF
                    print('Дверь заперта на замок')
                else:
                    print('Дверь нельзя запереть так как она открыта')


print(
    'Приветствую.' + '\n' + 'Данная программа является симулятором двери.' + '\n' + "В ней Вы сможете создать свою дверь,а так же открывать или закрывать ее на замок.")
print('Дверь работает с командами: Открыть, Закрыть ')

print('\n' + 'Пристутим к созданию двери!' + '\n' + "Пожалуйсто, введите команду двери : ")
while True:
    a = input().lower()
    if (a == "открыть") or (a == 'закрыть'):
        a1 = a == "открыть"
        new_door = Door(a1)
        new_door.door_status_new()
        break
    if a == 'q':
        try:
            a1 = int(100)
            b = int(0)
            c = a1/b
            print(c)
        except:
            print('Ошибка деления на ноль' + '\n' + '\n' + "Пожалуйсто, введите команду двери : ")
        continue
    else:
        print('\n' + 'Команда введена не верно, пожалуйста повторите попытку.')

print('При помощи замка можно отпереть и запереть дверь используя команды: Отпереть, Запереть ')
print("Если захочешь выйти из программы, просто введи команду: Выход")

while True:
    print('\n' + "Пожалуйсто, введите команду для двери: ")
    a = input().lower()
    if a == new_door.exit:
        print('Всего доброго!')
        break
    elif not a:
        print("Негодяй! Вы не ввели команду. Пожалуйста, введите команду")
        continue
    elif a == 'открыть':
        new_door.door_open()
        continue
    elif a == 'закрыть':
        new_door.door_close()
    elif a == 'запереть':
        new_door.loker_close()
    elif a == 'отпереть':
        new_door.loker_open()
    else:
        print('Введена неверная команда. Пожалуйста, введите команду')