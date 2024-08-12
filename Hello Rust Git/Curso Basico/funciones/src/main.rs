fn main() {
    // Funciones //

    
    println!("La suma de 20 y 4 es: {}", sumar(20, 4));  // le pasamos los datos que debe sumar



    // saludar("Santiago"); 
    // saludar("Mario"); 
    // saludar("Elias");  Descomentar

    // let x = 123; // es una setencia
    // 4 > 1; Es una expresion ya que debe devolver true o false
    //Parametros
    //BODY, STATEMENTS & EXPRESSION//
    //RETUNR VALUES
}

// Debemos de especificar el tipo de dato luego de poner  un parametro

// fn saludar(nombre: &str) {  // debemos de poner luego en la funcion main para que asi lo tome en cuenta
    

//     println!("Hola {}", nombre);
// }

fn sumar(num1:i32, num2:i32) ->i32  // decir que clase de datos nos tiene que retornar
{

    num1 + num2  // no lleva ;
}b