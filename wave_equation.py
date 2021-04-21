import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# y = f(x,t) gives us the wave equation
y=np.zeros((1000,1000),dtype=float)
x=np.linspace(-10,10,1000)
del_x=x[1]-x[0]
del_t=0.01
c=1.0

# alpha-parameter
a=(c*del_t/del_x)**2

# The evolution matrix
M=np.diag(a*np.ones(999,dtype=float),-1)-2.*(1-a)*np.diag(np.ones(1000,dtype=float),0)+np.diag(a*np.ones(999,dtype=float),1)

# In order to solve the wave equation we need boundary conditions and initial conditions. I will write the code again.

# Initialization this is the trickies part And I have no idea how to initialize the wavefunction.

def initialize_one(t):
    yi=np.zeros(1000)
    for i in range(1000):
        if t[i]<np.pi and t[i]>0:
            yi[i]=np.sin(t[i])
        else:
            yi[i]=0.01
    return yi

def initialize_two(t):
    return np.sin(t)

# y is initialized to for (x,0)
y[0]=initialize_two(x)
y[1]=y[0]

# Also the boundary conditions
#y[:,0]=0.0
#y[:,-1]=0.0

# Evolution of wave-function in time
for j in range(1,999,1):
    y[j+1]=np.dot(M,y[j]) - y[j-1]

# After execution of this loop we have our wave function

# Now visualizing the wave function
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()
ax.set_xlim(-15,15)
ax.set_ylim(-15,15)

wave_function, = plt.plot([],[],color='blue')

def visualizing_the_wave_function(t):
	wave_function.set_data(x,y[t])

ani = animation.FuncAnimation(fig,visualizing_the_wave_function,frames=range(1000),blit=False,repeat=True)
plt.show()
