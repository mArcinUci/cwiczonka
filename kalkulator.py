import logging

logging.info('są dwie zmienne i cztery opcje podstawowych działań między nimi. Please pick one.')
s = int(input('podaj pierwsza liczbę: '))
d = int(input('podaj drugą liczbę: '))
logging.warning('remember, to make it work right, pick digit from 1 to 4 in a third question')
y = str(input('jakie działanie chcesz wykonać: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie? Wybierz cyfrę 1-4: '))
score = ''
if y == str(1):
    score = s + d
elif y == str(2):
    score = s - d
elif y == str(3):
    score =  s * d
elif y == str(4):
    if s == 0:
        print('you cannot divide 0, mate')
    elif d == 0:
        print('you cannot divide 0, mate')
    else:
        score = s / d
else:
    print('hmm.. aby wszystko sprawnie działało, musisz w trzecim pytaniu wybrać cyfrę od 1 do 4')
print(score)