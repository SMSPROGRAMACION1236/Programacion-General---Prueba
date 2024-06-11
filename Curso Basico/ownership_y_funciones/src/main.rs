fn main() {
    //Ownership y funciones
    // let s =  String::from("Texto");
    // println!("{}", s);
    // texto(s);
    // println!("Despues de la funcion: {}", s);
    let x = 24;
    numero(x);
    println!("Fuera o despues de la funcion es {}", x);
// En el string nomas crea problemas al momento de hacer imprimir algo de una funcion y luego imprimir fuera o luego de la funcion
}
fn numero(numero: i32){

    println!("Numero debtro de la funcion es : {}", numero)
}
// Si queremos imprimir la variable s en otra funcion
// fn texto(texto:String){ //Parametro tipo string

//     println!("{}", texto);


// }