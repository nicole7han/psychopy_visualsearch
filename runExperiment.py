 #!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division
from psychopy.data import TrialHandler, importConditions
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.iohub import ioHubExperimentRuntime
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
import pandas as pd
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# set up path
script_path = "C:\\home\\Experiments\\Nicole\\Gaze_AllFree\\Scripts"
data_path = "C:\\home\\Experiments\\Nicole\\Gaze_AllFree\\Intact"
stim_path = "C:\\home\\Experiments\\Nicole\\Gaze_AllFree\\Intact\\Stimuli"
os.chdir(script_path)


# Store info about the experiment session
expName = "target search (free)"
expInfo = {u'Eye Tracker': u'SRR_eyelink_std.yaml', u'Participant': u'', u'Age': u'', u'Gender': u'', u'Session_num' : u''}
expInfo['Date'] = data.getDateStr()  # add a simple timestamp

dlg = gui.DlgFromDict(dictionary=expInfo, fixed=['Eye Tracker','Date', 'Session_num'], order = ['Participant', 'Gender', 'Age'])
if dlg.OK == False:
    core.quit()  # user pressed cancel


# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = data_path + os.sep + u'data' + os.sep + '%s_%s_%s' %(expInfo['Participant'], expInfo['Session_num'], expInfo['Date'])
dataFile = pd.DataFrame(columns=[ "movie", "corr_ans", "resp", "click_pos_x", "click_pos_y"])


# An ExperimentHandler isn't essential but helps with data saving
#thisExp = data.ExperimentHandler(name=expName, version='',
#    extraInfo=expInfo, runtimeInfo=None,
#    originPath=None,
#    savePickle=True, saveWideText=True,
#    dataFileName=filename)
# save a log file for detail verbose info
#logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
#logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file


endExpNow = False  # flag for 'escape' or other condition => quit the exp


# Setup the Window
win = visual.Window((1280, 1024), fullscr=False, allowGUI=True, winType='pyglet',
        monitor='testMonitor', units ='pix', screen=0)
expInfo['FrameRate'] = win.getActualFrameRate()
frameDur = 1.0 / round(expInfo['FrameRate']) #get each frame duration (s)


""" Initialize Compoenents """
## instructions ##
instrText = visual.TextStim(win=win, name='instrText',
    text='Welcome to the Visual Search Experiment! In this experiment you are looking for a specific target person in videos. In each video, multiple individuals will look at a same location as gaze cues.\
        Sometimes they look at the target person. Or they look at a distractor person or an empty space. You need to make a decision on whether the target is present or absent.\
        If the target is present, you also need to click at the location at which the target was based on your memory.\
        \n\n 1) Stay fixated on the central fixation to start each video.\n\n 2) Feel free to make eye movements to find the target.\n\n 3) Click to respond.\n\n 4) Press space bar to continue',
    font='Arial', 
    units='pix', pos=[0, 0], height=30, wrapWidth=800, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1,
    depth=0.0)

## target example ##
targetimg1 = visual.ImageStim(
    win=win, image= script_path + '\\T1.jpg',
    name = 'target1', mask=None,
    pos=(0,300), size=[350,250],
    colorSpace='rgb', opacity=1
)
targetimg2 = visual.ImageStim(
    win=win, image= script_path + '\\T2.jpg',
    name = 'target2', mask=None,
    pos=(0,-150), size=[550,350],
    colorSpace='rgb', opacity=1,ori=-90
)
targetintructText2 = visual.TextStim(win=win, name='targetinstructText2',
    text='target person: Ian',
    font='Arial',
    units='pix', pos=[0, -450], height=40, wrapWidth=800, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0);


## cross fixation ##
cross = visual.GratingStim(
    win=win, name='cross',
    tex='sin', mask='cross',
    ori=0, pos=(0, 0), size=[20,20], sf=40, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)


## response screen ##
present_button = visual.Rect(win=win, name='present',
    pos=(0, 50),width = 300, height = 150,opacity = .8,
    lineColor=(0, 142/255.0, 18/255.0), lineColorSpace='rgb',
    fillColor=(0, 142/255.0, 18/255.0), fillColorSpace='rgb')
present_text = visual.TextStim(win=win, name='presentTxt',
    text='Present',
    font='Arial',
    units='pix', pos=[0, 50], height=30, wrapWidth=800, ori=0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    depth=0.0)
present_text2 = visual.TextStim(win=win, name='presentTxt2',
    text='Please click where the target was',
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=800, ori=0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    depth=0.0)

