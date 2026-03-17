from pyscreenrecorder import ScreenRecorder
#import keyboard
def rec():
    recorder = ScreenRecorder()
    recorder.start_recording("DIH.mp4", fps=60)
def s():
    print("=---SETTINGS---=\n1)FPS\n2)WP")
print("ScreenREC\nR (RECORD)\nS (SETTINGS)\nQ (QUIT)\nAP COMP SCI")
n = input("=$ ").lower()
if n=="r": rec()
elif n=="s": s()
elif n=="Q": exit()
else: print("WRSEL")
