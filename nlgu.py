import googletrans
from googletrans import Translator
translator = Translator()

def number(text):
  return any(char.isdigit() for char in text)

class NLU:
    def __init__(self):
        pass
    def right(self, message, state):
        if state == 'tema':
            if (message =='Да'):
                return 1
            elif (message == 'Нет'):
                return 0
            else :
                return 'Error'
        elif state == 'history':
            if(message == 'Хочу иллюстрацию'):
                return 1
            else:
                return 'Error'
        else:
            if(number(message) == 'True'):
                return 'Error'
            else:
                if(len(message) < 3):
                    return 'Error'
                tems = message.split()
                tems[0] = translator.translate('папа')
                tems[1] = translator.translate('мир')
                return tems

