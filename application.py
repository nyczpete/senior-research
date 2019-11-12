# 
# Senior Research Project
# Tan Dung Luong
# Suntae Parks
#

from midi import *
from music import * 

# create midi input
midiIn = MidiIn()     

# create display
display = Display("MIDI App - Senior Research", 1024, 768, 0, 0, Color.cyan)

# coordinates
x = 0
y = 0

def printNote(eventType, channel, data1, data2):
   # eventType: 144 = start, 128 = stop
   # channel: only one channel for the moment, channel 0
   # data 1 = pitch number
   # data 2 = volume level
   global x
   global y
   print "Pitch = ", MIDI_PITCHES[data1]
   note = TextField(MIDI_PITCHES[data1])
   if(x >= 900):
      x = 0
      y += 40
   display.add(note, x, y)
   x += 40
   
# TODO: map pitches to images on staff lines for GUI

# TODO: Write method to score user on matching requested notes

midiIn.onNoteOn(printNote)