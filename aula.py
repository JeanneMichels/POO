import arcade, random, math

ALTURA = 600
LARGURA = 800
TITULO = "TUBAKU"

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("tubarão_direita.png", scale=1.2)
       
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
        elif self.right > 800:
            self.right = 800

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > 600:
            self.top = 600
            
class Peixe(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.change_x = random.choice([-4, -3, 3, 4])
        self.change_y = random.choice([-4, -3, 3, 4])
        self.raio_visao = 150
        self.velocidade_fuga = 3.2

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
        elif self.right >= 800:
            self.right = 800
            self.change_x *= -1

        if self.bottom <= 0:
            self.bottom = 0
            self.change_y *= -1
        elif self.top >= 600:
            self.top = 600
            self.change_y *= -1

class Tartaruga(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.change_x = random.choice([-6, 6])
        self.change_y = random.choice([-6, 6])
        self.raio_visao = 180
        self.velocidade_fuga = 4
        
        self.textura_direita = arcade.load_texture("tartaruga_direita.png")
        self.textura_esquerda = arcade.load_texture("tartaruga_esquerda.png")

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

        if self.change_x > 0:
            self.texture = self.textura_direita
        elif self.change_x < 0:
            self.texture = self.textura_esquerda

        if self.left <= 0:
            self.left = 0
            self.change_x *= -1
        elif self.right >= 800:
            self.right = 800
            self.change_x *= -1

        if self.bottom <= 0:
            self.bottom = 0
            self.change_y *= -1
        elif self.top >= 600:
            self.top = 600
            self.change_y *= -1

class JanelaJogo(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Comedor de Peixes - TUBAKU")
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
        self.jogo_finalizado = False
        self.fase_1_concluida = False
        self.fase = 1

        self.lista_peixe = arcade.SpriteList()
        self.lista_tartarugas = arcade.SpriteList()
        
        for i in range(20):
            peixe = Peixe("peixe.png", scale=0.2)
            peixe.center_x = random.randint(50, 750)
            peixe.center_y = random.randint(50, 550)
            self.lista_peixe.append(peixe)

        for i in range(20):
            peixe_especial = Peixe("peixe.png", scale=0.2)
            peixe_especial.color = arcade.color.GOLD
            peixe_especial.center_x = random.randint(50, 750)
            peixe_especial.center_y = random.randint(50, 550)
            peixe_especial.velocidade_fuga = 5
            peixe_especial.raio_visao = 200
            self.lista_peixe.append(peixe_especial)

    def iniciar_fase_2(self):
        self.fase = 2
        self.fase_1_concluida = False
        self.lista_peixe.clear()
        self.lista_tartarugas.clear()
        
        for i in range(25):
            tartaruga = Tartaruga("tartaruga_direita.png", scale=0.5)
            tartaruga.center_x = random.randint(50, 750)
            tartaruga.center_y = random.randint(50, 550)
            self.lista_tartarugas.append(tartaruga)

    def on_draw(self):
        self.clear()
        
        if self.fase == 1:
            self.lista_peixe.draw()
            arcade.draw_text(f"Peixes Comidos: {self.pontuacao}", 10, 570, arcade.color.WHITE, 14)
        else:
            self.lista_tartarugas.draw()
            arcade.draw_text(f"Tartarugas Comidas: {self.pontuacao}", 10, 570, arcade.color.WHITE, 14)
            
        self.sprite_jog.draw()
        arcade.draw_text(f"Fase: {self.fase}", 700, 570, arcade.color.WHITE, 14)
        arcade.draw_text(f"Tempo: {self.cronometro:.2f}s", 10, 545, arcade.color.WHITE, 14)

        if self.fase_1_concluida:
            arcade.draw_text("FASE 1 CONCLUÍDA!🦈 🎉", 240, 350, arcade.color.YELLOW, 26, bold=True)
            arcade.draw_text("Pressione J para ir para a Fase 2 🐢", 230, 300, arcade.color.WHITE, 18)

        if self.jogo_finalizado:
            arcade.draw_text("PARABÉNS! 🎉", 300, 350, arcade.color.YELLOW, 30, bold=True)
            arcade.draw_text("Você completou o jogo inteiro! 🐢 🦈", 200, 300, arcade.color.WHITE, 20)
            arcade.draw_text(f"Tempo Final: {self.cronometro:.2f}s", 310, 260, arcade.color.GOLD, 18)
            arcade.draw_text("Pressione R para recomeçar tudo ou ESC para sair", 160, 200, arcade.color.WHITE, 16)

    def on_update(self, delta_time):
        if not self.jogo_finalizado and not self.fase_1_concluida:
            self.jogador.update(delta_time)
            self.cronometro += delta_time
            
            if self.fase == 1:
                for peixe in self.lista_peixe:
                    peixe.update_fuga(self.jogador)
                self.lista_peixe.update(delta_time)

                peixes_colididos = arcade.check_for_collision_with_list(self.jogador, self.lista_peixe)
                for peixe in peixes_colididos:
                    peixe.remove_from_sprite_lists()
                    self.pontuacao += 1
                
                if len(self.lista_peixe) == 0:
                    self.fase_1_concluida = True
                    
            elif self.fase == 2:
                for tartaruga in self.lista_tartarugas:
                    tartaruga.update_fuga(self.jogador)
                self.lista_tartarugas.update(delta_time)

                tartarugas_colididas = arcade.check_for_collision_with_list(self.jogador, self.lista_tartarugas)
                for tartaruga in tartarugas_colididas:
                    tartaruga.remove_from_sprite_lists()
                    self.pontuacao += 1
                
                if len(self.lista_tartarugas) == 0:
                    self.jogo_finalizado = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.R:
            self.setup()
            
        if key == arcade.key.J and self.fase_1_concluida:
            self.iniciar_fase_2()

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.jogador.change_x = -self.velocidade
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.jogador.change_x = self.velocidade
        elif key == arcade.key.UP or key == arcade.key.W:
            self.jogador.change_y = self.velocidade
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.jogador.change_y = -self.velocidade

        if key == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.LEFT, arcade.key.RIGHT, arcade.key.A, arcade.key.D]:
            self.jogador.change_x = 0
        if key in [arcade.key.UP, arcade.key.DOWN, arcade.key.W, arcade.key.S]:
            self.jogador.change_y = 0

def main():
    janela = JanelaJogo()
    arcade.run()

if __name__ == "__main__":    
    main()