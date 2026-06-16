import arcade
import random

class Player(arcade.Sprite):
    def __init__(self) -> None:
        super().__init__("sonic_direita.png", scale=0.8)
        self.txt_parado_direita: arcade.Texture = self.texture
        self.txt_parado_esquerda: arcade.Texture = arcade.load_texture("sonic_esquerda.png")
        self.txt_correndo_direita: arcade.Texture = arcade.load_texture("sonic_correndo_direita.png")
        self.txt_correndo_esquerda: arcade.Texture = arcade.load_texture("sonic_correndo_esquerda.png")
        
    def update(self, *args, **kwargs) -> None:
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_x > 0:
            self.texture = self.txt_correndo_direita
        elif self.change_x < 0:
            self.texture = self.txt_correndo_esquerda
        else:
            if self.texture == self.txt_correndo_direita:
                self.texture = self.txt_parado_direita
            elif self.texture == self.txt_correndo_esquerda:
                self.texture = self.txt_parado_esquerda

        if self.left < 0:
            self.left = 0
        elif self.right > 800:
            self.right = 800

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > 600:
            self.top = 600


class Moeda(arcade.Sprite):
    def __init__(self) -> None:
        super().__init__("moeda.png", scale=0.1)
        self.change_x = 0.0
        self.change_y = 0.0


class MoedaEspecial(arcade.Sprite):
    def __init__(self) -> None:
        super().__init__("moeda.png", scale=0.15)
        self.change_x = random.choice([-3.0, 3.0])
        self.change_y = random.choice([-3.0, 3.0])

    def update(self, *args, **kwargs) -> None:
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0 or self.right > 800:
            self.change_x *= -1
        if self.bottom < 0 or self.top > 600:
            self.change_y *= -1


class Inimigo(arcade.Sprite):
    def __init__(self) -> None:
        super().__init__("inimigos.png", scale=0.4)
        self.change_x = 2.5
        self.change_y = 2.5

    def update(self, *args, **kwargs) -> None:
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0 or self.right > 800:
            self.change_x *= -1
        if self.bottom < 0 or self.top > 600:
            self.change_y *= -1


class InimigoEspecial(arcade.Sprite):
    def __init__(self) -> None:
        super().__init__("inimigos.png", scale=0.55)
        self.color = arcade.color.RED
        self.change_x = random.choice([-4.0, 4.0])
        self.change_y = random.choice([-4.0, 4.0])

    def update(self, *args, **kwargs) -> None:
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0 or self.right > 800:
            self.change_x *= -1
        if self.bottom < 0 or self.top > 600:
            self.change_y *= -1


