# 
# Senior Research Project
# Tan Dung Luong
# Suntae Parks
#

from midi import *
from music import * 

midiIn = MidiIn()     

def printNote(eventType, channel, data1, data2):
   # eventType: 144 = start, 128 = stop
   # channel: only one channel for the moment, channel 0
   # data 1 = pitch number
   # data 2 = volume level
   print "Pitch = ", MIDI_PITCHES[data1]
   
# TODO: map pitches to images on staff lines for GUI

# TODO: Write method to score user on matching requested notes

midiIn.onNoteOn(printNote)