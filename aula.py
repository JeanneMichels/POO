import arcade
ALTURA = 600
LARGURA = 800
TITULO = "BAGUIO"

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("sonic_direita.png", scale=1)
        self.textura_direita = arcade.load_texture("sonic_direita.png")
        self.textura_esquerda = arcade.load_texture("sonic_esquerda.png")

        def update(self):
            pass

class JanelaJogo(arcade.Window):
    def __init__(self):
        super().__init__(LARGURA, ALTURA, TITULO)
        arcade.set_background_color((0, 100, 30))
        self.personagem = Player()
        self.personagem.center_x =  100
        self.personagem.center_y = 200

    def on_draw(self) :
        self.clear()
        arcade.draw_sprite(self.personagem)
    
    def on_update(self, delta_time):
        pass


def roda():
    tela = JanelaJogo()
    arcade.run()

if __name__ == "__main__": 
    roda()