use regex::Regex;

fn mul(xy: &str) -> i32 {
    let col: Vec<&str> = xy.split(',').collect();
    col[0].to_string().parse::<i32>().unwrap_or(0) * col[1].to_string().parse::<i32>().unwrap_or(0)
}

fn main() {
    // let txt = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";
    let in_data = include_str!("../input.txt");

    let pattern = r"mul\(\d{1,3},\d{1,3}\)";
    let re = Regex::new(pattern).unwrap();

    // let dates: Vec<&str> = re.find_iter(txt).map(|m| m.as_str()).collect();
    let mut total = 0;
    for item in re.find_iter(in_data) {
        let current = item.as_str();
        let p = r"\d{1,3},\d{1,3}";
        let subre = Regex::new(p).unwrap();
        let res = subre.find(&current).unwrap().as_str();
        total += mul(res);
    }
    println!("{}", total)
}
