import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import time
from matplotlib import style 


style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):

	pull_data = open('twitter.txt' , 'r').read()
	lines = pull_data.split("\n")

	xar , yar = [] , []

	x , y = 0 , 0

	for l in lines[-200:] :
		x += l

		if 'pos' in l:
			y += 1
		elif  'neg' in l:
			y -= 1

		xar.append(x)
		yar.append(y)

	ax1.clear()
	ax1.plot(xar , yar)

ani = animation.FuncAnimation(fig , animate  , interval = 1000)
plt.show()

