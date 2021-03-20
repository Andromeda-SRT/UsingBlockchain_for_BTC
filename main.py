import requests
import json
import time

url = 'https://blockchain.info/ru/ticker'

def putData():
    return requests.get(url).text


data = json.loads(putData())
print(f'3.5 Перекодированный словарь:',data, '\n')

print(f'3.6 Результаты только по RUB: ')
for key, value in data["RUB"].items():
    print(key, value)

print(f'\n3.7 Цикл на обновление значений в ‘RUB’ с задержкой 5с: ')
num = 0
while True:
    response = requests.get(url).text
    data2 = json.loads(response)
    for key, value in data2["RUB"].items():
        print(key, value)
    time.sleep(5)
    if num == 1:
        break
    num += 1

print(f'\n3.8 Введите префикс валюты')
n = input()
for key, value in data[n].items():
    print(key, value)

print(f'\n3.9 Введите префикс валюты по каторой хотите закупить битки')
n = input()

print(f'Способ 1:')
for key, value in data[n].items():
    if key == 'buy':
        print(key, value, n, "for 1 BTC")

print(f'Способ 2:')
for key, value in data[n].items():
    d = json.dumps(data[n])
# print(d)
d2 = json.loads(d)
# print(d2)
for i in d2:
    if i == 'buy':
        print(f'buy BTC for',d2[i], n)