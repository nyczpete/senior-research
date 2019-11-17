# 
# Senior Research Project Part 2
# Tan Dung Luong
# Suntae Park
#

from midi import *
from music import *
from gui import *
import random
from datetime import *

# create midi input
midiIn = MidiIn()  

# create display
display = Display("MIDI App - Senior Research", 1024, 768, 0, 0, Color.white)  

# coordinates
x = 0
y = 0

#saved list of notes to be played
listOfNotes = []

#track current note and score
currentNote = 0
score = 0

#get current time
currentTime = datetime.now()

def printNote(eventType, channel, data1, data2):
   # eventType: 144 = start, 128 = stop
   # channel: only one channel for the moment, channel 0
   # data 1 = pitch number
   # data 2 = volume level
   global currentNote
   global listOfNotes
   global score
   global x
   global y
   global currentTime
   timeSinceLast = (datetime.now() - currentTime).total_seconds()
   currentTime = datetime.now()
   if(currentNote < len(listOfNotes)):
      if(x >= 900):
         x = 0
         y += 70
      if(listOfNotes[currentNote] == MIDI_PITCHES[data1]):
         score += 1
         answer = TextField("Correct")
      else:
         answer = TextField(MIDI_PITCHES[data1] + " Incorrect")
      currentNote += 1
      display.add(answer, x, y)
      y += 20
      time = TextField(str(timeSinceLast) + " s")
      display.add(time, x, y)
      y -= 20
      x += 80
   else:
      x = 0
      y += 70
      endcard = TextField("End")
      endcard2 = TextField("Score: " + str(score) + " out of " + str(len(listOfNotes)), 20)
      display.add(endcard, x, y)
      y += 40
      display.add(endcard2, x, y)
   print "Pitch = ", MIDI_PITCHES[data1]
   
# TODO: Write method to score user on matching requested notes

def displayNotesToPlay(numberOfNotesToPlay):
   global x
   global y
   instruction = TextField("Play the following notes:", 20)
   display.add(instruction)
   y += 40
   global listOfNotes
   for noteToPlay in range(numberOfNotesToPlay):
      if(x >= 900):
         x = 0
         y += 70
      note = MIDI_PITCHES[random.randint(21, 108)]
      listOfNotes.append(note)
      noteDisplay = TextField(note) 
      display.add(noteDisplay, x, y)
      x += 80

displayNotesToPlay(30)
x = 0
y = 60
midiIn.onNoteOn(printNote)