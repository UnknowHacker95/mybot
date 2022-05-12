from googletrans import Translator

translator = Translator()

def number(text):
  return any(char.isdigit() for char in text)

class NLU:
    def __init__(self):
        pass
    def right(self, message, state):
        if state == 'vibor':
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
        elif state == 'start':
            if(message == 'Хочу историю'):
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
                tems[0] = translator.translate(tems[0], src='ru', dest='en').text
                tems[1] = translator.translate(tems[1], src='ru', dest='en').text
                return tems

def text(a):
    import requests
    s = a[0] + ' and ' + a[1]
    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': s,
        },
        headers={'api-key': '89116dba-6d4a-4c86-977a-04b7d8a82029'}
    )
    string = r.json()['output']
    string = translator.translate(string, src='en', dest='ru').text
    return string

def illustrachiya(b):
    import requests
    s = translator.translate(b, src='ru', dest='en').text
    r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': s,
        },
        headers={'api-key': '89116dba-6d4a-4c86-977a-04b7d8a82029'}
    )
    return r.json()['output_url']
