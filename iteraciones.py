contador_externo = 1
contador_interno = 1

while contador_externo < 12:
    while contador_interno < 60:
        print(contador_externo, contador_interno)
        contador_interno += 1

        # if contador_interno >= 3:
        #     break

    contador_externo += 1
    contador_interno = 0