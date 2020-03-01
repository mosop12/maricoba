import sys , hashlib , zlib , time , random , os , time

"""
__Author__  = matludin
__Name__    = hash generator
__version__ = 3.4.1
__Code__    = python
__Github__  = https://github.com/mosop12
__Date__    = 21 - 4 - 2018
"""

if sys.platform == "linux2" or sys.platform == "linux":
	B = "\033[34;1m"
	W = "\033[0m"
	C = "\033[36;1m"
	G = "\033[32;1m"
	R = "\033[31;1m"
	Y = "\033[33;1m"
	X = "\033[35;1m"

	rand = (B,C,G,R,Y,X)
	P = random.choice(rand)

elif sys.platform == "win32":
	B = ''
	W = ''
	C = ''
	G = ''
	R = ''
	P = ''
	Y = ''
	X = ''

try:
	import passlib , progressbar
except ImportError:
	print (R+"\n["+W+"!"+R+"] "+G+"module "+W+"passlib or progressbar"+G+"not installed"+W+"\n")
	sys.exit()

os.system("clear")
print (P+"\n....................................................................")
print (P+".##.....##....###.....######..##.....##..######...########.##....##.")
print (P+".##.....##...##.##...##....##.##.....##.##....##..##.......###...##.")
print (P+'.##.....##..##...##..##.......##.....##.##........##.......####..##.')
print (P+".#########.##.....##..######..#########.##...####.######...##.##.##.")
print (P+".##.....##.#########.......##.##.....##.##....##..##.......##..####.")
print (P+".##.....##.##.....##.##....##.##.....##.##....##..##.......##...###.")
print (P+".##.....##.##.....##..######..##.....##..######...########.##....##.")
print (P+"........................."+W+" Hash Generator "+P+"...........................\n")

try:
	x = raw_input(B+"["+W+"+"+B+"] "+G+"String "+B+": "+W)
except NameError:
	print (R+"\n["+W+"!"+R+"] "+G+"use "+W+"python2.7\n")
	quit()

print (B+"["+W+"!"+B+"] "+G+"Generate Hash "+W+". . . ."+G+" Please Wait !!!"+W)
time.sleep(0.5)