absent_button = visual.Rect(win=win, name='absent',
    pos=(0, -150),width = 300, height = 150,opacity = .8,
    lineColor=(183/255.0, 28/255.0, 0), lineColorSpace='rgb',
    fillColor=(183/255.0, 28/255.0, 0), fillColorSpace='rgb')
absent_text = visual.TextStim(win=win, name='absentTxt',
    text='Absent',
    font='Arial',
    units='pix', pos=[0, -150], height=30, wrapWidth=800, ori=0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    depth=0.0)

## Thanks screen ##
thanksText = visual.TextStim(win=win, name='thanksText',
    text='Thank you! You have completed this session. Press Space Bar to Exit.',
    font='arial',
    units='pix', pos=[0, 0], height=40, wrapWidth=800, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0)



maintain_fix_pix_boundary= 80.0 #66.0
eyetracker =False#will change if we get one!



""" Initialize Eyetracking """
if expInfo['Eye Tracker']:
    try:
        from psychopy.iohub import EventConstants,ioHubConnection,load,Loader
        from psychopy.iohub.util import NumPyRingBuffer
        from psychopy.data import getDateStr
        # Load the specified iohub configuration file converting it to a python dict.
        io_config=load(file(expInfo['Eye Tracker'],'r'), Loader=Loader)

        # Add / Update the session code to be unique. Here we use the psychopy getDateStr() function for session code generation
        session_info=io_config.get('data_store').get('session_info')
        session_info.update(code="S_%s"%(getDateStr()))
        session_info.update(name = expInfo['Participant'])

        # Create an ioHubConnection instance, which starts the ioHubProcess, and informs it of the requested devices and their configurations.
        io=ioHubConnection(io_config)

        iokeyboard=io.devices.keyboard
        mouse=io.devices.mouse
        if io.getDevice('tracker'):
            eyetracker=io.getDevice('tracker')
            win.winHandle.minimize()
            eyetracker.runSetupProcedure()
            win.winHandle.activate()
            win.winHandle.maximize()
            eyetracker.setRecordingState(True)

    except Exception, e:
       import sys
       print "!! Error starting ioHub: ",e," Exiting..."
       sys.exit(1)

    display_gaze=False
    x,y=0,0
    



""" Present Instruction """
ContinueThisRoutine = True
keyResponse = event.BuilderKeyResponse()
trialClock = core.Clock()
t = 0
while ContinueThisRoutine :
    t = trialClock.getTime()
    instrText.setAutoDraw(True)
    win.flip()
    
    theseKeys = event.getKeys()
    if "escape" in theseKeys:
        endExpNow = True
    if len(theseKeys) > 0: 
        instrText.setAutoDraw(False)
        ContinueThisRoutine = False
        break


""" Present Target Images """
ContinueThisRoutine = True
keyResponse = event.BuilderKeyResponse()
trialClock = core.Clock()
t = 0
while ContinueThisRoutine :
    t = trialClock.getTime()
    targetimg1.setAutoDraw(True)
    targetimg2.setAutoDraw(True)
    targetintructText2.setAutoDraw(True)
    win.flip()

    theseKeys = event.getKeys()
    if "escape" in theseKeys:
        endExpNow = True
    if len(theseKeys) > 0:
        targetimg1.setAutoDraw(False)
        targetimg2.setAutoDraw(False)
        targetintructText2.setAutoDraw(False)
        ContinueThisRoutine = False
        break


""" Set up and Present Trials in Random Order"""
movie_list = script_path +'\\moviePaths.xlsx'
#set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(movie_list),
    seed=None, name='trials')
#thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
io.createTrialHandlerRecordTable(trials)


