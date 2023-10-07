fn main() {
   //Strings y Alojamiento de Memoria
   {
        let mut cadena = String::from("ESTE ES UNA CADENA DE TEXTO");
        cadena.push_str("MAS TEXTO"); // Para agregarle texto extra

        println!("{}", cadena);

        let x= String::from("Esta es X");

        let y = x;
        // println!("x: {}", x);
        println!("y: {}", y); // Y adquiere la direccion de memoria de x y no su valor
   }
   
}
