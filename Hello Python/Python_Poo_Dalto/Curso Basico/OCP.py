# it is open system to create another classes but without modified if so is closed to modify
class Notifier: # main class tell another person or dev he/she  need to put something
  def __init__(self, user, message) -> None:
    self.user = user
    self.message = message
  def notify(self):
    raise NotImplementedError

class NotifierEmail (Notifier):
  def notify(self):
    print(f'Sending message by email to: {self.user.email}')
    return super().notify()

class NotifierSMS (Notifier):
  def notify(self):
    print(f'Sending SMS to: {self.user.sms}')
    return super().notify()

class NotifierSMS (Notifier):
  def notify(self):
    print(f'Sending SMS by facebook to: {self.user.facebook}')
    return super().notify()

class NotifierSMS (Notifier):
  def notify(self):
    print(f'Sending twit by x to: {self.user.x}')
    return super().notify()