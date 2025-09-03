class Settings:
    def __init__(self):
        self.screen_width = 800             #screen width (in pixels)
        self.screen_height = 600            #screen height (in pixels)
        self.bg_color = "BLACK"             #background color of screen

        self.bullet_speed = 2               #how fast the bullet goes upwards
        self.bullet_width = 3               #how wide the bullet is (in pixels)
        self.bullet_height = 15             #how tall the bullet is (in pixels)
        self.bullet_color = (245,239,66)    #color of bullet (yellow)
        self.bullets_allowed = 3            #amount of bullets allowed on screen at once

        self.player_image = "ship.bmp"      #image for player ship
        self.player_speed = 3               #max speed of the player

        self.alien_direction = 1            #1 = right, -1 = left
        self.alien_speed = 2             #how fast the aliens move
        self.fleet_drop = 10                #how far the fleet goes down each time it drops
