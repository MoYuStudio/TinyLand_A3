
import sys
sys.dont_write_bytecode = True
sys.path.append('./')

# from raylib import *
import pyray

import drivers

LocalsVar = locals()
yaml = drivers.yaml.yaml_driver.YamlDriver()
config = yaml.read(read_file='game/config.yml')
print(config)

pyray.init_window(config['window_size'][0],config['window_size'][1], config['window_title'])

a_i = pyray.load_image('game/assets/tile/1.png')
mask = pyray.load_image('game/assets/mask/landtile_mask.png')

pyray.set_window_icon(a_i)
pyray.set_target_fps(160)#160

a = pyray.load_texture('game/assets/tile/1.png')

pos = (-30,-30)

a_r = pyray.Rectangle(0,0,100,100)

while not pyray.window_should_close():
    
    # print(ImageAlphaMask(a,mask))
    
    # RenderTexture2D
    
    mouse_pos = (pyray.get_mouse_x(),pyray.get_mouse_y())
    
    print(pyray.check_collision_point_rec(mouse_pos,a_r))
    
    aC = pyray.Camera2D([0,0], mouse_pos, 0, 0)
    
    pyray.begin_mode_2d(aC)
    
    # print(GetTouchPosition(0))
    
    # if IsKeyPressed(MOUSE_BUTTON_LEFT):
    if pyray.is_mouse_button_down(0):
        pos = (- pyray.get_touch_x(), - pyray.get_touch_y())

    pyray.begin_drawing()
    
    pyray.clear_background((0,0,0,255))
    pyray.draw_texture_pro(a, (0,0,16,16), (0,0,64,64), pos, 0, (255,255,255,255))
    pyray.draw_text(b'TinyLand OpenGL Test', 190, 200, 20, (255,255,255,255))
    pyray.draw_fps(0,0)
    
    pyray.end_drawing()
    
    pyray.end_mode_2d()
    
pyray.close_window()