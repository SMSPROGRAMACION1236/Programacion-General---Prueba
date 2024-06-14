


fn main() {
  price();
  three_employees_salary();

  guarany_to_dollar();
  dollar_to_guarany();
  salary_per_hour()
}

fn price () {
  let _price:f64  = 50.0;
  // println!(" Es: {}",_price);

  let _cant:f64 = 5.0;
  let mut _total:f64 = 0.0;
  _total = (_price * _cant) * 1.1 ;
  println!(" El precio total, teniendo en cuenta el IVA del 10 % es: {}",_total);
}

fn three_employees_salary() {
  let _employee1_salary:f64 = 1000.0;
  let _employee2_salary:f64 = 2000.0;
  let _employee3_salary:f64 = 3000.0;
  let _employee1_total_salary :f64 = _employee1_salary *1.1;
  let _employee2_total_salary :f64 = _employee2_salary *1.12;
  let _employee3_total_salary :f64 = _employee3_salary *1.15;
  println!("El salario total del empleado 1 es: {}",_employee1_total_salary);
  println!("El salario total del empleado 2 es: {}",_employee2_total_salary);
  println!("El salario total del empleado 3 es: {}",_employee3_total_salary);
}

fn guarany_to_dollar() {
  let guarany_value:f64 = 150000.0;
  let dollar_value :f64 = 70000.0;

  let change_to_doolar:f64 = guarany_value / dollar_value;
  println!("El cambio de guarani a dollar es: {}",change_to_doolar);    
}

fn dollar_to_guarany() {
  let dollar_value :i64 = 4315;
  let guarany_value :i64 = 7000;
  let change_to_guarany:i128 = (dollar_value * guarany_value).into();
  println!("El cambio de dollar a guarani es: {}",change_to_guarany);
    
}

fn salary_per_hour() {
    let working_hours:i64 = 12;
    let money_per_hour :i64 = 1000;
    let salary :i64 = working_hours * money_per_hour;
    println!("El salario total es: {}", salary)
}