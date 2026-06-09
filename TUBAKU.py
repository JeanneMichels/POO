import arcade, random, math

ALTURA = 768
LARGURA = 1024
TITULO = "TUBAKU"

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("tubarão_direita.png", scale=1)
       
        self.textura_direita = arcade.load_texture("tubarão_direita.png")
        self.textura_esquerda = arcade.load_texture("tubarão_esquerda.png")
        self.textura_cima = arcade.load_texture("tubarão_cima.png")
        self.textura_baixo = arcade.load_texture("tubarão_baixo.png")
    
    def update(self, delta_time):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_y > 0:
            self.texture = self.textura_cima
        elif self.change_y < 0:
            self.texture = self.textura_baixo
        elif self.change_x > 0:
            self.texture = self.textura_direita
        elif self.change_x < 0:
            self.texture = self.textura_esquerda

        if self.left < 0:
            self.left = 0
        elif self.right > LARGURA:
            self.right = LARGURA

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > ALTURA:
            self.top = ALTURA
            
class Peixe(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.change_x = random.choice([-4, -3, 3, 4])
        self.change_y = random.choice([-4, -3, 3, 4])
        self.raio_visao = 150
        self.velocidade_fuga = 4

    def update_fuga(self, jogador):
        vetor_x = self.center_x - jogador.center_x
        vetor_y = self.center_y - jogador.center_y
        distancia = math.sqrt(vetor_x ** 2 + vetor_y ** 2)

        if distancia < self.raio_visao and distancia > 0:
            self.change_x = (vetor_x / distancia) * self.velocidade_fuga
            self.change_y = (vetor_y / distancia) * self.velocidade_fuga

    def update(self, delta_time):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left <= 0:
            self.left = 0
            self.change_x *= -1
        elif self.right >= LARGURA:
            self.right = LARGURA
            self.change_x *= -1

        if self.bottom <= 0:
            self.bottom = 0
            self.change_y *= -1
        elif self.top >= ALTURA:
            self.top = ALTURA
            self.change_y *= -1

class Tartaruga(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.change_x = random.choice([-6, 6])
        self.change_y = random.choice([-6, 6])
        self.raio_visao = 180
        self.velocidade_fuga = 6
        
        self.textura_direita = arcade.load_texture("tartaruga_direita.png")
        self.textura_esquerda = arcade.load_texture("tartaruga_esquerda.png")

    def update_fuga(self, jogador):
        vetor_x = self.center_x - jogador.center_x
        vetor_y = self.center_y - jogador.center_y
        distancia = math.sqrt(vetor_x ** 2 + vetor_y ** 2)

        if distancia < self.raio_visao and distancia > 0:
            self.change_x = (vetor_x / Math.sqrt(vetor_x ** 2 + vetor_y ** 2)) * self.velocidade_fuga
            self.change_y = (vetor_y / math.sqrt(vetor_x ** 2 + vetor_y ** 2)) * self.velocidade_fuga

    def update(self, delta_time):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_x > 0:
            self.texture = self.textura_direita
        elif self.change_x < 0:
            self.texture = self.textura_esquerda

        if self.left <= 0:
            self.left = 0
            self.change_x *= -1
        elif self.right >= LARGURA:
            self.right = LARGURA
            self.change_x *= -1

        if self.bottom <= 0:
            self.bottom = 0
            self.change_y *= -1
        elif self.top >= ALTURA:
            self.top = ALTURA
            self.change_y *= -1

class Orca(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.velocidade_perseguicao = 15
        self.textura_direita = arcade.load_texture("orca_direita.png")
        self.textura_esquerda = arcade.load_texture("orca_esquerda.png")

    def perseguir(self, jogador):
        vetor_x = jogador.center_x - self.center_x
        vetor_y = jogador.center_y - self.center_y
        distancia = math.sqrt(vetor_x ** 2 + vetor_y ** 2)

        if distancia > 0:
            self.change_x = (vetor_x / distancia) * self.velocidade_perseguicao
            self.change_y = (vetor_y / distancia) * self.velocidade_perseguicao

    def update(self, delta_time):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_x > 0:
            self.texture = self.textura_direita
        elif self.change_x < 0:
            self.texture = self.textura_esquerda

class JanelaJogo(arcade.Window):
    def __init__(self):
        super().__init__(LARGURA, ALTURA, "Comedor de Peixes - TUBAKU")
        arcade.set_background_color(arcade.color.DEEP_SKY_BLUE)
        self.setup()

    def setup(self):
        self.jogador = Player()
        self.jogador.bottom = 0
        self.jogador.left = 0
        self.sprite_jog = arcade.SpriteList()
        self.sprite_jog.append(self.jogador)
        
        self.velocidade = 20
        self.pontuacao = 0
        self.cronometro = 0.0
        self.cronometro_fase3 = 0.0
        self.jogo_finalizado = False
        self.game_over = False
        self.fase_1_concluida = False
        self.fase_2_concluida = False
        self.fase = 1

        self.lista_peixe = arcade.SpriteList()
        self.lista_tartarugas = arcade.SpriteList()
        self.lista_orca = arcade.SpriteList()
        
        for i in range(80):
            peixe = Peixe("peixe.png", scale=0.2)
            peixe.center_x = random.randint(50, LARGURA - 50)
            peixe.center_y = random.randint(50, ALTURA - 50)
            self.lista_peixe.append(peixe)

        for i in range(20):
            peixe_especial = Peixe("peixe.png", scale=0.2)
            peixe_especial.color = arcade.color.GOLD
            peixe_especial.center_x = random.randint(50, LARGURA - 50)
            peixe_especial.center_y = random.randint(50, ALTURA - 50)
            peixe_especial.velocidade_fuga = 4
            peixe_especial.raio_visao = 200
            self.lista_peixe.append(peixe_especial)

    def iniciar_fase_2(self):
        self.fase = 2
        self.fase_1_concluida = False
        self.lista_peixe.clear()
        
        for i in range(25):
            tartaruga = Tartaruga("tartaruga_direita.png", scale=0.2)
            tartaruga.center_x = random.randint(50, LARGURA - 50)
            tartaruga.center_y = random.randint(50, ALTURA - 50)
            self.lista_tartarugas.append(tartaruga)

    def iniciar_fase_3(self):
        self.fase = 3
        self.fase_2_concluida = False
        self.lista_tartarugas.clear()
        self.cronometro_fase3 = 0.0
        
        orca = Orca("orca_direita.png", scale=0.6)
        orca.center_x = 100
        orca.center_y = ALTURA - 100
        self.lista_orca.append(orca)

    def on_draw(self):
        self.clear()
        
        if self.fase == 1:
            self.lista_peixe.draw()
            arcade.draw_text(f"Peixes Comidos: {self.pontuacao}", 10, ALTURA - 30, arcade.color.WHITE, 14)
        elif self.fase == 2:
            self.lista_tartarugas.draw()
            arcade.draw_text(f"Tartarugas Comidas: {self.pontuacao}", 10, ALTURA - 30, arcade.color.WHITE, 14)
        elif self.fase == 3:
            self.lista_orca.draw()
            tempo_restante = max(0.0, 10.0 - self.cronometro_fase3)
            arcade.draw_text(f"Sobreviva por: {tempo_restante:.2f}s", 10, ALTURA - 30, arcade.color.RED, 14, bold=True)
            
        self.sprite_jog.draw()
        arcade.draw_text(f"Fase: {self.fase}", LARGURA - 100, ALTURA - 30, arcade.color.WHITE, 14)
        arcade.draw_text(f"Tempo Total: {self.cronometro:.2f}s", 10, ALTURA - 55, arcade.color.WHITE, 14)

        if self.fase_1_concluida:
            arcade.draw_text("FASE 1 CONCLUÍDA! 🌊", LARGURA // 2 - 160, ALTURA // 2, arcade.color.YELLOW, 26, bold=True)
            arcade.draw_text("Pressione J para ir para a Fase 2", LARGURA // 2 - 150, ALTURA // 2 - 50, arcade.color.WHITE, 18)

        if self.fase_2_concluida:
            arcade.draw_text("FASE 2 CONCLUÍDA! 🐢", LARGURA // 2 - 160, ALTURA // 2, arcade.color.YELLOW, 26, bold=True)
            arcade.draw_text("Pressione J para ir para a Fase 3", LARGURA // 2 - 150, ALTURA // 2 - 50, arcade.color.WHITE, 18)

        if self.game_over:
            arcade.draw_text("GAME OVER! 💀", LARGURA // 2 - 120, ALTURA // 2, arcade.color.RED, 30, bold=True)
            arcade.draw_text("A Orca pegou o Tubaku!", LARGURA // 2 - 130, ALTURA // 2 - 50, arcade.color.WHITE, 18)
            arcade.draw_text("Pressione R para recomeçar tudo", LARGURA // 2 - 150, ALTURA // 2 - 100, arcade.color.WHITE, 16)

        if self.jogo_finalizado:
            arcade.draw_text("PARABÉNS! 🎉", LARGURA // 2 - 100, ALTURA // 2 + 50, arcade.color.YELLOW, 30, bold=True)
            arcade.draw_text("Você completou o jogo inteiro! 🦈", LARGURA // 2 - 160, ALTURA // 2, arcade.color.WHITE, 20)
            arcade.draw_text(f"Tempo Final: {self.cronometro:.2f}s", LARGURA // 2 - 80, ALTURA // 2 - 40, arcade.color.GOLD, 18)
            arcade.draw_text("Pressione R para recomeçar tudo ou ESC para sair", LARGURA // 2 - 220, ALTURA // 2 - 100, arcade.color.WHITE, 16)

    def on_update(self, delta_time):
        if not self.jogo_finalizado and not self.game_over and not self.fase_1_concluida and not self.fase_2_concluida:
            self.jogador.update(delta_time)
            self.cronometro += delta_time
            
            if self.fase == 1:
                for peixe in self.lista_peixe:
                    peixe.update_fuga(self.jogador)
                self.lista_peixe.update(delta_time)

