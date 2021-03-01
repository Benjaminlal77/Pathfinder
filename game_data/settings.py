class ScreenSetings:
    screen_width = 600
    screen_height = 675
    
    bg_color = (255,255,255)
    FPS = 50
    
class GameSettings:
    pass
    
class GridBoardSettings:
    class BoxSettings:
        color = (255, 255, 255)
        width = 20
        height = 20
        
        border_size = 1
        border_color = (0, 0, 0)
        
    columns = 30
    rows = 30
    
    width = BoxSettings.width * columns 
    height = BoxSettings.height * rows
    