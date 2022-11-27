from GameTwo import Game

class Main:
    game = Game()
    game.initialization()
    lost = False

    print(game.grid)
    print("Welcome to 2048 game!")

    def display(game):
        largest = game.grid[0][0]
        for row in game.grid:
            for ele in row:
                if ele > largest:
                    largest = ele

        numspaces = len(str(largest))
        for row in game.grid:
            currRow = "|"
            for ele in row:
                if ele == 0:
                    currRow+= " " * numspaces + "|"
                else:
                    currRow += str(ele) + "|"
            print(currRow)
    
    display(game)

    while lost != True:
        action = input("Choose your movement: ")

        game.determine_movement(action)

        display(game)

        if game.won():
            print("Congrats! You win!")
            break
        elif game.no_move() == False:
            game.random_generator()
            continue
        else:
            print("Game over. Lost")
            break

    
        
        

