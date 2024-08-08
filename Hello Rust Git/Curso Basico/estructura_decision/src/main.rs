fn main() {
    // Estructuras de desicion
    let edad = 16;
    

    if edad < 16 {  // Siempre verifica la primera luego los demas decisiones
        println!("Menor de edad");
    } 
    else if edad == 16 { // similar a elif
        println!("Menor de edad pero puede conducir");


    }
    else{  

        println!("Es mayor de edad");
    }


    
    let expression = 5>1;
    if expression {
        println!("cool");
    }


    let number: f64 = if 5<1{ 5.3 } else {1.3};  //todos los datos deben ser lo mismo es decir todos int o todos floats

    println!("{}", number);
}

