from bge import logic
from bge import events
import numpy as np
import math

def vector2sphere(vector):
    """
    converts a 3d cartesian vector to a spherical vector
    """
    
    x,y,z = vector
    
      
    R = math.sqrt((x**2) + (y**2) + (z**2))
    theta = np.arccos(z/R) #[0, pi]
    phi = np.arctan(y/x)
            # returns a value between [-pi/2, pi/2]
    
    sign = (x + y + z) / abs(x + y + z)
    R = R*sign
    
    if z < 0:
        theta += np.pi
    if y < 0:
        phi += np.pi
    if x < 0:
        phi += np.pi
 

    return np.array((R, theta, phi))

def sphere2vector(sphere):
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


#from bge import logic
#from bge import events


scene = logic.getCurrentScene()


Event_Radius = 10

Fog_ = scene.objects['Fog']
FogWall_ = scene.objects['FogWall']
Fog_.localScale = Fog_.localScale * Event_Radius
FogWall_.localScale = FogWall_.localScale * Event_Radius

player = scene.objects['Player']

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

        
def Camera():
    cont = logic.getCurrentController()
    obj = cont.owner

    
    def Init():
        logic.mouse.position = 0.5, 0.5
        if not 'init' in obj:
            obj['init'] = 1

    def mouselook():
        ###############
        # Looking
        ###############

        #The mouse input:
        # centre of screen = 0,0?
        #X = (logic.mouse.position[0] - 0.5)
        X, Y = logic.mouse.position
        Y = Y - 0.5
        
        x,y,z = obj.localOrientation.to_euler()
        #the X movement is applied to the rotation of the character itself
        obj.localOrientation= (x-Y, y, z)

        #and then the cursor is set back to the center of the screen.
        logic.mouse.position = 0.5, 0.5

    
    Init()
    mouselook()


def FogWall():
    cont = logic.getCurrentController()
    obj = cont.owner
        
    
    ax, ay, az = obj.localOrientation.to_euler()
    #print(obj.position)
    
    #calculate rotation
    vector = Fog_.position - player.position
    
    R, theta, phi = vector2sphere(vector)

    dx, dy, dz = sphere2vector((R, theta,phi))
    print(R, dx,dy,dz)
    obj.position = (dx,dy,dz)
    #print(vector)
    obj.localOrientation = (ax, ay, phi-(np.pi/2))


def Fog():
    cont = logic.getCurrentController()
    obj = cont.owner
    
    displacement = (obj.position - player.position).length
    
    if displacement < Event_Radius:
        obj.visible = 0
    else:
        obj.visible = 1

    # cast ray to player
    # scale = distance to player

def Player():
    cont = logic.getCurrentController()
    obj = cont.owner

   
    motion = cont.actuators['Motion']
   
    key = logic.keyboard.events
    kbleft = key[events.AKEY]
    kbright = key[events.DKEY]
    kbup = key[events.WKEY]
    kbdown = key[events.SKEY]
   
    def Init():
        logic.mouse.position = 0.5, 0.5
        if not 'init' in obj:
            obj['init'] = 1
   
   
    def mouselook():
        ###############
        # Looking
        ###############

        #The mouse input:
        # centre of screen = 0.5,0.5?
        X, Y = logic.mouse.position
    
        X = X - 0.5
        #the X movement is applied to the rotation of the character itself
        obj.applyRotation([0, 0, -X])

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
           
        pos = obj.position    # Get the Player's current position
        topos = pos.copy()    # Make a copy of the Player's current position
        topos.x += mx        # And offset the copy by the movement value for the X-axis
       
        if obj.rayCast(topos, pos, 0, 'wall', 1, 1)[0] != None:    # We just collided with something on the X-axis
            mx = 0    # So stop movement on the X-axis
           
        pos = obj.position    # Get the Player's current position
        topos = pos.copy()    # Make a copy of the Player's current position
        topos.y += my        # And offset the copy by the movement value for the Y-axis

        if obj.rayCast(topos, pos, 0, 'wall', 1, 1)[0] != None:    # We just collided with something on the Y-axis
            my = 0  # So stop movement on the Y-axis
       
        motion.dLoc = [mx, my, 0.0]
        cont.activate(motion)
           
    Init()
    mouselook()
    Update()