import pygame

def getSprites(direccion,scale=1.5):
    sprites = []
    n=0
    while True:
        try:
            print('Loading : ',f'{direccion}/{n}.png')
            actualSprite=pygame.image.load(f'{direccion}/{n}.png')
            size = actualSprite.get_size()
            scaleSprite = pygame.transform.scale(actualSprite, (int(size[0]*scale), int(size[1]*scale)))
            sprites.append(scaleSprite)
            n+=1
        except FileNotFoundError:
            return sprites

character = {
    'Magic_Book':getSprites('Magic_Book'),
    'Knife':getSprites('Knife'),
    'Beer':getSprites('Beer'),
    'Water':getSprites('Water', scale = 1),
    'Principal_Character': {
        'Down': {
            'Attack':getSprites('Principal_Character/Down/Attack1'), 
            'Death':getSprites('Principal_Character/Down/Death'),
            'Hurt':getSprites('Principal_Character/Down/Hurt'),
            'Idle':getSprites('Principal_Character/Down/Idle'),
            'Walk':getSprites('Principal_Character/Down/Walk') },

        'Left': {
            'Attack':getSprites('Principal_Character/Left/Attack1'), 
            'Death':getSprites('Principal_Character/Left/Death'),
            'Hurt':getSprites('Principal_Character/Left/Hurt'),
            'Idle':getSprites('Principal_Character/Left/Idle'),
            'Walk':getSprites('Principal_Character/Left/Walk') },
        'Right': {
            'Attack':getSprites('Principal_Character/Right/Attack1'), 
            'Death':getSprites('Principal_Character/Right/Death'),
            'Hurt':getSprites('Principal_Character/Right/Hurt'),
            'Idle':getSprites('Principal_Character/Right/Idle'),
            'Walk':getSprites('Principal_Character/Right/Walk') },
        'Up': {
            'Attack':getSprites('Principal_Character/Up/Attack1'), 
            'Death':getSprites('Principal_Character/Up/Death'),
            'Hurt':getSprites('Principal_Character/Up/Hurt'),
            'Idle':getSprites('Principal_Character/Up/Idle'),
            'Walk':getSprites('Principal_Character/Up/Walk') },

    },
    'Green_Enemy':{
        'Down': {
            'Attack':getSprites('Green_Enemy/Down/Attack'), 
            'Death':getSprites('Green_Enemy/Down/Death'),
            'Hurt':getSprites('Green_Enemy/Down/Hurt'),
            'Idle':getSprites('Green_Enemy/Down/Idle'),
            'Walk':getSprites('Green_Enemy/Down/Walk') },
        'Left': {
            'Attack':getSprites('Green_Enemy/Left/Attack'), 
            'Death':getSprites('Green_Enemy/Left/Death'),
            'Hurt':getSprites('Green_Enemy/Left/Hurt'),
            'Idle':getSprites('Green_Enemy/Left/Idle'),
            'Walk':getSprites('Green_Enemy/Left/Walk') },
        'Right':  {
            'Attack':getSprites('Green_Enemy/Right/Attack'), 
            'Death':getSprites('Green_Enemy/Right/Death'),
            'Hurt':getSprites('Green_Enemy/Right/Hurt'),
            'Idle':getSprites('Green_Enemy/Right/Idle'),
            'Walk':getSprites('Green_Enemy/Right/Walk') },
        'Up': {
            'Attack':getSprites('Green_Enemy/Up/Attack'), 
            'Death':getSprites('Green_Enemy/Up/Death'),
            'Hurt':getSprites('Green_Enemy/Up/Hurt'),
            'Idle':getSprites('Green_Enemy/Up/Idle'),
            'Walk':getSprites('Green_Enemy/Up/Walk') },

    },
    'Skeleton_Enemy':{
        'Down': {
            'Attack':getSprites('Skeleton_Enemy/Down/Attack'), 
            'Death':getSprites('Skeleton_Enemy/Down/Death'),
            'Hurt':getSprites('Skeleton_Enemy/Down/Hurt'),
            'Idle':getSprites('Skeleton_Enemy/Down/Idle'),
            'Walk':getSprites('Skeleton_Enemy/Down/Walk') },
        'Left': {
            'Attack':getSprites('Skeleton_Enemy/Left/Attack'), 
            'Death':getSprites('Skeleton_Enemy/Left/Death'),
            'Hurt':getSprites('Skeleton_Enemy/Left/Hurt'),
            'Idle':getSprites('Skeleton_Enemy/Left/Idle'),
            'Walk':getSprites('Skeleton_Enemy/Left/Walk') },
        'Right':  {
            'Attack':getSprites('Skeleton_Enemy/Right/Attack'), 
            'Death':getSprites('Skeleton_Enemy/Right/Death'),
            'Hurt':getSprites('Skeleton_Enemy/Right/Hurt'),
            'Idle':getSprites('Skeleton_Enemy/Right/Idle'),
            'Walk':getSprites('Skeleton_Enemy/Right/Walk') },
        'Up': {
            'Attack':getSprites('Skeleton_Enemy/Up/Attack'), 
            'Death':getSprites('Skeleton_Enemy/Up/Death'),
            'Hurt':getSprites('Skeleton_Enemy/Up/Hurt'),
            'Idle':getSprites('Skeleton_Enemy/Up/Idle'),
            'Walk':getSprites('Skeleton_Enemy/Up/Walk') },

    },
}



