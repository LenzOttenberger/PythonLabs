inp = int(input('Enter time in seconds: '))
minutes = inp // 60
inp -= minutes*60
seconds = inp
print(f'{minutes} min and {seconds} sec')