from raylib import *

InitWindow(800, 450, b"Hello Raylib")
SetTargetFPS(60)

SetCameraMode(Camera2D, CAMERA_ORBITAL)

while not WindowShouldClose():
    UpdateCamera(Camera2D)
    
    BeginDrawing()
    
    ClearBackground((255,255,255))
    DrawText(b"Hellow World", 0, 0, 0, (0,255,255))
    
    EndDrawing()
CloseWindow()
