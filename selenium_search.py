# Created by Jan Rummens at 8/09/2020
from nemonet.engines.graph import Graph
from nemonet.engines.sequencer import Sequences
from nemonet.seleniumwebdriver.commands import Command
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#create a selenium webdriver
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options)
driver.maximize_window()

#execute the graph scenario
graph = Graph()
graph.build("selenium-dev")
seqences = Sequences( graph )
commands = Command( driver )
commands.executeSequences(seqences, graph)

#close the browser
driver.close()



