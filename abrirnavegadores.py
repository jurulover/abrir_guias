import pyautogui as pg
pg.PAUSE = 1

#abrir o chrome 

pg.press("win")
pg.write("chrome")
pg.press("enter")

#abrir os favoritos  

pg.middleClick(27,97)
pg.middleClick(152,93)
pg.middleClick(230,105)
pg.middleClick(370,95)
pg.middleClick(489,100)
pg.middleClick(695,102)
pg.middleClick(781,93)
pg.middleClick(972,101)
pg.middleClick(1110,97)

#abrir firefox

pg.press("win")
pg.write("firefox")

#pelo firefox ser mais lento, precisa mudar o tempo do pause 
pg.PAUSE=4
pg.press("enter")

#abrir os favoritos

pg.click(24,93)
pg.middleClick(49,97)