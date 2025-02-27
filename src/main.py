from src.player import Player
from src.shooting_game import ShootingGame

def main():
    game = ShootingGame()

    # เพิ่มผู้เล่น 3 คน
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    player3 = Player("Player 3")

    game.add_player(player1)
    game.add_player(player2)
    game.add_player(player3)

    # เริ่มเกม
    game.run()

if __name__ == "__main__":
    main()
