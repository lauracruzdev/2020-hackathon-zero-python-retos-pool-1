from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    
    if player == ai:
        return "Empate!"
    elif player == "Piedra" and ai == "Tijeras":
        return "Ganaste!"
    elif player == "Papel" and ai == "Piedra":
        return "Ganaste!"
    elif player == "Tijeras" and ai == "Papel":
        return "Ganaste!"

    if player == "Piedra" and ai == "Tijeras":
        return "Perdiste!"
    elif player == "Papel" and ai == "Piedra":
        return "Perdiste!"
    elif player == "Tijeras" and ai == "Papel":
        return "Perdiste!"
   
# Entry Point
def Game():
    
    player = input("Elige Piedra, Papel o Tiejeras: ")
    player = player.lower()

    ai = random.choice(options)

    
    winner = quienGana(player, ai)

    print(winner)

