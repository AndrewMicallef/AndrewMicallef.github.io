    def xy (x, y) 
        this.x = x
        this.y = y
    
    
    def object (loc = [0,0], v = [0,0], mass = 1) 
        this.loc = new xy(loc)
        this.mass = mass
        this.v = new xy(v)
        
        this.p = def() 
            p = new xy([0, 0])
            p.x = this.x * this.mass
            p.y = this.y * this.mass
        
        
        this.updatepos = def (impulse) 
            this.p.x = this.p.x + impulse.x
            this.p.y = this.p.y + impulse.y
           
            this.v.x = this.p.x / this.mass
            this.v.y = this.p.y /this.mass

            this.loc.x += this.v.x
            this.loc.y += this.v.y
        
    
    
    
    Ball = new object([150,150], [0,0], 1)
    
    var v_max = 2 # max velocity
    
    var impulse = new xy([0,0])
    
    console.log("velocty is " + Ball.v)
    console.log("momentum is " + Ball.p.x + Ball.p.y)
    
    
    # The momentum principle:
    # -----------------------
    # 
    # An object has momentum. Momentum is determined
    # as the mass of the object multiplied by the object's 
    # velocity.
    # 
    # py = vy * mass
    # px = px * mass
    # 
    # Force acts on momentum. The impulse is the force over dt.
    # 
    # p = p + F/dt
    #
    
    var xmlns = "http:#www.w3.org/2000/svg"
    
    # Quest: Find a way to land the traveller in the world
    var traveller = document.createElementNS(xmlns, "circle")      
    
    traveller.setAttributeNS(null,"x",50)
    traveller.setAttributeNS(null,"y",50)
    traveller.setAttributeNS(null,"r",50)
    traveller.setAttributeNS(null,"fill", "black")
    document.documentElement.appendChild(traveller)
    
    # This def is called on page load.

    def drawGameSVG() 

        # Play the game until the player stops.
        gameLoop = setInterval(drawBall, 1)

        # Add keyboard listener.
        window.addEventListener('keydown', whatKey, true)
        
    

    def drawBall() 
        Ball.updatepos(impulse)
        impulse.x = 0
        impulse.y = 0
        
        # Change the player location.
        player.setAttribute("cx", Ball.loc.x)
        player.setAttribute("cy", Ball.loc.y)
    
    # Get key press.
    def whatKey(evt) 

        switch (evt.keyCode) 
            # Left arrow.
            case 37:
            impulse.x = -1
            break
            # Right arrow.
            case 39:
            impulse.x = 1
            break
            #Up arrow
            case 38:
            impulse.y = -1
            break
            #Down arrow
            case 40:
            impulse.y = 1
            break
