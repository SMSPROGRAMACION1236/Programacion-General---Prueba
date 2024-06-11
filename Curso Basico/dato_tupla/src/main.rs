fn main() {
    //Tuplas
    let tupla: (i32, f64, char, bool)=(24, 3.14159265, 'a', false); // el primer parametro es de int, el segundo es float, el tercero es str y el cuarto es bool
    println!("Tupla: {}", tupla.0); // tupla.numero de indice en la que quieres acceder
    println!("Tupla: {}", tupla.1);
    println!("Tupla: {}", tupla.2);
    println!("Tupla: {}", tupla.3);

    let (_a, b, _c, _d)=tupla;
    println!("Tupla: {}", b)


}
