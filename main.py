import json; import cv2; import mss; import time; import threading; import numpy as np
def wjf(dat):
    with open('s.json', "w") as f:
        json.dump(dat, f, indent=2)
def rjf():
    try:
        with open('s.json', "r") as f:
            return json.load(f)
    except (FileNotFoundError,  json.JSONDecodeError):
        d = {'fps': 60, 'format': "mp4"}
        wjf(d)
        return d
rjf()
def recT(fln, f):
    global isrc
    if foo=="avi": fcc=cv2.VideoWriter_fourcc(*"XVID")
    else: fcc=cv2.VideoWriter_fourcc(*"mp4v")
    o=cv2.VideoWriter(fln, fcc, f, (1920, 1080))
    with mss.mss() as ms:
        mon=ms.monitors[1]
        while isrc:
            st=time.time()
            img=ms.grab(mon)
            fr=cv2.cvtColor(np.array(img), cv2.COLOR_BGRA2BGR)
            fr=cv2.resize(fr, (1920, 1080))
            o.write(fr)
            time.sleep(max(0, (1.0/f)-(time.time()-st)))
        o.release()
def rec():
    global isrc; global foo
    dd=rjf()
    f=int(dd['fps'])
    foo=dd['format']
    fln=input("Filename? =$ ")
    fln+="."+foo
    isrc=True
    t=threading.Thread(target=recT, args=(fln, f)); t.start()
    print("REC...")
    input("ENTER TO STOP")
    isrc=False
    print("STOPPIN")
    t.join()
    print("SAVED")
def s():
    while True:
        print("=---SETTINGS---=\nF (FPS)\nE (Format) mp4, avi\nB (Back)\n=--------------=")
        n=input("=$ ").lower()
        if n=="f":
            wf=input("=$ ")
            try: int(wf)
            except ValueError: print("Put a number here bru"); wf=60
            i=rjf(); i['fps']=wf; wjf(i); mm()
        if n=="e":
            wf=input("=$ ")
            i=rjf(); i['format']=wf; wjf(i); mm()
        if n=="b": mm()
        else: break
def mm():
    print("=---ScreenREC---=\nR (RECORD)\nS (SETTINGS)\nQ (QUIT)\n=--AP COMP SCI--=")
    n = input("=$ ").lower()
    if n=="r": rec()
    elif n=="s": s()
    elif n=="q": exit()
    else: print("WRSEL")
mm()
