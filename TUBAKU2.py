
import arcade
import random
import math

ALTURA = 600
LARGURA = 800
TITULO = "TUBAKU"

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("tubarão_direita.png", scale=0.5)
        
        self.textura_direita = arcade.load_texture("tubarão_direita.png")
        self.textura_esquerda = arcade.load_texture("tubarão_esquerda.png")
        self.textura_cima = arcade.load_texture("tubarão_cima.png")
        self.textura_baixo = arcade.load_texture("tubarão_baixo.png")
     
    def update(self, delta_time=0.0):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_y > 0:
            self.texture = self.textura_cima
        elif self.change_y < 0:
            self.texture = self.textura_baixo
        
        if self.change_x > 0:
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
        self.tipo = "normal"

    def update_fuga(self, jogador):
        vetor_x = self.center_x - jogador.center_x
        vetor_y = self.center_y - jogador.center_y
        distancia = math.sqrt(vetor_x ** 2 + vetor_y ** 2)
        if 0 < distancia < self.raio_visao:
            self.change_x = (vetor_x / distancia) * self.velocidade_fuga
            self.change_y = (vetor_y / distancia) * self.velocidade_fuga

    def update(self, delta_time=0.0):
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


class Orca(arcade.Sprite):
    def __init__(self, filename, scale=0.8):
        super().__init__("orca_direita.png", scale)
        
        self.textura_direita = arcade.load_texture("orca_direita.png")
        self.textura_esquerda = arcade.load_texture("orca_esquerda.png")
        
        self.change_x = random.choice([-3.5, -2.5, 2.5, 3.5])
        self.change_y = random.choice([-3.5, -2.5, 2.5, 3.5])

    def update(self, delta_time=0.0):
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
        if 0 < distancia < self.raio_visao:
            self.change_x = (vetor_x / distancia) * self.velocidade_fuga
            self.change_y = (vetor_y / distancia) * self.velocidade_fuga

    def update(self, delta_time=0.0):
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


# --- TELAS EDUCATIVAS DE TRANSIÇÃO ---

class TelaTextoFase1(arcade.View):
    def __init__(self, tela_jogo):
        super().__init__()
        self.tela_jogo = tela_jogo

    def on_show_view(self):
        self.background_color = (0, 80, 100)

    def on_draw(self):
        self.clear()
        arcade.draw_text("FASE 1 CONCLUÍDA!", LARGURA / 2, 500, arcade.color.YELLOW, 26, anchor_x="center", bold=True)
        arcade.draw_text("CURIOSIDADE: ALIMENTAÇÃO DOS TUBARÕES", LARGURA / 2, 440, arcade.color.WHITE, 18, anchor_x="center", bold=True)
        
        texto = (
            "Os tubarões são predadores de topo essenciais para o equilíbrio dos oceanos.\n\n"
            "• Eles se alimentam principalmente de peixes, moluscos e crustáceos.\n"
            "• Algumas espécies maiores caçam mamíferos marinhos e tartarugas.\n"
            "• Tubarões possuem um olfato extremamente apurado e a capacidade de sentir\n"
            "  campos elétricos emitidos por outros animais (ampolas de Lorenzini).\n"
            "• Eles ajudam a manter a população de peixes saudável ao caçar animais doentes."
        )
        arcade.draw_text(texto, LARGURA / 2, 280, arcade.color.LIGHT_GRAY, 14, anchor_x="center", multiline=True, width=700)
        arcade.draw_text("Pressione [ESPAÇO] para ir para a Fase 2", LARGURA / 2, 80, arcade.color.GOLD, 16, anchor_x="center", bold=True)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.tela_jogo.iniciar_fase_2()
            self.window.show_view(self.tela_jogo)


