import pygame # Impordime pygame'i
import sys # Impordime sys'i

pygame.init() # Algatan pygame'i

#Värvid
lBlue = [153, 204, 255] # Muutuja lBlue saab väärtuseks [153, 204, 255]

#Ekraani seaded
screenX = 640 # ScreenX saab väärtuseks 640px
screenY = 480 # ScreenY saab väärtuseks 480px
screen=pygame.display.set_mode([screenX,screenY]) # Muutuja screen saab väärtuseks pygame.display.set_mode([640,480])
pygame.display.set_caption('4') # Määrab praeguse akna pealkirja
screen.fill(lBlue) # Täidab ekraani
clock = pygame.time.Clock() # Loon kella objekti

#Lisame tausta
bg = pygame.image.load("bg_rally.jpg") # Muutja bg saab väärtuse pygame.image.load("bg_rally.jpg")
screen.blit(bg,[0,0]) # Tausta asetus ekraanil (laius,kõrgus)

#Lisame auto
auto = pygame.image.load("f1_red.png") # Muutuja auto saab väärtuse pygame.image.load("f1_red.png")
screen.blit(auto,[299,390]) # Auto asetus ekraanil (laius,kõrgus)

#Graafika laadimine
auto2 = pygame.image.load("f1_blue.png") # Muutuja auto2 saab väärtuse pygame.image.load("f1_blue.png") 

#Kiirus ja asukoht
posX1, posY1 = 180, -60 # X ja Y asetus ekraanil 
speedX1, speedY1 = 0, 3 # X ja Y kiirus ekraanil

#Kiirus ja asukoht teise auto
posX2, posY2 = 420, -250 # X ja Y asetus ekraanil
speedX2, speedY2 = 0, 3 # X ja Y kiirus ekraanil

#Kiirus ja asukoht kolmanda auto
posX3, posY3 = 420, 0 # X ja Y asetus ekraanil
speedX3, speedY3 = 0, 3 # X ja Y kiirus ekraanil

#Kiirus ja asukoht neljanda auto
posX4, posY4 = 180, -350 # X ja Y asetus ekraanil
speedX4, speedY4 = 0, 3 # X ja Y kiirus ekraanil

#Counter
counter = 0 # Muutuja counter saab väärtuseks 0

#Pygame exit
gameover = False # Muutuja gameover saab väärtuseks False

while not gameover: # Juhul kui pole gameover
    
    #Eventi käsitlemine
    for event in pygame.event.get():
        #Vaatab kas event on x nupu vajutus 
        if event.type == pygame.QUIT:
            #Kui vajutatakse x nuppu, siis programm suletakse
            pygame.quit()
            sys.exit()
    
    #FPS
    clock.tick(60) # FPS väärtuseks saab 60

    #Uuendame esimese auto asukohta
    posY1 += speedY1 # Muutuja posY1 saab väärtuseks posY1 + speedY1
    
    #Kui esimene auto on jõudnud ekraani alaossa, siis alustab see ülevalt uuesti
    if posY1 >= screenY: # Kui posY1 on suurem võrdne screenY
        posY1 = -60 # Muutuja posY1 väärtuseks saab -60
        counter += 1 # Muutuja counter saab väärtuse counter + 1
        
    #Uuendame teise auto asukohta
    posY2 += speedY2 # Muutuja posY2 saab väärtuseks posY2 + speedY2
    
    #Kui teine auto on jõudnud ekraani alaossa, siis alustab see ülevalt uuesti
    if posY2 >= screenY: # Kui posY2 on suurem võrdne screenY
        posY2 = -60 # Muutuja posY2 väärtuseks saab -60
        counter += 1 # Muutuja counter saab väärtuse counter + 1
        
    #Uuendame kolmanda auto asukohta
    posY3 += speedY3 # Muutuja posY3 saab väärtuseks posY3 + speedY3
    
    #Kui kolmas auto on jõudnud ekraani alaossa, siis alustab see ülevalt uuesti    if posY3 >= screenY:
    if posY3 >= screenY: # Kui posY3 on suurem võrdne screenY
        posY3 = -60 # Muutuja posY3 väärtuseks saab -60
        counter += 1 # Muutuja counter saab väärtuse counter + 1
    
    #Uuendame neljanda auto asukohta
    posY4 += speedY4 # Muutuja posY4 saab väärtuseks posY4 + speedY4
    
    #Kui neljas auto on jõudnud ekraani alaossa, siis alustab see ülevalt uuesti
    if posY4 >= screenY: # Kui posY4 on suurem võrdne screenY
        posY4 = -60 # Muutuja posY4 väärtuseks saab -60
        counter += 1 # Muutuja counter saab väärtuse counter + 1
            
    #Skoori lisamine ekraanile
    font = pygame.font.SysFont("Arial", 20) # Muutuja font saab väärtuseks pygame.font.SysFont(fondi nimetus, fondi suurus)
    text = font.render("Skoor: " + str(counter), True, (0, 0, 0)) # Muutuja text saab väärtuseks font.render("Skoor: " + str(counter), True, (0, 0, 0))
    screen.blit(text, (10, 10)) # Teksti asetus ekraanil (laius,kõrgus)
    
    #Pildi lisamine ekraanile
    screen.blit(auto2, (posX1,posY1)) # Auto2 asetus ekraanil X ja Y positsioon
    screen.blit(auto2, (posX2,posY2)) # Auto2 asetus ekraanil X ja Y positsioon
    screen.blit(auto2, (posX3,posY3)) # Auto2 asetus ekraanil X ja Y positsioon
    screen.blit(auto2, (posX4,posY4)) # Auto2 asetus ekraanil X ja Y positsioon
    
    pygame.display.flip() #Kuvab lisatud objektid ekraanile
    
    #Tausta uuesti laadimine
    bg = pygame.image.load("bg_rally.jpg") # Muutja bg saab väärtuse pygame.image.load("bg_rally.jpg")
    screen.blit(bg,[0,0]) # Tausta asetus ekraanil (laius,kõrgus)
    
    #Lisame auto
    auto = pygame.image.load("f1_red.png") #Muutuja auto saab väärtuse pygame.image.load("f1_red.png")
    screen.blit(auto,[299,390]) #Auto asetus ekraanil (laius,kõrgus)