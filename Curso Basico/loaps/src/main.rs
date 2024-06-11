use std::arch::x86_64::_mm256_load_pd;

fn main() {
    // Interaciones con: Loop
    let mut i = 0;   
     loop{
        println!("Mensaje");
        if i == 5 // en el momento que valga 5 se detendra
        {
            break;
        }
        i+=1; // se suma 1 a 1|
    }


    let suma = loop {
        if i==10 {
            break i;
        }
        i+=1;
    };
    println!("suma: {}", suma);
}
