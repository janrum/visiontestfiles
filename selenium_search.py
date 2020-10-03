# Created by Jan Rummens at 8/09/2020
from nemonet.engines.graph import Graph
from nemonet.engines.sequencer import Sequences
from nemonet.seleniumwebdriver.commands import Command
from nemonet.screencast.recording import ScreenRecorder
from selenium import webdriver

#start screenrecorder
screenRecorder = ScreenRecorder()
screenRecorder.start()

#create a selenium webdriver
driver = webdriver.Chrome()
driver.maximize_window()

#execute the graph scenario
graph = Graph()
graph.build("selenium-dev")
seqences = Sequences( graph )
commands = Command( driver )
commands.executeSequences(seqences, graph)

#close the browser
driver.close()
screenRecorder.stop()