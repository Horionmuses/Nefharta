# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bgfonbosque

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    "Mi madre está enferma, así que no tuve más opción que dejar mi pueblo atrás. Con un saco lleno de piedras de amor —mi única mercancía—"
    "Emprendí el viaje con la esperanza de ganar lo suficiente para su medicina. No pasó mucho tiempo antes de que el destino me pusiera en el camino de dos personas."

    show juana normal
    "La primera persona era una chica rubia con cabellos dorados."

    juana "¿Hum...? Hola, ¿estás perdido?"

    "Digamos que sí... Estoy buscando un lugar donde poder vender piedras de amor."

    # juana sorprendida
    juana "¿¿Piedras de amor??"
    hide juana normal
    show Takashiel
    v "Esas piedras son muy difíciles de conseguir y el gas de las montañas del amor es tóxico."
    hide Takashiel
    show juana normal
    juana "¡Demasiado tóxicas para tener esa cantidad!"
    hide juana normal
    show Takashiel
    v "De donde vengo, valen mucho."
    hide Takashiel
    show juana rara
    juana "Nefharta... No sé si debería ir allá."
    "¿Nefharta? ¡No puede ser! En mi pueblo, los clientes más generosos siempre vienen de ese reino."
    show juana normal
    juana "Si es así... ¡Deberías ir! Así podrás vender esas piedras a un buen precio."
    hide juana normal
    show Takashiel
    v "¡Yo podría llevarte! Justo tengo que ir para allá."
    hide Takashiel
    
    menu:
        "Preferiría que me lleve la señorita... me da más seguridad":
            jump juanafeliz
        "¡Sí, claro! Muchas gracias.":
            jump vifeliz

label vifeliz:
        show juana rara at left
        show Takashiel at right
        v "¡Perfecto! Entonces, vámonos."
        hide juana rara
        hide Takashiel
        jump caminoanefharta_vi
        
label juanafeliz:
        show juana rara at left
        show takaenojado at right
        juana "¡Genial! Te acercaré lo más que pueda a Nefharta."
        hide juana rara
        hide takaenojado
        jump caminoanefhartajuana

label caminoanefharta_vi:
    show Takashiel
    v "Asique..."
    "Asique...?"
    v "Como te llamas?"
    "Me llamo ... y tu?"
    v "Yo soy Takashiel, pero mis amigos me dicen Vi."
    v "aunque tu no tienes derecho de decirme asi."
    #si no pones el jump a que te lleve a una zona, este te saltara a el camino de juana porque es el que sigue owo!
    hide Takashiel
    jump final_del_juego

label caminoanefhartajuana:
    scene bgfonbosquenoche
    show juana rara
    juana "Perdona, pero no voy a poder entrar al pueblo contigo, así que te dejaré lo más cerca de la entrada."
    "Tal vez es un poco incómodo lo que voy a preguntar, pero... ¿por qué no puedes ir?"
    juana "Es una larga historia..."
    "¿Fuiste desterrada? —tono de broma—"
    show juana enojada
    juana "..."
    hide juana enojada
    "Se puso algo incómoda por un rato, pero luego seguimos hablando."
    "Me pregunto..."
    #Esto no esta verificado la ortografia owo
    show juana normal
    "Me pregunto como una persona que se ve tan amable fuera desterrada."
    juana "Bueno estamos en el bosque Violeta."
    scene bgbosquevioleta with fade
    "Wow..es sorprendente"
    show juana rara
    juana "hum..."
    "¿Y esa cara?"
    juana "ten...mucho cuidado, dicen que cualquier ser con alma puede perderse para siempre en este bosque."
    menu:
        "Tranquila linda estare bien":
            jump alago
        "Estare bien, no creo que sea tan dificil.":
            jump tranquilidad
label alago:
    show juana normal
    juana "Eso...se sintio bonito, espero volver a verte."
    "nos vemos..."
    juana "Mi nombre es Juana, fue un placer conocerte"
    hide juana normal with dissolve
    "Asi fue como me quede mirando la entrada..."
    jump tomoe
label tranquilidad:
    show juana rara
    juana "todos dicen eso..."
    hide juana rara with dissolve 
    jump tomoe
label tomoe:
    "Comence a caminar confundido."
    "El aire se siente denso y despues de unos minutos caminando ya me siento raro.
    Sera que todo lo que dicen de este bosque es verdad..."
    e "¿Estas perdido humano?"
    "EH??"
    e "Se ve que es la primera vez que entras al bosque violeta."
    "¿¿QUE ERES??"
    e "Es verdad aun no me vez..."
    show tomoe with fade
    t "Soy tomoe un gusto..."
    "(E-es un Zorro...)"
    t "Soy mas que eso"
    "LEISTE MI MENTE"
    t "tu mente no, tu alma... me presento soy el protector y dueño de este bosque"
    "Dueño de este bosque?..."
    "¿pasa algo?"
    #show tomoe with fade

label final_del_juego:
    scene black
    "TERMINA EL CAPITULO 1"