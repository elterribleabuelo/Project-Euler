def contar_formas(amount,method = "tabulation"):
    
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    if method == "tabulation":
    
        formas = [0] * (amount + 1)
        
        formas[0] = 1
        
        for moneda in coins:
            for i in range(moneda, amount + 1):
                formas[i] += formas[i - moneda]
        
        print(f"El número de maneras diferentes de obtener {amount} es: {formas[amount]}")

        return formas[amount]
    
    elif method == "memorization":
        
        table = [[0] * len(coins) for _ in range(amount + 1)]
        table = [[1] + fila[1:] for fila in table]
        
        for i in range(amount + 1):  # i = 4
            for j in range(1,len(coins)): # j = 1
                table[i][j] = table[i][j-1] # table[4][1] = table[4][0] = 1
                if coins[j] <= i:
                    table[i][j] = table[i][j] + table[i - coins[j]][j] # table[4][1] + table[2][1]
        
        print(f"El número de maneras diferentes de obtener {amount} es: {table[i][j]}")
        return table[i-1][j-1]

amount = 200
maneras = contar_formas(amount,"memorization") # 73682