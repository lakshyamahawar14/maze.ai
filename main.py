import pygame
import numpy as np
from functions.screen import Screen
from functions.colors import RED, BLACK, BLUE, GREEN, PINK, YELLOW, WHITE
from functions.game import Game
from functions.player import Player
from functions.gui import GUI
from functions.input import Input
from functions.rules import Rules

pygame.init()

screenObj = Screen()
gameObj = Game((np.random.randint(3, 5), np.random.randint(3, 10)))
guiObj = GUI()
playerObj = Player(screenObj, gameObj, guiObj)
inputObj = Input()
rulesObj = Rules()

while True:
	gameObj.loadGame(screenObj)
	guiObj.drawReset(screenObj)
	guiObj.drawRandom(screenObj)
	guiObj.drawRowInput(screenObj, gameObj)
	guiObj.drawColInput(screenObj, gameObj)
	guiObj.drawGenerate(screenObj)
	guiObj.drawQuit(screenObj)
	guiObj.drawVisited(screenObj, gameObj)
	guiObj.drawPlayer(screenObj, playerObj)
	guiObj.drawMaze(screenObj, gameObj)
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
			playerObj.movePlayer(event.key, screenObj, gameObj, playerObj, guiObj, rulesObj)
		if event.type == pygame.KEYDOWN and inputObj.isRowInputFocus == True:
			inputObj.takeRowInput(event.key, gameObj)
		if event.type == pygame.KEYDOWN and inputObj.isColInputFocus == True:
			inputObj.takeColInput(event.key, gameObj)
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			if(rulesObj.isResetClicked(pos) == True):
				gameObj.resetGame(screenObj, playerObj, guiObj)
			if(rulesObj.isPlayAgainClicked(gameObj.isGameOver or gameObj.isGameFinish, pos, screenObj) == True or rulesObj.isRandomClicked(pos) == True):
				gameObj = gameObj.startNewGame(screenObj, gameObj, playerObj, guiObj)	
			if(rulesObj.isRowInputClicked(pos) == True or (rulesObj.isRowInputClicked(pos) == False and inputObj.isRowInputFocus == True)):
				inputObj.toggleRowInputFocus()
			if(rulesObj.isColInputClicked(pos) == True or (rulesObj.isColInputClicked(pos) == False and inputObj.isColInputFocus == True)):
				inputObj.toggleColInputFocus()
			if(rulesObj.isGenerateClicked(pos) == True):
				gameObj = gameObj.startNewGame(screenObj, gameObj, playerObj, guiObj, (gameObj.rowSize, gameObj.colSize))
			if(rulesObj.isQuitClicked(pos, screenObj) == True):
				pygame.quit()
				quit()
			

	pygame.display.update()
