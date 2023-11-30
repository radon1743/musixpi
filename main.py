import dearpygui.dearpygui as dpg
import dearpygui.demo as demo
from pygame import mixer
import pygame as pg
global x
x=0


mixer.init()

def Select():
    return f'10,000 Hours.mp3'
def Play():
    global x
    if x==0:
        song= Select()
        mixer.music.load(song)
        mixer.music.play()
        x=1
        
        
    else:
        mixer.music.unpause()
    
def Pause():
    mixer.music.pause()


def master_volume(sender):
    vol=dpg.get_value(sender)
    mixer.music.set_volume(float(vol/100))
    
def move(sender):
    pointer=dpg.get_value(sender)
    try:
        mixer.music.play(start=pointer)
    except pg.error:
        print("end")
    


dpg.create_context()
dpg.create_viewport(title='TEST', width=600, height=600)
vol_tag = dpg.generate_uuid()




with dpg.window(label="MP3",width=1000, height=600):
    
    dpg.add_button(label="|>", callback=Play, tag="play")
    with dpg.tooltip("play"):
        dpg.add_text("Play")
        
        
    dpg.add_button(label="||", callback=Pause, tag="pause")
    with dpg.tooltip("pause"):
        dpg.add_text("Pause")
    
    dpg.add_slider_int(label="Volume",width=100,default_value=45,
                       tag="VOl",callback=master_volume)
    
    len_o_song=pg.mixer.Sound(Select()).get_length()
    print(len_o_song)
    dpg.add_slider_int(label="Time",width=400,callback=move, max_value=int(len_o_song))
    

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
mixer.quit()