class JanelaJogo(arcade.Window):
    def __init__(self) -> None:
        super().__init__(800, 600, "Sonic: Coletor de Tesouros com Desafios POO")
        self.fundo: arcade.Texture = arcade.load_texture("cenario.png")
        self.setup()

    def setup(self) -> None:
        self.velocidade: float = 6.0 
        self.pontuacao: int = 0 
        self.cronometro: float = 0.0 
        self.jogo_finalizado: bool = False
        
        self.alerta_dano: bool = False
        self.tempo_alerta: float = 0.0

        self.sprite_jog: arcade.SpriteList = arcade.SpriteList() 
        self.lista_moedas: arcade.SpriteList = arcade.SpriteList()
        self.lista_moedas_especiais: arcade.SpriteList = arcade.SpriteList()
        self.lista_inimigos: arcade.SpriteList = arcade.SpriteList()
        self.lista_inimigos_especiais: arcade.SpriteList = arcade.SpriteList()

        self.jogador: Player = Player() 
        self.jogador.center_x = 400 
        self.jogador.center_y = 100 
        self.sprite_jog.append(self.jogador) 

        self.inimigo: Inimigo = Inimigo()
        self.inimigo.center_x = 200
        self.inimigo.center_y = 400
        self.lista_inimigos.append(self.inimigo)

        self.inimigo_especial: InimigoEspecial = InimigoEspecial()
        self.inimigo_especial.center_x = 600
        self.inimigo_especial.center_y = 400
        self.lista_inimigos_especiais.append(self.inimigo_especial)

        for _ in range(25):
            moeda = Moeda()
            moeda.center_x = random.randint(50, 750)
            moeda.center_y = random.randint(50, 550) 
            self.lista_moedas.append(moeda)

        for _ in range(5):
            moeda_especial = MoedaEspecial()
            moeda_especial.center_x = random.randint(50, 750)
            moeda_especial.center_y = random.randint(50, 550)
            self.lista_moedas_especiais.append(moeda_especial)

    def on_draw(self) -> None:
        self.clear()
        
        arcade.draw_texture_rect(self.fundo, arcade.XYWH(400, 300, 800, 600))
        
        self.lista_moedas.draw()
        self.lista_moedas_especiais.draw()
        self.lista_inimigos.draw()
        self.lista_inimigos_especiais.draw()
        self.sprite_jog.draw()
        
        arcade.draw_text(f"Moedas Coletadas: {self.pontuacao}", 10, 570, arcade.color.WHITE, 14)
        arcade.draw_text(f"Tempo: {self.cronometro:.2f}s", 10, 545, arcade.color.WHITE, 14)

        if self.alerta_dano and not self.jogo_finalizado:
            arcade.draw_text("Cuidado! Você foi atingido!", 260, 565, arcade.color.RED, 16, bold=True)

        if self.jogo_finalizado:
            arcade.draw_text("PARABÉNS!", 300, 350, arcade.color.YELLOW, 30, bold=True)
            arcade.draw_text("Você coletou todas as moedas!", 200, 300, arcade.color.WHITE, 20)
            arcade.draw_text(f"Tempo Final: {self.cronometro:.2f}s", 310, 260, arcade.color.GOLD, 18)
            arcade.draw_text("Pressione R para recomeçar ou ESC para sair", 180, 200, arcade.color.WHITE, 16)

    def on_update(self, delta_time: float) -> None:
        if not self.jogo_finalizado:
            self.jogador.update()
            self.lista_moedas_especiais.update()
            self.lista_inimigos.update()
            self.lista_inimigos_especiais.update()
            
            self.cronometro += delta_time

            if self.alerta_dano:
                self.tempo_alerta += delta_time
                if self.tempo_alerta > 1.2:
                    self.alerta_dano = False
                    self.tempo_alerta = 0.0

            moedas_colididas = arcade.check_for_collision_with_list(self.jogador, self.lista_moedas)
            for moeda in moedas_colididas:
                moeda.remove_from_sprite_lists()
                self.pontuacao += 1

            especiais_colididas = arcade.check_for_collision_with_list(self.jogador, self.lista_moedas_especiais)
            for m_especial in especiais_colididas:
                m_especial.remove_from_sprite_lists()
                self.pontuacao += 5
            
            if arcade.check_for_collision(self.jogador, self.inimigo):
                self.alerta_dano = True
                self.tempo_alerta = 0.0
                self.pontuacao -= 2
                self.inimigo.change_x *= -1
                self.inimigo.change_y *= -1

            if arcade.check_for_collision(self.jogador, self.inimigo_especial):
                self.alerta_dano = True
                self.tempo_alerta = 0.0
                self.pontuacao -= 1
                
                self.inimigo_especial.remove_from_sprite_lists()
                
                self.inimigo_especial.center_x = random.randint(50, 750)
                self.inimigo_especial.center_y = random.randint(100, 550)
                self.inimigo_especial.change_x = random.choice([-4.0, 4.0])
                self.inimigo_especial.change_y = random.choice([-4.0, 4.0])
                
                self.lista_inimigos_especiais.append(self.inimigo_especial)

            if len(self.lista_moedas) == 0 and len(self.lista_moedas_especiais) == 0:
                self.jogo_finalizado = True

    def on_key_press(self, key: int, modifiers: int) -> None:
        if key == arcade.key.R: 
            self.setup()
            
        if key in [arcade.key.LEFT, arcade.key.A]: 
            self.jogador.change_x = -self.velocidade
        elif key in [arcade.key.RIGHT, arcade.key.D]: 
            self.jogador.change_x = self.velocidade
        elif key in [arcade.key.UP, arcade.key.W]: 
            self.jogador.change_y = self.velocidade
        elif key in [arcade.key.DOWN, arcade.key.S]: 
            self.jogador.change_y = -self.velocidade

        if key == arcade.key.ESCAPE: 
            arcade.close_window()

    def on_key_release(self, key: int, modifiers: int) -> None:
        if key in [arcade.key.LEFT, arcade.key.RIGHT, arcade.key.A, arcade.key.D]:
            self.jogador.change_x = 0
        if key in [arcade.key.UP, arcade.key.DOWN, arcade.key.W, arcade.key.S]:
            self.jogador.change_y = 0


def main() -> None:
    janela = JanelaJogo()
    arcade.run()

if __name__ == "__main__":    
    main()
