class MobilePhone():
    def __init__(self):
        self.states = {
            'power_off': PowerOff,
            'power_on': PowerOn,
            'camera': Camera,
            'phone': Phone,
            'sms': SMS,
            'calendar': Calendar
        }

        self.state = self.states['power_off'](self)

    def power_on(self):
        pass  # Они тут как бы не нужны по пусть будут как основа

    def power_off(self):
        pass

    def camera_on(self):
        # я решил что у камеры есть отдельная кнопка :)
        self.state.camera_on()

    def touch_ок(self):
        # это типо нажатие на кнопку управления
        self.state.touch_ok()

    def touch_menu(self):
        self.state.touch_menu()

    def touch_options(self):
        self.state.touch_options()

    def keyboard(self):
        self.state.keyboard()
        # Думаю полностью организововать клавиатуру нет смысла

    def notify(self, event):
        print(f"Received event: {event}")


class PowerOff:
    def __init__(self, phone_status):
        self.phone_status = phone_status

    def power_on(self):
        self.phone_status.state = self.states['power_on']

        self.phone_status.notify('power_on')

    def power_off(self):
        pass

    def touch_ок(self):
        pass

    def touch_menu(self):
        pass

    def touch_options(self):
        pass

    def keyboard(self):
        pass


class PowerOn:
    def __init__(self, phone_status):
        self.phone_status = phone_status

    def power_on(self):
        pass

    def power_off(self):
        self.phone_status.state = self.states['power_off'](self)

        self.phone_status.notify('power_off')

    def touch_ок(self):
        self.phone_status.state = self.states['phone'](self)
        # тут идет по аналогии со старыми телефонами
        self.phone_status.notify('phone')

    def touch_menu(self):
        menu = {
            'camera': 'camera',
            'phone': 'phone',
            'sms': 'sms',
            'calendar': 'calendar'
        }
        choice = menu.get(input())
        # это упрошенный выбор меню,
        # представим что мы тут как то упоавляем кнопками через input
        self.phone_status.state = self.states[choice](self)

        self.phone_status.notify(choice)

    def touch_options(self):
        pass  # тут дополнительные настройки телефона

    def keyboard(self):
        pass


class Phone:  # Я хз как назвать класс в котором происходят вызовы
    def __init__(self, phone_status):
        self.phone_status = phone_status
        self.number = self.keyboard()

    def touch_ок(self):
        self.phone_status.notify(f'call to the number - {self.number}')

    def touch_menu(self):
        self.phone_status.state = self.states['power_on']

        self.phone_status.notify('power_on')

    def touch_options(self):
        phone_book = {"тут телефонная книга": '8-800-555-35-35'}
        self.number = phone_book.get(input())

    def keyboard(self):
        return input()


class SMS:
    def __init__(self, phone_status):
        self.phone_status = phone_status
        self.number = self.keyboard()
        self.text = self.keyboard_text()

    def touch_ок(self):
        self.phone_status.notify(f'sms to the number - {self.number}')

    def touch_menu(self):
        self.phone_status.state = self.states['power_on']

        self.phone_status.notify('power_on')

    def touch_options(self):
        phone_book = {"тут телефонная книга": '8-800-555-35-35'}
        self.number = phone_book.get(input())

    def keyboard(self):
        return input()

    def keyboard_text(self):
        return input()


class Camera():
    def __init__(self, phone_status):
        self.phone_status = phone_status

    def touch_ок(self):
        self.phone_status.notify('photo/video')

    def touch_menu(self):
        self.phone_status.state = self.states['power_on']

        self.phone_status.notify('power_on')

    def touch_options(self):
        pass  # тут происходит переход в настройки photo/video

    def keyboard(self):
        pass


class Calendar:
    def __init__(self, phone_status):
        self.phone_status = phone_status

    def touch_ок(self):
        pass  # тут происходить просмотр выбранаго для

    def touch_menu(self):
        self.phone_status.state = self.states['power_on']

        self.phone_status.notify('power_on')

    def touch_options(self):
        pass  # тут происходит переход в выбор дней, недель месяцов..

    def keyboard(self):
        pass  # навигация по календарю
