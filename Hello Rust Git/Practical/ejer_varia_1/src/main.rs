


fn main() {
  println!("First Exercise");
  price();
  println!("Second Exercise");
  three_employees_salary();
  println!("Third Exercise");
  guarany_to_dollar();
  println!("Fourth Exercise");
  dollar_to_guarany();
  println!("Fifth Exercise");
  salary_per_hour();
  println!("Sixth Exercise");
  sum_two_values_divided_by_one_value();
  println!("Seventh Exercise");
  salary_increased();
  println!("Eighth Exercise");
  basic_arithmetic_operation();
  println!("Nineth Exercise");
  earn_30percentage();
  println!("Tenth Exercise");
  total_invest();
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

fn sum_two_values_divided_by_one_value() {
    let num1 :f64 = 4.0;
    let num2 :f64 = 2.0;
    let num3 :f64 = 2.0;

    let result_after_adding_and_divided:f64 = (num1+ num2) / num3 ;
    println!("The result after adding the first and second value and divided by the third value is: {}",result_after_adding_and_divided);
}

fn salary_increased() {
  let base_salary :f64 = 10000.0;
  let percentage:f64 = 1.25;

  let final_salary: f64 = base_salary * percentage;

  println!("The salary after increased 25% is: {}",final_salary)
}


fn basic_arithmetic_operation() {

  let value1 :f64 = 5.0;
  let value2:f64 = 3.0;

  let add: f64 = value1 + value2;
  let subtract: f64 = value1 - value2;
  let multiply: f64 = value1 * value2;
  let divide: f64 = value1 / value2;

  println!("The adding of the two values is: {}",add);    
  println!("The subytract of the two values is: {}",subtract);    
  println!("The multiply of the two values is: {}",multiply);    
  println!("The divide of the two values is: {}",divide);    
}

fn earn_30percentage(){
  let buying_price :f64 = 10000.0;
  let selling_price:f64 = buying_price *1.3;

  println!("He must sell it with a price of: {}",selling_price);

}

fn total_invest() {
  let person1 :f64 = 100.0;
  let person2 :f64 = 80.0;
  let person3 :f64 = 120.0;
  let total_invested :f64 = person1 + person2 + person3;
  let person1_percent :f64 = (person1 /total_invested) *100.0;
  let person2_percent :f64 = (person2 /total_invested) *100.0;
  let person3_percent :f64 = (person3 /total_invested) *100.0;

  println!("The person number 1 has invested: {} percentage",person1_percent);
  println!("The person number 2 has invested: {} percentage",person2_percent);
  println!("The person number 3 has invested: {} percentage",person3_percent);
}