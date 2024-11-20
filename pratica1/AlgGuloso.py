coins = [1, 2, 5, 10, 20, 50, 100]  # Representa as moedas em centavos


def Algoritmo_Guloso(value):
    value = int(value * 100)  # Converta o valor para centavos
    change = []  # Lista com as moedas do troco
    while value > 0:
        i = len(coins) - 1
        while True:
            possibleCoin = coins[i]
            if possibleCoin <= value:
                value -= possibleCoin
                change.append(
                    possibleCoin / 100
                )  # Volta para reais ao adicionar à lista
                break
            else:
                i -= 1
    return change


change = Algoritmo_Guloso(1.1)
print(change)
