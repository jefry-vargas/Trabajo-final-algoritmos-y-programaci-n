# Proyecto Final : Algoritmos y Programación
## Galaga
###### Este proyecto esta realizado por: 
    Andres Felipe Borbon Sierra 
    Jefry Daniel Vargas Sierra 
    Juan Felipe Gualdria Carranza 

# Introducción
¿De casualidad te has peguntado como se hacian los juegos que tanto te entretenian?
es muy probable que tu respuesta sea un si, si estas leyendo esto. En este repositorio vamos a resolverte esa incógnita que puede que hayas tenido desde la primera vez que jugaste un videojuego, asi como tambien el por que decidimos revivir este videojuego de la decada de los 80s, que puede que haya sido la primera experienncia de muchos de nuestros lectores y seguidores.
Entonces por que no empezamos por lo mas importante, ¿Como se crean los videojuegos?, los videojuegos asi como los conocemos, no es solo un muñeco que se mueve y dispara, lo que tenemos que destacar en un videojuego, es su codigo, ya que es donde se almacena, no solo ese movimiento icónico de la nave y los enemigos, sino todo lo que tu ves y que puede que te haya sacado una sonrisa como tambien que hayas golpeado los controles unas 10 veces, todo se encuentra en el codigo, asi que, iniciemos con nuestro proyecto, y descubramos todos los secretos que alberga el juego de galaga, o como muchos puede que lo conozcan, space invaders, pero antes.

# ¿Por que Galaga?
La decision de hacer un galaga surgio de la oportunidad de poder hacerlo y por nuestra porpia curiosidad en la creacion de videojuegos, nos preguntamos, ¿por que no hacemos un galaga? no perdemos nada en intentarlo y seria una gran experiencia para nosotros, no solo como estudiantes, sino como profesionales. De esta simple pregunta nacio la idea de hacer un galaga con todos los conocimientos que teniamos a la mano y los conocimientos que podiamos obtener de todos los medios que teniamos a nuestra disposicion y de esta manera revivirlo y traerlo a un formato virtual y portable para todo el mundo y evitar que este llegue al olvido.

# Programas usados:
## Python:
  <br>
  <img 
       src="https://developers.redhat.com/sites/default/files/styles/large/public/Python-01%20%282%29.png?itok=ZHGBm2C3"
    width="800"
    height="400"
       <br>
Python es un lenguaje de programación imprescindible para cualquier persona que quiera empezar en el mundo del desarrollo web, ya que hablamos de aquel lenguaje dinámico que se desarrolla e implementa en una diversidad de plataformas, en este caso no solo plataformas si no también de aplicaciones. El objetivo principal es la automatización de procesos en el cual se pueda ahorrar el tiempo y por ende la dificultad de un problema, esta totalmente diseñado para trabajar con grandes volúmenes de datos, pues su procesamiento y amplia biblioteca de recursos es ideal para iniciar en la programación. Fue el lenguaje de programación usado en Visual Studio Code para la creacion del proyecto.

## Visual Studio
<br>
  <img 
       src="https://res.cloudinary.com/practicaldev/image/fetch/s--phtox0U7--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://cdn-images-1.medium.com/max/1200/1%2AEOPCay4ML76rIUskd6ZwRg.png"
    width="800"
    height="400"
       <br>
Es un editor de código fuente desarrollado por Microsoft para multiples plataformas. También es personalizable, de modo que los usuarios pueden cambiar el tema del editor, los métodos abreviados de teclado y las preferencias. Cuenta con herramientas de Debug hasta opciones para actualización en tiempo real de nuestro código en la vista del navegador y compilación en vivo de los lenguajes que lo requieran. Su papel fue ser el editor de texto que usamos para el desarrollo del proyecto.

## Pygame
<br>
  <img 
       src="https://www.unipython.com/wp-content/uploads/2017/07/pygame_logo.gif"
    width="800"
    height="236"
       <br>
Pygame es una librería multiplataforma sobre SDL para Python para la implementacion de juegos y aplicaciones de multimedios en 2 dimensiones.
Con sus clases y módulos brinda soporte al desarrollador para importar, tratar y exportar imágenes en varios formatos, IGC y formas básicos, efectos de sonido, reproducción de audio de fondo y CDs, reproducción de video MPEG, tratamiento de eventos de ratón, joystick, teclado, tiempo y otras facilidades que permite rápidez y efectividad para el programador, especialmente si se trata de grupos o empresas pequeños, así como la garantía de soporte para varios sistemas operativos, sin cambios en el código fuente o en la versión compilada para la Máquina virtual de Python.