""" Present Trials """
for thisTrial in trials:
    if thisTrial != None:
        eyetracker.setRecordingState(True)
        ## present cross before movie ##
        ContinueThisRoutine = True
        keyResponse = event.BuilderKeyResponse()
        while ContinueThisRoutine:
            cross.setAutoDraw(True)
            win.flip()
            theseKeys = event.getKeys(keyList=['space', 'c','escape'])
            if 'c' in theseKeys:
                eyetracker.runSetupProcedure()
                win.winHandle.activate()
                win.winHandle.maximize()
                    # check for quit:
            if "escape" in theseKeys:
                dlg = gui.Dlg(title='quit experiment?', screen=-1)
                dlg.addText('Are you sure you want to quit the experiment?')
                dlg.show()
                if dlg.OK:
                    dataFile.to_excel(filename+'.xlsx')
                    core.quit()
            if 'space' in theseKeys: #check broken fixation
                if eyetracker: # get gaze position
                    gpos=eyetracker.getLastGazePosition()
                    if type(gpos) in [list,tuple]:
                        x,y=gpos[0], gpos[1]
                        d = np.sqrt(x**2+y**2)
                        if "space" in theseKeys and d<maintain_fix_pix_boundary:
                            #if fixation is within boundary, stop cross, start present video
                            keyResponse.keys = theseKeys[-1]  # just the last key pressed
                            keyResponse.rt = keyResponse.clock.getTime()
                            cross.setAutoDraw(False)
                            ContinueThisRoutine = False
        
        ## present movie ##
        ContinueThisRoutine = True
        keyResponse = event.BuilderKeyResponse()
        movieName = thisTrial["movieName"]
        corrAns = thisTrial["corrAns"]
        mov = visual.MovieStim3(
            win=win, name='movie',
            filename=movieName,
            size=[1000,800]
        )
        t = 0
        trialClock = core.Clock()  # clock
        while ContinueThisRoutine == True:
            theseKeys = event.getKeys(keyList=['space'])
            t = trialClock.getTime()
            if t >= 0 and mov.status == 0:
                tStart = t
                print(tStart)
                io.sendMessageEvent("movie start")
                mov.setAutoDraw(True)
                win.flip()
            if t < 3 and mov.status == 1 and len(theseKeys) == 0:
                mov.setAutoDraw(True)
                win.flip()
            if t >= 3: # stop when video ends
                mov.setAutoDraw(False)
                tEnd = t
                print(tEnd)
                io.sendMessageEvent("movie end")
                ContinueThisRoutine = False
            if 'space' in theseKeys: # stop when participant responds
                tEnd = t
                print(tEnd)
                mov.setAutoDraw(False)
                ContinueThisRoutine = False
                io.sendMessageEvent("movie end")
            
            
        # click for response (yes + click where it was OR no)
        ContinueThisRoutine = True
        click_pos = None
        while ContinueThisRoutine == True:
            targetimg1.setAutoDraw(True)
            present_button.setAutoDraw(True)
            present_text.setAutoDraw(True)
            absent_button.setAutoDraw(True)
            absent_text.setAutoDraw(True)
            win.flip()
            mouse = event.Mouse()
            
            if mouse.isPressedIn(present_button):
                resp = 1
                #present background to ask subject to click where the target was
                mouse.clickReset()
                ContinueExtraRoutine = True
                while ContinueExtraRoutine:
                    mouse = event.Mouse()
                    targetimg1.setAutoDraw(False)
                    present_button.setAutoDraw(False)
                    present_text.setAutoDraw(False)
                    absent_button.setAutoDraw(False)
                    absent_text.setAutoDraw(False)
                    present_text2.setAutoDraw(True)
                    win.flip()
                    if mouse.getPressed()[0] == 1:
                        click_pos = mouse.getPos()
                        present_text2.setAutoDraw(False)
                        ContinueExtraRoutine = False
                ContinueThisRoutine = False
                newrow = {'movie':movieName, 'corr_ans':corrAns, 'resp':resp, 'click_pos_x':click_pos[0],'click_pos_y':click_pos[1] }
                dataFile = dataFile.append(newrow, ignore_index=True)
                
            if mouse.isPressedIn(absent_button):
                targetimg1.setAutoDraw(False)
                present_button.setAutoDraw(False)
                present_text.setAutoDraw(False)
                absent_button.setAutoDraw(False)
                absent_text.setAutoDraw(False)
                resp = 0
                ContinueThisRoutine = False
                newrow = {'movie':movieName, 'corr_ans':corrAns, 'resp':resp }
                dataFile = dataFile.append(newrow, ignore_index=True)
   
dataFile.to_excel(filename+'.xlsx')




""" Present thanksText """
ContinueThisRoutine = True
keyResponse = event.BuilderKeyResponse()
trialClock = core.Clock()
t = 0
while ContinueThisRoutine :
    t = trialClock.getTime()
    thanksText.setAutoDraw(True)
    win.flip()
    
    theseKeys = event.getKeys()
    if len(theseKeys) > 0: 
        thanksText.setAutoDraw(False)
        ContinueThisRoutine = False
        break

if eyetracker:
    eyetracker.setConnectionState(False)
    io.quit()

# make sure everything is closed down
win.close()
core.quit()
