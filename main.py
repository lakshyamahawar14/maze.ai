import pygame
import numpy as np
from functions.screen import Screen
from functions.game import Game
from functions.player import Player
from functions.gui import GUI
from functions.input import Input
from functions.rules import Rules
from functions.writecsv import insertData
from functions.models import Models
from functions.solvers import Solvers
from functions.generators import Generators
from functions.params import Params

pygame.init()

screenObj = Screen()
modelsObj = Models()
__random_level = np.random.randint(9,26)
generatorsObj = Generators()
paramsObj = Params()
solversObj = Solvers()
gameObj = Game((__random_level, __random_level), modelsObj, generatorsObj, solversObj, paramsObj)
guiObj = GUI()
playerObj = Player(screenObj, gameObj, guiObj)
inputObj = Input(gameObj)
rulesObj = Rules()

while True:
	gameObj.loadGame(screenObj)
	guiObj.drawReset(screenObj)
	guiObj.drawRandom(screenObj)
	guiObj.drawRowInput(screenObj, inputObj)
	guiObj.drawGenerate(screenObj)
	guiObj.drawDifficultyInput(screenObj, inputObj)
	guiObj.drawRate(screenObj)
	guiObj.drawSolution(screenObj)
	guiObj.drawQuit(screenObj)
	guiObj.drawVisited(screenObj, gameObj)
	guiObj.drawPlayer(screenObj, playerObj)
	guiObj.drawMaze(screenObj, gameObj)
	if solversObj.isSolutionDisplayed == True:
		gameObj.isGameFinish = True
		solversObj.toggleSolutionDisplayed()
	if gameObj.isGameOver == True:
		guiObj.drawGameOver(screenObj)
		guiObj.drawPlayAgain(screenObj)
	elif gameObj.isGameFinish == True:
		guiObj.drawFinish(screenObj)
		guiObj.drawPlayAgain(screenObj)
	else:
		guiObj.drawHeadText(screenObj)
		guiObj.drawLevelText(screenObj, gameObj)
		guiObj.drawMaze(screenObj, gameObj)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		if event.type == pygame.KEYDOWN and gameObj.isGameOver == False and gameObj.isGameFinish == False:
			playerObj.movePlayer(event.key, screenObj, gameObj, guiObj)
		if event.type == pygame.KEYDOWN and inputObj.isRowInputFocus == True:
			inputObj.takeRowInput(event.key)
		if event.type == pygame.KEYDOWN and inputObj.isDifficultyInputFocus == True:
			inputObj.takeDifficultyInput(event.key)
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			if(rulesObj.isResetClicked(pos) == True):
				gameObj.resetGame(screenObj, playerObj, guiObj)
			if(rulesObj.isSolutionClicked(pos) == True):
				solversObj.solutionPath = solversObj.backtrackingSolver(generatorsObj.generatorObj)
				solversObj.toggleSolutionDisplayed()
				solversObj.insertSolutionPath(solversObj, gameObj)
			if(rulesObj.isPlayAgainClicked(gameObj.isGameOver or gameObj.isGameFinish, pos, screenObj) == True or rulesObj.isRandomClicked(pos) == True):
				gameObj = gameObj.startNewGame(screenObj, playerObj, guiObj, inputObj, modelsObj, generatorsObj, solversObj, paramsObj)	
				inputObj = Input(gameObj)
			if(rulesObj.isRowInputClicked(pos) == True or (rulesObj.isRowInputClicked(pos) == False and inputObj.isRowInputFocus == True)):
				inputObj.toggleRowInputFocus()
			if(rulesObj.isDifficultyInputClicked(pos, screenObj) == True or (rulesObj.isDifficultyInputClicked(pos, screenObj) == False and inputObj.isDifficultyInputFocus == True)):
				inputObj.toggleDifficultyInputFocus()
			if(rulesObj.isRateClicked(pos, screenObj) == True):
				gameObj.setLevel(inputObj.difficultyInput)
				insertData(paramsObj, gameObj, solversObj, generatorsObj.generatorObj, inputObj.difficultyInput)
			if(rulesObj.isGenerateClicked(pos) == True):
				gameObj = gameObj.startNewGame(screenObj, playerObj, guiObj, inputObj, modelsObj, generatorsObj, solversObj, paramsObj, (inputObj.rowInput, inputObj.rowInput))
				inputObj = Input(gameObj)
			if(rulesObj.isQuitClicked(pos, screenObj) == True):
				pygame.quit()
				quit()
			

	pygame.display.update()
