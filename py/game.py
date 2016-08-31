from bge import logic
from bge import events
import numpy as np
import math

def vector2sphere(vector):
    """
    converts a 3d cartesian vector to a spherical vector
    """

    x,y,z = vector

    if (x,y,z) == (0,0,0):
        return (0,0,0)

    R = math.sqrt((x**2) + (y**2) + (z**2))
    theta = np.arccos(z/R) #[0, pi]
    # in the above unless R = 0, z is always less than R

    
#        phi = 0.5 * np.pi# if y > 0 else -0.5 * np.pi

    phi = np.arctan(y/x) 
    if x < 0:
        phi -= np.pi

    sign = (x + y + z) / abs(x + y + z)
    #R = R*sign

    return np.array((R, theta, phi))

def sphere2vector(sphere):
    """
    converts a 3d cartesian vector to a spherical vector
    """
    
    R, theta, phi = sphere
      
    x = R * np.sin(theta) * np.cos(phi)
    y = R * np.sin(theta) * np.sin(phi)
    z = R * np.cos(theta)
    
    return np.array((x, y, z))


class event():
    

    def __init__(self, decay_constant = 0.95)
        self.location = np.random.rand(3)
        self.radius = np.random.rand()
        self.decay_constant = decay_constant

    def __update__(self, ):
        if np.random.rand() > self.decay_constant:
            initiate_decay


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
        
    def get_distance_to_Event(self, ):
        dx, dy, dz = self.loc - Event.position
        dist = np.sqrt(dx**2 + dy**2 + dz**2)

        self.distance = dist
        
    if dist < Event_Radius:
            
    

scene = logic.getCurrentScene()


Event_Radius = 10

Fog_ = scene.objects['Fog']
FogWall_ = scene.objects['FogWall']
Fog_.localScale = Fog_.localScale * Event_Radius
FogWall_.localScale = FogWall_.localScale * Event_Radius

player = scene.objects['Player']





        
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

    # relative osition of player
    vector = player.position - Fog_.position
    displacement = vector.length
    
    # The angle of the fog wall should be the pi + the angle of the player
    # to the origin point.
    
    ax, ay, az = obj.localOrientation.to_euler()

    # Calculate rotation
    # ------------------
    R, theta, phi = vector2sphere(vector)
    obj.localOrientation = (ax, ay, phi + np.pi/2)

    # Calculate Position
    # ------------------
    
    # the fog wall should appear ~ 50 cm away from the player, allow the time
    # to blend into the pas, rather than be a solid wall (to explain why the
    # players nervous system / circulation continue to work)
    
    # Hard mode should force the player to regularly spin on the spot to allow
    # oxygen to pass into their lungs....

    x = (R - 1.5) * np.cos(phi)
    y = (R - 1.5) * np.sin(phi)
    
    obj.position = (x, y, 0)

    # Calculate Scale
    # ---------------
    
    # The radius of the fog wall is equal to the  R / displacement
    
    obj.localScale = [Event_Radius/displacement]*3
    
    if displacement < Event_Radius:
        obj.visible = 1
    else:
        obj.visible = 0
    
    #print(vector)


def Fog():
    cont = logic.getCurrentController()
    obj = cont.owner
    
    displacement = (player.position - obj.position).length
    
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
           
        motion.dLoc = [mx, my, 0.0]
        cont.activate(motion)
           
    Init()
    mouselook()
    Update()