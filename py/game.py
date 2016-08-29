from bge import logic
from bge import events
import numpy as np
#---------------------------
# Utilities
def vector2sphere(vector):
    """
    converts a 3d cartesian vector to a spherical vector
    """
    
    x,y,z = vector
    
      
    R = np.sqrt((x**2) + (y**2) + (z*2))
    theta = np.arctan(y/x)
    phi = np.arcsin(z/R)
    
    sign = x + y + z / abs(x + y + z)
    R = R*sign
    theta = abs(theta)
    phi = abs(phi)   

    return np.array((R, theta, phi))

def sphere2vector(sphere):
    print('gets run')
    """
    converts a 3d cartesian vector to a spherical vector
    """
    
    R,theta,phi = sphere
      
    x = R * np.sin(theta) * np.cos(phi)
    y = R * np.sin(theta) * np.sin(phi)
    z = R * np.cos(theta)
    
    return np.array((x, y, z))

class physobj():
    
    ###dt = 0.001
    
    def __init__(self, loc = [0,0,0], v = [0,0,0], mass = 1):
        self.location = np.array(loc)
        self.mass = mass
        self.velocity = np.array(v)
        
    def applyForce(self, force, dt = 0.01):
        
        force = np.array(force)
        velocity = self.velocity
        mass = self.mass
        
        impulse = force * dt
        
        momentum = velocity * mass
        momentum = momentum + impulse
        velocity = momentum / mass

        self.velocity = velocity
    
    def update(self, dt = 0.01):
        loc = self.location
        v = self.velocity
        
        self.location = loc + (v*dt)


#Game initialisation        
logic.mouse.position = 0.5, 0.5        
        
scene = logic.getCurrentScene()

Camera = scene.objects['Camera']
Player = scene.objects['Player']
Fog = scene.objects['Fog']

# Controls

key = logic.keyboard.events
kbleft = key[events.AKEY]
kbright = key[events.DKEY]
kbup = key[events.WKEY]
kbdown = key[events.SKEY]

print('run')
        
def Camera_mouselook():
    

    #The mouse input:
    # centre of screen = 0.5,0.5
    X, Y = logic.mouse.position
    Y = Y - 0.5
    # original orientation
    x,y,z = Camera.localOrientation.to_euler()
    
    #Y axis mouse movement shifts the camera's X axis
    Camera.localOrientation= (x-Y, y, z)
    #and then the cursor is set back to the centre of the screen.
    logic.mouse.position = 0.5, 0.5

def Fog_shrink():
    
    displacement = Fog.position - Player.position


    # cast ray to player
    # scale = distance to player

def Player_move():

    
    def mouselook():
        ###############
        # Looking
        ###############

        #The mouse input:
        # centre of screen = 0.5,0.5?
        X, Y = logic.mouse.position
    
        X = X - 0.5
        #the X movement is applied to the rotation of the character itself
        Player.applyRotation([0, 0, -X])

        #and then the cursor is set back to the center of the screen.
        logic.mouse.position = 0.5, 0.5
    
   
    def Update():
   
        movespd = 0.2
        mx = 0.0
        my = 0.0
       
        if kbleft > 0:
            mx = -movespd
        elif kbright > 0:
            mx = movespd
       
        if kbup > 0:
            my = movespd
        elif kbdown > 0:
            my = -movespd
           
        Player.position = [mx, my, 0.0]
           
    
    mouselook()
    Update()