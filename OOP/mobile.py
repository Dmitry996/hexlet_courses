class MobilePhone:
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
        self.state = self.states['power_on'](self)

        self.notify('power_on')

    def power_off(self):
        print(1)
        pass

    def camera_on(self):
        # я решил что у камеры есть отдельная кнопка :)
        self.state.camera_on()

    def touch_ок(self):
        # это типо нажатие на кнопку управления
        self.state.touch_ок()

    def touch_menu(self):
        self.state.touch_menu()

    def touch_options(self):
        self.state.touch_options()

    def keyboard(self):
        self.state.keyboard()
        # Думаю полностью организововать клавиатуру нет смысла

    def notify(self, event):
        print(f"Received event: {event}")


class Сonnection:
    def touch_menu(self):
        self.phone_status.state = self.phone_status.states['power_on']

        self.phone_status.notify('power_on')

    def touch_options(self):
        phone_book = {"тут телефонная книга": '8-800-555-35-35'}
        self.number = phone_book.get(input())

    def keyboard(self):
        return input()


class PowerOff:
    def __init__(self, phone_status):
        self.phone_status = phone_status

    def power_on(self):
        self.phone_status.state = self.phone_status.states['power_on'](self)

        self.phone_status.notify('power_on')

    def power_off(self):
        pass

    def camera_on(self):
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
        self.phone_status.state = self.phone_status.states['power_off'](self)

        self.phone_status.notify('power_off')

    def camera_on(self):
        self.phone_status.state = self.phone_status.states['camera'](self)

        self.phone_status.notify('camera')

    def touch_ок(self):
        self.phone_status.state = self.phone_status.states['phone'](self)
        # тут идет по аналогии со старыми телефонами
        self.phone_status.notify('phone')

    def touch_menu(self):
        menu = {
            'camera': 'camera',
            'phone': 'phone',
            'sms': 'sms',
            'calendar': 'calendar'
        }
        choice = menu.get('sms')  # тут должен быть инпут
        # это упрошенный выбор меню,
        # представим что мы тут как то урпаляем кнопками через input
        self.phone_status.state = self.phone_status.states[choice](self)

        self.phone_status.notify(choice)

    def touch_options(self):
        pass  # тут дополнительные настройки телефона

    def keyboard(self):
        pass

    def notify(self, event):
        print(f"Received event: {event}")


class Phone(Сonnection):  # Я хз как назвать класс в котором происходят вызовы
    def __init__(self, phone_status):
        self.phone_status = phone_status
        self.number = self.keyboard()

    def touch_ок(self):
        self.phone_status.notify(f'call to the number - {self.number}')


class SMS(Сonnection):
    def __init__(self, phone_status):
        self.phone_status = phone_status
        self.number = self.keyboard()
        self.text = self.keyboard_text()

    def touch_ок(self):
        self.phone_status.notify(f'sms to the number - {self.number}')

    def keyboard_text(self):
        return input()


class Menu:
    def __init__(self, phone_status):
        self.phone_status = phone_status

    def touch_menu(self):
        self.phone_status.state = self.phone_status.states['power_on'](self)

        self.phone_status.notify('power_on')

    def keyboard(self):
        pass


class Camera(Menu):
    def touch_ок(self):
        self.phone_status.notify('photo/video')

    def touch_options(self):
        pass  # тут происходит переход в настройки photo/video


class Calendar(Menu):
    def touch_ок(self):
        # тут происходить просмотр выбранаго для
        self.phone_status.notify('day')

    def touch_options(self):
        pass  # тут происходит переход в выбор дней, недель месяцов..

    def keyboard(self):
        pass  # навигация по календарю