class TelaTextoFase2(arcade.View):
    def __init__(self, tela_jogo):
        super().__init__()
        self.tela_jogo = tela_jogo

    def on_show_view(self):
        self.background_color = arcade.color.DARK_BLUE

    def on_draw(self):
        self.clear()
        arcade.draw_text("FASE 2 CONCLUÍDA!", LARGURA / 2, 500, arcade.color.YELLOW, 26, anchor_x="center", bold=True)
        arcade.draw_text("CURIOSIDADE: TUBARÕES E TARTARUGAS MARINHAS", LARGURA / 2, 440, arcade.color.WHITE, 18, anchor_x="center", bold=True)
        
        texto = (
            "As tartarugas marinhas são presas de tubarões de grande porte (como o Tubarão-Tigre).\n\n"
            "• O casco duro da tartaruga não é problema para a mordida potente destes predadores.\n"
            "• Ao caçar tartarugas, os tubarões impedem que elas consumam excessivamente as\n"
            "  erbas marinhas, garantindo a saúde desse ecossistema marinho!\n"
            "• Agora prepare-se: na próxima fase, você passará de predador para presa!"
        )
        arcade.draw_text(texto, LARGURA / 2, 290, arcade.color.LIGHT_GRAY, 14, anchor_x="center", multiline=True, width=700)
        arcade.draw_text("Pressione [ESPAÇO] para ir para a Fase 3", LARGURA / 2, 80, arcade.color.GOLD, 16, anchor_x="center", bold=True)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.tela_jogo.iniciar_fase_3()
            self.window.show_view(self.tela_jogo)


class TelaTextoFase3(arcade.View):
    def __init__(self, pontuacao_final):
        super().__init__()
        self.pontuacao = pontuacao_final

    def on_show_view(self):
        self.background_color = arcade.color.DARK_BLUE

    def on_draw(self):
        self.clear()
        arcade.draw_text("VOCÊ SOBREVIVEU ÀS ORCAS!", LARGURA / 2, 500, arcade.color.GREEN, 26, anchor_x="center", bold=True)
        arcade.draw_text("POR QUE AS ORCAS CAÇAM TUBARÕES?", LARGURA / 2, 440, arcade.color.WHITE, 18, anchor_x="center", bold=True)
        
        texto = (
            "Embora o tubarão seja um superpredador, a Orca está no topo definitivo!\n\n"
            "• As orcas são golfinhos gigantes extremamente inteligentes e caçam em grupo.\n"
            "• Elas caçam tubarões principalmente para comer o seu FÍGADO, que é rico em nutrientes\n"
            "  e gorduras (esqualeno).\n"
            "• As orcas viram os tubarões de cabeça para baixo, o que faz com que eles entrem em\n"
            "  um estado de paralisia chamado 'imobilidade tônica', tornando a caça fácil."
        )
        arcade.draw_text(texto, LARGURA / 2, 280, arcade.color.LIGHT_GRAY, 14, anchor_x="center", multiline=True, width=700)
        arcade.draw_text("Pressione [ESPAÇO] para ver os resultados!", LARGURA / 2, 80, arcade.color.GOLD, 16, anchor_x="center", bold=True)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            tela_vitoria = TelaVitoria(self.pontuacao)
            self.window.show_view(tela_vitoria)


# --- TELAS PRINCIPAIS ---

