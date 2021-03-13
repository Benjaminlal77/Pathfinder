class ScreenSettings:
    screen_width = 600
    screen_height = 675
    
    button_area_height = 75
    
    bg_color = (255,255,255)
    FPS = 60
        
class ButtonSettings:
    num_of_buttons = 3
    
    marginx = 10
    margin_area = (num_of_buttons * marginx) + marginx
    left_over_space = ScreenSettings.screen_width - margin_area
    
    width = int(left_over_space/num_of_buttons)
    height = 45
    size = (width, height)
        
class GridBoardSettings:
    class NodeSettings:
        obstacle_color = (0,0,0)
        color = (255, 255, 255)
        start_point_color = (0,255,0)
        end_point_color = (255,0,0)
        path_color = (0, 0, 255)
        
        width = 20
        height = 20
        
        border_size = 1
        border_color = (0, 0, 0)
        
    columns = 30
    rows = 30
    
    width = NodeSettings.width * columns 
    height = NodeSettings.height * rows
    