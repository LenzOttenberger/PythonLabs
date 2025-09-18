ip = str(input('Enter ip: '))
checkIpFormat = ip.split('.')
if(len(checkIpFormat) != 4):
    print(f'{ip} is not correct IP adress :<')
else:
    first = int(checkIpFormat[0])
    second = int(checkIpFormat[1])
    third = int(checkIpFormat[2])
    fourth = int(checkIpFormat[3])
    if (first >= 0 and first <= 256) and (second >= 0 and second <= 256) and (third >= 0 and third <= 256) and (fourth >= 0 and fourth <= 256):
        print(f'{ip} is correct <3')
    else:
        print(f'{ip} is incorrect :<')


