from bge import logic
from bge import events
import numpy as np
import math

def length(vector):
    return np.linalg.norm(vector)

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

    if x == 0:
        phi = np.pi/2 * np.sign(y)
    else:
        phi = np.arctan(y/x) 
    
    if x < 0:
        phi -= np.pi 

    if x == 0: x=1
    if y == 0: y=1
    if z == 0: z=1
    
    sign = ((x/abs(x)) + (y/abs(y)) + (z/abs(z)) ) / 3
    R = R * sign

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

'''
class event():
    

    def __init__(self, decay_constant = 0.95)
        self.location = np.random.rand(3)
        self.radius = np.random.rand()
        self.decay_constant = decay_constant

    def __update__(self, ):
        if np.random.rand() > self.decay_constant:
            initiate_decay
'''

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
        
    #def get_distance_to_Event(self, ):
    #    dx, dy, dz = self.loc - Event.position
    #    dist = np.sqrt(dx**2 + dy**2 + dz**2)
    #
    #    self.distance = dist
        
    #if dist < Event_Radius:
            
    

scene = logic.getCurrentScene()


Event_Radius = 10

Fog_ = scene.objects['Fog']
Fog_.localScale = Fog_.localScale * Event_Radius


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

    x = (abs(R) - 1.5) * np.cos(phi)
    y = (abs(R) - 1.5) * np.sin(phi)
    
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

    key = logic.keyboard.events
    kbleft = key[events.AKEY] > 0
    kbright = key[events.DKEY] > 0
    kbup = key[events.WKEY] > 0
    kbdown = key[events.SKEY] > 0
   
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
        
        Event_Pos = np.array(Fog_.position)
        pos_0 = np.array(player.position)
        #restrict motion
        displacement = (pos_0 - Event_Pos).length
        x,y,z = pos_0
        ax, ay, az = player.localOrientation.to_euler()
        
        if any((kbup, kbdown, kbleft, kbright)):
            spd = 0.2

            # bug, using two keys at a time still gives positive motion
            if not (kbright and kbleft):
                az += kbright*2*np.pi 
                az += kbleft*np.pi
                
            if not (kbup and kbdown):
                az += ((kbup - kbdown) * np.pi/2)

            motion = spd * np.cos(az), spd * np.sin(az), 0.0
            motion = np.array(motion)
            
            pos_1 = pos_0 + motion
            
            if displacement < Event_Radius:
                
                R0 = np.linalg.norm(Event_Pos - pos_0)
                R1 = np.linalg.norm(Event_Pos - pos_1)
                
                if R1 > R0:
                    R, theta, phi = vector2sphere(motion)
                    
                
                
            print(displacement)
             
            player.position = np.array(player.position) + np.array(motion) 
           
    Init()
    mouselook()
    Update()