# Codigo del Galaga
Para el codigo del galaga tuvimos al principio varios percanses, como que al momento de generar los aliens solo generaba 1, o cuando especificabamos que en el siguiente nivel la cantidad fuese el doble de la anterior, aparecieran mas enemigos de los especificados, pero al final todos estos problemas pudimos solucionarlos paso a paso mirando el codigo y revisando que, por casualidad, no hubiese una coma en un lugar donde no debia, pero bueno, hablemos del codigo como tal que podran presenciarlo en el archivo proyect.py en la carpeta del proyecto final.

Bueno, para poder crear el galaga, necesitabamos principalmente la libreria de Pygame y sys con las cuales realizamos ,la implementacion de la apariencia de los enemigos y del jugador y del laser junto a sus respectivos sonidos conmo el disparo del laser del jugador y la colision lase-enemigo; entre las distintas lineas de codigo podemos centrarnos las clases, que son aquellas que desigan la apariencia y la posision y el movimiento de los aliens, el jugador y el laser, y tambien podemos destacar el apartado de bucle principal que es donde se encuentran todas las interraciones con el teclado el cual conecta el movimiento, el disparo y el hecho de iniciar a jugar o pasar de nivel, asi como tambien el hecho de querer volve a jugar en dado caso de haber sido alcanzado por los aliens.
   
# Interfazes del Galaga
## Menu
![menu](https://user-images.githubusercontent.com/102546313/170792391-3e07885a-368c-4dbf-8a6c-aec0084771a0.png)

En este apartado nos centramos en la pantalla de inicio del juego, que bueno, aquellos que hayan jugado en las maquinitas space invaders, sabran que tocaba insertar una moneda para poder empezar a jugar y por este motivo, quisimos acoplar esa idea, solo que en vez de insertar una moneda, simplemente pedimos al jugador que oprima la letra E en su teclado para poder disfrutar del juego.

## Mientras se juega
![in game](https://user-images.githubusercontent.com/102546313/170792375-408e21df-2f38-4c05-8788-5c3566bd481d.png)

En este apartado podemos apreciar el momento en el que, valga la redundancia, estas jugando el juego, donde se puede apreciar, no solo la apariencia de la nave, sino tambien de los enemigos y del laser.

## Pasar de nivel o reiniciar el juego
![next level](https://user-images.githubusercontent.com/102546313/170792335-903fe4ed-d369-42fe-9ebd-9dc41914ef2a.png)

En este apartado y como ultima instancia, vemos el menu que le da a decidir al jugador si desea pasar al siguiente nivel pulsando la letra R en el teclado, en dado caso de que no desee continuar, solo tendria que cerrar la pestaña, lo mismo que podemos hacer al momento de cerrar nuestro navegador preferido.

# Conclusion 

Al momento de pensar en la creacion de un videojuego como el galaga podrian pasar varias cosas por tu mente como, no puedo hacerlo por que no tengo un pc lo suficientemente potente para poder hacerlo, se necesitan muchas cosas para poder crearlo, o simplemente piensas que es muy dificl de realizar, y la verdad no es asi, simplemente tienes que conocer lo mas importante, es decir, conocer las libreria de pygame y sus utilidades, algo que la verdad no es tan complejo como podrias imaginar, y asi tengas errores al principio, o no consigas lo que esperabas, el simple hecho de que no te rindas e intentes crear algo por tus propios medios es suficiente para poder hacer un videojuego, y de tus propios errores aprender de ellos y tomarlos como tu propia experiencia. Tomemos como ejemplo todos los errores que cometimos al momento de hacer el codigo, de todos y cada uno adquirimos experiencia , y eso es lo que nos ayudo a terminar el mismo codigo y el juego en si como lo ven en estos momentos, algo que siempre vamos a recordar como equipo, siendo este nuestro primer paso de muchos que vamos a dar.

# Referencias
Por ultimo, aqui pueden evidenciar los sitios de los que sacamos la informacion y la forma de editar usando la libreria de pygame para realizar el videojuego.

    -Code intef. Obtenido de https://code.intef.es/prop_didacticas/pygame-realizando-juegos-con-python/
    -ecured. Obtenido de https://www.ecured.cu/Python_Game_Library
    -Santander Universidades. Obtenido de https://www.becas-santander.com/es/blog/python-que-es.html
    -ecured. Obtenido de https://www.ecured.cu/Visual_Studio_Code
