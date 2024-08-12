fn main() {
    //ownership//
        // STACK//

        //HEAP //
        //REGLAS//
            /*
            - Cada valor tiene una variedad la cual es su propietario.
            - Solo puede haber un propietario a la vez
            - SI el propietario sale de su ambito de valor es eliminado
            } 
            */
        //AMBITO
       
        {  
             let  s= 5;
             println!("{}", s);
        }
// SI esta declarada la variable en {} y la impresion fuera habra un error ya que es como si fuera que la  variable no existe
// println!("{}", s); Error
        




}