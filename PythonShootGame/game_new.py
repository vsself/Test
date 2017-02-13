pygame.init()

# 设置游戏界面大小、背景图片及标题
# 游戏界面像素大小
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 游戏界面标题
pygame.display.set_caption('飞机大战')

# 背景图
background = pygame.image.load('resources/image/background.png').convert()

# Game Over 的背景图
game_over = pygame.image.load('resources/image/gameover.png')

# 飞机及子弹图片集合
plane_img = pygame.image.load('resources/image/shoot.png')

player_rect = []
player_rect.append(pygame.Rect(0, 99, 102, 126))        # 玩家飞机图片
player_rect.append(pygame.Rect(165, 360, 102, 126))
player_rect.append(pygame.Rect(165, 234, 102, 126))     # 玩家爆炸图片
player_rect.append(pygame.Rect(330, 624, 102, 126))
player_rect.append(pygame.Rect(330, 498, 102, 126))
player_rect.append(pygame.Rect(432, 624, 102, 126))
player_pos = [200, 600]
player = Player(plane_img, player_rect, player_pos)

screen.fill(0)
screen.blit(background, (0, 0))

screen.blit(player.image[player.img_index], player.rect)