use std::collections::HashMap;

fn main() {
    let input = include_str!("../input.txt");
    let v: Vec<&str> = input.lines().collect();

    let mut l0: Vec<i32> = vec![];
    let mut l1: Vec<i32> = vec![];

    for a_line in v.into_iter() {
        let res: Vec<&str> = a_line.split_whitespace().collect();
        l0.push(res[0].to_string().parse::<i32>().unwrap_or(0));
        l1.push(res[1].to_string().parse::<i32>().unwrap_or(0));
    }

    l0.sort();
    l1.sort();

    // let mut diff: Vec<i32> = vec![];

    let mut counted = HashMap::new();

    for item in l1.iter() {        
        let count = counted.entry(item).or_insert(0);
        *count += 1;
    }

    let mut res = 0;

    for item in l0.iter() {        
        let count = counted.entry(item).or_insert(0);
        res += *item * *count;
    }

    println!("Your result: {}", res);
}
