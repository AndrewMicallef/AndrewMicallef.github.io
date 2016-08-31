from bge import logic
from bge import events


scene = logic.getCurrentScene()

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

def Fog():
    cont = logic.getCurrentController()
    obj = cont.owner
    
    player = scene.objects['Player']
    displacement = obj.position - player.position
    [print(i) for i in dir(displacement)]
    quit()

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