class TelaInicial(arcade.View):
    def __init__(self):
        super().__init__()
        self.exibindo_objetivos = False

    def on_show_view(self):
        self.background_color = arcade.color.DARK_BLUE

    def on_draw(self):
        self.clear()
        if not self.exibindo_objetivos:
            arcade.draw_text("COMEDOR DE PEIXES", LARGURA / 2, 420, arcade.color.WHITE, 32, anchor_x="center", bold=True)
            arcade.draw_text("Pressione [J] para Jogar", LARGURA / 2, 320, arcade.color.LIGHT_SEA_GREEN, 18, anchor_x="center")
            arcade.draw_text("Pressione [O] para Ver os Objetivos", LARGURA / 2, 270, arcade.color.LIGHT_SEA_GREEN, 18, anchor_x="center")
            arcade.draw_text("Pressione [ESC] para Sair", LARGURA / 2, 220, arcade.color.LIGHT_SEA_GREEN, 18, anchor_x="center")
        else:
            arcade.draw_text("OBJETIVOS DO JOGO", LARGURA / 2, 450, arcade.color.YELLOW, 28, anchor_x="center", bold=True)
            arcade.draw_text("1. Controle o Tubarão usando as setas do teclado ou W, A, S, D.", 50, 360, arcade.color.WHITE, 16)
            arcade.draw_text("2. Na Fase 1, devore todos os peixes normais e dourados rápidos.", 50, 320, arcade.color.WHITE, 16)
            arcade.draw_text("3. Na Fase 2, capture as tartarugas velozes para vencer.", 50, 280, arcade.color.WHITE, 16)
            arcade.draw_text("4. Na Fase 3, fuja das orcas por 10 segundos.", 50, 248, arcade.color.WHITE, 16)
            arcade.draw_text("5. Os animais tentarão fugir de você se você chegar muito perto!", 50, 218, arcade.color.WHITE, 16)
            arcade.draw_text("6. Seja rápido e coma todos os peixes e tartarugas!", 50, 185, arcade.color.WHITE, 16)
            arcade.draw_text("7. Desenvolvido por Jeanne Michels D Aviz e Victoria Dias Goes.", 50, 155, arcade.color.WHITE, 16)
            arcade.draw_text("Pressione [M] ou [ESC] para Voltar ao Menu", LARGURA / 2, 100, arcade.color.LIGHT_GRAY, 14, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if not self.exibindo_objetivos:
            if key == arcade.key.J:
                tela_jogo = TelaJogo()
                tela_jogo.setup()
                self.window.show_view(tela_jogo)
            elif key == arcade.key.O:
                self.exibindo_objetivos = True 
            elif key == arcade.key.ESCAPE:
                arcade.close_window()
        else:
            if key == arcade.key.M or key == arcade.key.ESCAPE:
                self.exibindo_objetivos = False 


class TelaVitoria(arcade.View):
    def __init__(self, pontuacao_final):
        super().__init__()
        self.pontuacao = pontuacao_final

    def on_show_view(self):
        self.background_color = arcade.color.DARK_GREEN

    def on_draw(self):
        self.clear()
        arcade.draw_text("PARABÉNS! VOCÊ VENCEU O OCEANO!", LARGURA / 2, 400, arcade.color.GOLD, 28, anchor_x="center", bold=True)
        arcade.draw_text(f"Pontuação Máxima: {self.pontuacao} pontos", LARGURA / 2, 320, arcade.color.WHITE, 18, anchor_x="center")
        arcade.draw_text("Pressione [R] para Jogar Novamente", LARGURA / 2, 220, arcade.color.AQUAMARINE, 16, anchor_x="center")
        arcade.draw_text("Pressione [ESC] para Voltar ao Menu", LARGURA / 2, 170, arcade.color.AQUAMARINE, 16, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.R:
            tela_jogo = TelaJogo()
            tela_jogo.setup()
            self.window.show_view(tela_jogo)
        elif key == arcade.key.ESCAPE:
            menu_inicial = TelaInicial()
            self.window.show_view(menu_inicial)


class TelaGameOver(arcade.View):
    def __init__(self, pontuacao_final):
        super().__init__()
        self.pontuacao = pontuacao_final

    def on_show_view(self):
        self.background_color = arcade.color.DARK_RED

    def on_draw(self):
        self.clear()
        arcade.draw_text("GAME OVER", LARGURA / 2, 400, arcade.color.WHITE, 40, anchor_x="center", bold=True)
        arcade.draw_text(f"Pontos acumulados: {self.pontuacao}", LARGURA / 2, 320, arcade.color.LIGHT_GRAY, 18, anchor_x="center")
        arcade.draw_text("Pressione [R] para Tentar Novamente", LARGURA / 2, 220, arcade.color.YELLOW, 16, anchor_x="center")
        arcade.draw_text("Pressione [ESC] para Voltar ao Menu", LARGURA / 2, 170, arcade.color.YELLOW, 16, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.R:
            tela_jogo = TelaJogo()
            tela_jogo.setup()
            self.window.show_view(tela_jogo)
        elif key == arcade.key.ESCAPE:
            menu_inicial = TelaInicial()
            self.window.show_view(menu_inicial)


class TelaJogo(arcade.View):
    def __init__(self):
        super().__init__()
        self.cenario_fase2 = None
        
        self.jogador = None
        self.sprite_jog = None
        self.velocidade = 10
        self.pontuacao = 0
        self.fase = 1
        
        self.lista_peixe = None
        self.lista_tartarugas = None
        self.lista_orcas = None
        
        self.jogador_vivo = True
        self.cronometro_fase3 = 0.0
        self.tempo_preparacao = 0.0

    def setup(self):
        try:
            self.cenario_fase2 = arcade.load_texture("cenario2.png")
        except FileNotFoundError:
            self.cenario_fase2 = None
            
        self.jogador = Player()
        self.jogador.center_x = 400
        self.jogador.center_y = 300
        self.sprite_jog = arcade.SpriteList()
        self.sprite_jog.append(self.jogador)
        
        self.pontuacao = 0
        self.fase = 1
        self.jogador_vivo = True
        self.cronometro_fase3 = 0.0  
        self.tempo_preparacao = 0.0
        
        self.lista_peixe = arcade.SpriteList()
        self.lista_tartarugas = arcade.SpriteList()
        self.lista_orcas = arcade.SpriteList()

        for i in range(20):
            peixe = Peixe("peixe.png", scale=0.2)
            peixe.center_x = random.randint(50, 750)
            peixe.center_y = random.randint(50, 550)
            peixe.tipo = "normal"
            self.lista_peixe.append(peixe)
            
        for i in range(10):
            peixe_especial = Peixe("peixe.png", scale=0.2)
            peixe_especial.color = arcade.color.GOLD
            peixe_especial.center_x = random.randint(50, 750)
            peixe_especial.center_y = random.randint(50, 550)
            peixe_especial.velocidade_fuga = 5
            peixe_especial.raio_visao = 200
            peixe_especial.tipo = "dourado"
            self.lista_peixe.append(peixe_especial)

    def iniciar_fase_2(self):
        self.fase = 2
        self.lista_peixe.clear()
        self.lista_tartarugas.clear()
        self.lista_orcas.clear()
        
        for i in range(15):
            tartaruga = Tartaruga("tartaruga_direita.png", scale=0.5)
            tartaruga.center_x = random.randint(50, 750)
            tartaruga.center_y = random.randint(50, 550)
            self.lista_tartarugas.append(tartaruga)

    def iniciar_fase_3(self):
        self.fase = 3
        self.lista_peixe.clear()
        self.lista_tartarugas.clear()
        self.lista_orcas.clear()
        
        self.cronometro_fase3 = 10.0 
        self.tempo_preparacao = 3.0
        
        self.jogador.center_x = LARGURA / 2
        self.jogador.center_y = ALTURA / 2
        self.jogador.change_x = 0
        self.jogador.change_y = 0
        
        orca = Orca("orca_direita.png", scale=1.2)
        orca.center_x = random.choice([100, 700])
        orca.center_y = random.choice([100, 500])
        self.lista_orcas.append(orca)

    def on_draw(self):
        self.clear()
        
        if self.fase == 1:
            self.background_color = arcade.color.SEA_BLUE
            self.lista_peixe.draw()
            
        elif self.fase == 2:
            if self.cenario_fase2:
                arcade.draw_texture_rect(texture=self.cenario_fase2, rect=arcade.LBWH(0, 0, LARGURA, ALTURA))
            else:
                self.background_color = arcade.color.OCEAN_BLUE
            self.lista_tartarugas.draw()
            
        elif self.fase == 3:
            self.background_color = arcade.color.DARK_BLUE
            self.lista_orcas.draw()
            
            if self.tempo_preparacao > 0:
                arcade.draw_text(f"PREPARE-SE! A CAÇADA COMEÇA EM: {int(self.tempo_preparacao) + 1}", 
                                 LARGURA / 2, ALTURA - 40, arcade.color.RED, 18, anchor_x="center", bold=True)
            else:
                arcade.draw_text(f"Sobreviva: {self.cronometro_fase3:.1f}s", 
                                 LARGURA / 2, ALTURA - 40, arcade.color.YELLOW, 18, anchor_x="center", bold=True)
            
        self.sprite_jog.draw()
        arcade.draw_text(f"Pontos: {self.pontuacao}", 10, 570, arcade.color.WHITE, 14, bold=True)
        arcade.draw_text(f"Fase: {self.fase}", LARGURA - 80, 570, arcade.color.WHITE, 14, bold=True)

    def on_update(self, delta_time):
        if not self.jogador_vivo:
            return

        self.sprite_jog.update()
        
        if self.fase == 1:
            for peixe in self.lista_peixe:
                peixe.update_fuga(self.jogador)
                peixe.update()
                
            colisoes = arcade.check_for_collision_with_list(self.jogador, self.lista_peixe)
            for peixe in colisoes:
                peixe.remove_from_sprite_lists()
                if peixe.tipo == "dourado":
                    self.pontuacao += 30
                else:
                    self.pontuacao += 10
                    
            if len(self.lista_peixe) == 0:
                tela_texto1 = TelaTextoFase1(self)
                self.window.show_view(tela_texto1)
                return

        elif self.fase == 2:
            for tartaruga in self.lista_tartarugas:
                tartaruga.update_fuga(self.jogador)
                tartaruga.update()
                
            colisoes = arcade.check_for_collision_with_list(self.jogador, self.lista_tartarugas)
            for tartaruga in colisoes:
                tartaruga.remove_from_sprite_lists()
                self.pontuacao += 50
                
            if len(self.lista_tartarugas) == 0:
                tela_texto2 = TelaTextoFase2(self)
                self.window.show_view(tela_texto2)
                return

        elif self.fase == 3:
            if self.tempo_preparacao > 0:
                self.tempo_preparacao -= delta_time
                return
            
            self.lista_orcas.update()
            self.cronometro_fase3 -= delta_time
            
            if arcade.check_for_collision_with_list(self.jogador, self.lista_orcas):
                self.jogador_vivo = False
                tela_game_over = TelaGameOver(self.pontuacao)
                self.window.show_view(tela_game_over)
                return
                
            if self.cronometro_fase3 <= 0:
                tela_texto3 = TelaTextoFase3(self.pontuacao)
                self.window.show_view(tela_texto3)
                return

    def on_key_press(self, key, modifiers):
        if key in (arcade.key.UP, arcade.key.W):
            self.jogador.change_y = self.velocidade
        elif key in (arcade.key.DOWN, arcade.key.S):
            self.jogador.change_y = -self.velocidade
        elif key in (arcade.key.LEFT, arcade.key.A):
            self.jogador.change_x = -self.velocidade
        elif key in (arcade.key.RIGHT, arcade.key.D):
            self.jogador.change_x = self.velocidade

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.LEFT, arcade.key.A, arcade.key.RIGHT, arcade.key.D]:
            self.jogador.change_x = 0

        if key in [arcade.key.UP, arcade.key.W, arcade.key.DOWN, arcade.key.S]:
            self.jogador.change_y = 0


def executar():
    janela = arcade.Window(LARGURA, ALTURA, TITULO)
    menu_inicial = TelaInicial()
    janela.show_view(menu_inicial)
    arcade.run()

if __name__ == "__main__":
    executar()

