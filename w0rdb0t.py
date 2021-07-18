"""
   *** Author: Eduardo. ***
   *** Alias: H3x4b1t. ***
   *** Script para generar un diccionario que va desde el 0000AAAA - 9999ZZZZ. ***
   *** Aviso: Para completar el diccionario se necesita una capacidad de procesamiento elevada, sino no se completará con éxito el diccionario. ***
   *** Y también será necesario bastante memoria RAM, con pruebas realizadas calculamos necesarios unos 64 Gb RAM para poder finalizar el diccionario. ***
   *** Además de tener instalado el Python de 64 bits.
"""
#LOS PRINTS COMENTADOS SON LOGS PARA HACER PRUEBAS, SI QUIERES HACER PRUEBAS CON EL SCRIPT DESCOMENTALOS O PONLOS COMO MEJOR TE AYUDEN.
#SI NO VAS A HACER PRUEBAS, NO ES NECESARIO QUE DESCOMENTES NINGÚN PRINT.

finally_list = []
letras_actual = "AAAA"

def creador_diccionario_final():

    num_init = 0
    num_total = 9999
    num_matricula = 0000
    num_matr = ""
    letras_actual = "AAAA"
    wordlist = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    four_word_block = []
    one_word = "A"
    two_word = "A"
    three_word = "A"
    four_word = "A"
    backup_list = []
    contador_letras1 = 0
    contador_letras2 = 0
    contador_letras3 = 0
    contador_letras4 = 0


    try:
        while letras_actual != "ZZZZ":

            while num_init <= num_total:

                num_matr = "" + str(num_matricula).zfill(4)
                four_word_block.append(num_matr + letras_actual)
                #print(letras_actual + " estoy dentro del segundo bucle")
                num_matricula += 1
                num_init += 1

            #print(four_word)
            #print(three_word)
            #print(two_word)
            #print(one_word)

            if four_word == "Z":
                #print(four_word)
                contador_letras4 = 0
                four_word = wordlist[contador_letras4]
                #print(four_word)
                #print(letras_actual + " bloque 4")

                if three_word == "Z":
                    contador_letras3 = 0
                    three_word = wordlist[contador_letras3]
                    #print(three_word)
                    #print(letras_actual + " bloque 3")

                    if two_word == "Z":
                        contador_letras2 = 0
                        two_word = wordlist[contador_letras2]
                        #print(two_word)
                        #print(letras_actual + " bloque 2")

                        if one_word == "Z":
                            #print(one_word)
                            #print(letras_actual + " bloque 1")
                            continue
                            #contador_letras1 = 0
                            #one_word = wordlist[contador_letras1]
                        else:
                            contador_letras1 += 1
                            one_word = wordlist[contador_letras1]
                            #print(one_word)
                            #print(letras_actual + " bloque 1 del else")

                    else:
                        contador_letras2 += 1
                        two_word = wordlist[contador_letras2]
                        #print(two_word)
                        #print(letras_actual + " bloque 2 del else")

                else:
                    contador_letras3 += 1
                    three_word = wordlist[contador_letras3]
                    #print(three_word)
                    #print(letras_actual + " bloque 3 del else")

            else:
                contador_letras4 += 1
                four_word = wordlist[contador_letras4]
                #print(four_word)
                #print(letras_actual + " bloque 4 del else")

            letras_actual = one_word + two_word + three_word + four_word

            #print(four_word)
            #print(three_word)
            #print(two_word)
            #print(one_word)
            print(letras_actual)

            num_init = 0
            num_matricula = 0

        finally_list.append(four_word_block)

    except MemoryError:
        print("Cierre del programa por no tener suficiente capacidad de procesamiento.")


def mod_fichero():
    fo = open("diccionario_matriculas2.txt", "w")
    lista_limpia = str(finally_list).strip('[]')
    fo.write(lista_limpia)
    fo.close()

def main():
    creador_diccionario_final()
    mod_fichero()

if __name__ == '__main__':
    main()