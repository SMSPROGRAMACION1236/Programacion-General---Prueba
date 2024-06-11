fn main() {
    // COPIAR DAT0S DEL STACK//
    let x = String::from("Cadena");
    let y = x.clone(); // Clone para copiar exactamente el valor  o sea el texto

    println!("{}", x);
    println!("{}", y);
  
  // Tienen inherente copiar int, bool, float, caracter, tupla solo los STR String
}
//   let X = 5;
//     let y = X;