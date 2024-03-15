import os
import csv
def conv(path):
    infocsv = []
    with open('info_new.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i in reader:
            infocsv.append(i)
    dic = {}
    changes = {'Cipher : /2&//<|0': 'Cipher', 'ρars/ey': 'ρarsley', 'Labyrinth in Kowloon: Walled World': 'Labyrinth in Kowloon Walled World',}
    for i in infocsv:
        n1, n2 = i[:2]
        n1 = n1.strip()
        n2 = n2.strip().replace('\xa0', ' ')
        if 'AnotherMe' in n1:
            if n1 == 'AnotherMe.NeutralMoon':
                dic[n1] = 'Another Me - Rising Sun Traxx'
            else:
                dic[n1] = 'Another Me - KALPA'
        else:
            dic[n1] = changes.get(n2, n2)
    for i in range(1, 7):
        dic[f'Random.SobremSilentroom.{i}'] = f'Random [{" RANDOM"[i]}]'
    for i in os.listdir(path):
        name = '.'.join(i.split('.')[:-1])
        ext = i.split('.')[-1]
        if name in dic:
            os.rename(path + '/' + i, path + '/' + dic[name] + '.' + ext)
            print(f'{name} -> {dic[name]}')
        if name.endswith('.0'):
            if name[:-2] in dic:
                os.rename(path + '/' + i, path + '/' + dic[name[:-2]] + '.' + ext)
                print(f'{name} -> {dic[name[:-2]]}')
if __name__ == '__main__':
    conv(input())