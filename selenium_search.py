# Created by Jan Rummens at 8/09/2020
from nemonet.engines.graph import Graph
from nemonet.engines.sequencer import Sequences
from nemonet.seleniumwebdriver.commands import Command
from selenium import webdriver

#create a selenium webdriver
options = webdriver.ChromeOptions()
capabilities = options.to_capabilities()
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=capabilities)
driver.maximize_window()

#execute the graph scenario
graph = Graph()
graph.build("selenium-dev")
seqences = Sequences( graph )
commands = Command( driver )
commands.executeSequences(seqences, graph)

#close the browser
driver.close()



