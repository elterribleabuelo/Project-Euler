def main(cota):
    found = False
    while found == False:
        k = 286
        j = 165
        i = 144
        T_k = (pow(k,2) + k)//2
        P_j = (3*pow(j,2) - j)//2
        H_i = 2*pow(i,2) - i
        if T_k==P_j==H_i:
            print("i,j,k",i,j,k)
            print("numero:",T_k)
            found = True
        k +=1
        j +=1
        i +=1

cota = 1500
main(cota)