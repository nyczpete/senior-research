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
   # time since last note was played
   timeSinceLast = (datetime.now() - currentTime).total_seconds()
   # set current time to now
   currentTime = datetime.now()
   # tracks current note needed to be played
   if(currentNote < len(listOfNotes)):
      if(x >= 900):
         x = 0
         y += 70
      if(listOfNotes[currentNote] == MIDI_PITCHES[data1]):
         score += 1
         answer = TextField("Correct")
      else:
         answer = TextField(MIDI_PITCHES[data1] + " Incorrect")
     
      # displays if the correct note was played, if not, tells which note was played and incorrect message
      display.add(answer, x, y)
      y += 20
      # displays time since last note was played
      time = TextField(str(timeSinceLast) + " s")
      display.add(time, x, y)
      y -= 20
      x += 80
      
      currentNote += 1
   # if end of list, end and score
   else:
      x = 0
      y += 70
      endcard = TextField("End")
      endcard2 = TextField("Score: " + str(score) + " out of " + str(len(listOfNotes)), 20)
      display.add(endcard, x, y)
      y += 40
      display.add(endcard2, x, y)
   print "Pitch = ", MIDI_PITCHES[data1]

# sets up notes to be played
def displayNotesToPlay(numberOfNotesToPlay):
   global x
   global y
   # display instructions
   instruction = TextField("Play the following notes:", 20)
   display.add(instruction)
   y += 40
   global listOfNotes
   # creates random notes to be played
   for noteToPlay in range(numberOfNotesToPlay):
      if(x >= 900):
         x = 0
         y += 70
      note = MIDI_PITCHES[random.randint(21, 108)]
      listOfNotes.append(note)
      noteDisplay = TextField(note) 
      display.add(noteDisplay, x, y)
      x += 80
   # resets coordinates
   x = 0
   y = 60

# start of program
displayNotesToPlay(50)
midiIn.onNoteOn(printNote)