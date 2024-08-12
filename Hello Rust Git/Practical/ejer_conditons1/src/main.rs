

fn main() {
    older();
    pair_not_pair();
    positive();
    interest();
    days_of_week();
    type_of_int();
    employee_category();
}

fn older() {
    let age :i32 = 12;
    if age > 17 {
        println!("It's an adult, because she/he is: {}",age);
    }
}


fn pair_not_pair() {
    let number :i64 = 13;
    if number % 2==0 {
        println!("It's pair");
    }   
    else {
        println!("It's not pair");
    }
}
fn positive() {
    let number :i64 = 13;
    if number> 0 {
        println!("The number {} is positive", number);
    }
    else {
        println!("The number {} is not positive", number);
    }    
}

fn interest() {
    let money:f64 = 50000000.0;
    let percentage:f64 = 50.0;
    if money>5000000.0 {
        let _result:f64 = (money* percentage)/100.0;
        println!("Reinvest")
    }
    else{
        println!("Not reinvest")
    }
}
fn days_of_week() {
    let _day:i8 = 3;
    if _day == 1 {
        println!("Monday");
    } 
    else if _day == 2 {
        println!("Tuesday"); 
    }
    else if _day == 3 {
        println!("Wednesday");
    }
    else if _day == 4 {
        println!("Thursday");
    }
    else if _day == 5 {
        println!("Friday");
    }
    else if _day == 6 {
        println!("Saturday");
    }
    else if _day== 7 {
        println!("Sunday");
    }
    else {
        println!("Invalid Number")
    }
}

fn type_of_int() {
    let _num:i32 = -1;
    if _num ==0 {
        println!("Neutral")
    }
    else if _num > 0 {
        println!("Positive")
    }
    else {
        println!("Negative")
    }
}
fn employee_category() {
    let category_employee:char = 'f';
    let quantity_children:i64 = 2;
    let money_for_son :i64 = 80000;
    if category_employee == 'A' {
        let money_category: i64  = 3000000;
        let mut _total: i64 = 0;
        _total = (money_for_son * quantity_children) + (money_category - (money_category * 1));
    }
}
