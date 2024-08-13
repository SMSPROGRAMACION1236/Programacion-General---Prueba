// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
// Press Alt+Enter with your caret at the highlighted text to see how
        // IntelliJ IDEA suggests fixing it.
        System.out.println("Hello Jesus");
        System.out.println("Hola");
        System.out.println();

        //* Sintaxis basica de Variables de Java
        //tipo nombre = valor;
        // byte acepta datos del -128 al 127
        byte num1 = 100; // Aca lo hacemos en la misma linea de codigo

        // Aqui en diferentes lineas de codigo
        byte numx;
        numx = -23;
        System.out.println(numx);
        // Cambial el valor de una variable
        num1 = 43;

        System.out.println(num1); //  sirve para imprimir lo que esta dentro de la variable
        // java es sensible a las mayusculas y minusculas.

        //* Tipos de Datos //

        // Byte: Numeros mas chicos en java,  desde -128 a 127, en la memoria ram ocupa un byte
        //! no se puede puesto que 1201 es mucho mayor al valor que puede soportar byte
        //byte sum = 1201;
        //System.out.println(sum);

        //short: Datos chicos pero no tanto como el byte, desde -32768 a 32767, ocupa 2 bytes
        short sum = 31244;
        System.out.println(sum);

        //int: datos mas grandes,  desde -2.147.483.648 a 2.147.483.647, ocupa 4 bytes

        int hola3 = 35243240;
        System.out.println(hola3);


        //long: es que almacena la mayor cantidad desde -9.223.372.036.854.775.808 a  9.223.372.036.854.775.807, es de 8 bytes
        long hola4 = 345433332003432L; // se debe de poner el L, para usar cifras grandes, al imprimirlo no sale en la pantalla

        System.out.println(hola4);

        //float: tipo de datos integran de 4 bytes, almacena valores hasta 7 digitos decimales.
        float hola5 = 243.242F;  // debemos de poner la F, o sino el programa va a identificar como un tipo de dato double
        System.out.println(hola5);

        //double: valores decimales de hasta 15 digitos, ocupa 8 bytes

        double hola6 = 34.2343241325425;
        System.out.println(hola6);

        //char: ocupa 2 bytes, almacena caracteres, solo un caracter

        char hola7 = '♣';  // debemos usar comillas simples, si usas dobles lo tratara como un string
        System.out.println(hola7);

        //boolean: Solo puede ser true o  false, es decir solo dos valores, ocupan un solo byte

        boolean hola8 = false;
        System.out.println(hola8);


        //*Tipos de Comentarios /

        // De una sola linea: //Hola, esto es un comentario
        //Comentarios multilinea : /* */
        /* Esto es
        un comentario
        que abarca
        muchas
        lineas

         */


        //* Constantes en java //
        // su valor es constante, no puede cambiar con el tiempo, es decir le damos un valor inicial y nunca cambia, el nombre de las constantes se pone en mayusculas por una buena practica
        final  double PI = 3.14; // final luego el tipo de dato y al final el nombre de la variable
        System.out.println(PI);

//!        PI = 34  No se puede ponerle otro valor
        // se puede inicializar una variable sin ningun valor, y luego en otra linea, pero solo una vez
        final  double euler;
        euler = 2.71;
        System.out.println(euler);

        //* Operaciones aritmeticas
        System.out.println(10 +1); // se puede imprimir directamente
        //? Se usa normalmente el tipo de dato int para variables

        int numero1 = 12;
        int numero2 = 15;

        int resultado = numero1 + numero2;  // suma
        System.out.println(resultado);

        resultado = numero1 - numero2;// resta
        System.out.println(resultado);

        resultado = numero1 * numero2;// multiplicacion
        System.out.println(resultado);

        resultado = numero1 / numero2;// division
        System.out.println(resultado);


        //* Operaciones comparadores: se usa tipo boolean, y sirve para tomar desiciones logicas, si es falso se hace algo y si es verdadero otra cosa
        boolean comparacion = 20 > 10; // Comparacion es una variable de tipo boolean
        /* Un numero valor(izquierda) operacion de comparacion  valor(derecha) ---> boolean
        > mayor
        < menor
        != difererente
        == igual
        >= igual o mayor
        <= igual o menor
        */
        System.out.println(comparacion);

        // Comparando dos variables
        byte numero1x = 10;
        byte numero2x  =20;
        boolean comparacionx = numero1x <= numero2x;
        System.out.println(comparacionx);
        comparacionx = numero1x >= numero2x;
        System.out.println(comparacionx);
        comparacionx = numero1x == numero2x;
        System.out.println(comparacionx);
        comparacionx = numero1x != numero2x;
        System.out.println(comparacionx);

    }
}