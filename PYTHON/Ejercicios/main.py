from hangman import Hangman


hangman_game= Hangman()
hangman_game.load('./files/words.csv')
hangman_game.play()