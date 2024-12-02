#[derive(Debug, PartialEq, Eq)]
pub enum Direction {
    Up,
    Down,
    Undirected,
    Unset,
}

fn set_dir(a: i32, b: i32) -> Direction{
    if a < b {
        Direction::Up
    } else if a > b {
        Direction::Down
    } else {
        Direction::Undirected
    }
}

fn check_rep(v: &Vec<&str>) -> bool {
    let mut last_direct = Direction::Unset;
    let mut a = v[0].to_string().parse::<i32>().unwrap_or(0);
    for idx in 1..v.len() {
        let b = v[idx].to_string().parse::<i32>().unwrap_or(0);
        if last_direct == Direction::Unset {
            last_direct = set_dir(a, b);
        }
        let current_direct = set_dir(a, b);
        let good_ord = current_direct == last_direct;
        let good_diff = 1 <= i32::abs(a - b) && i32::abs(a - b) <= 3;
        if !(good_diff && good_ord) {
            return false;
        }
        a = b;
    }
    true
}

fn main() {
    let str_date = include_str!("../input.txt");

    let reports: Vec<&str> = str_date.lines().collect();

    let mut safe_reports = 0;
    let mut l_safe_reports = 0;
    for r in reports{
        let report: Vec<&str> = r.split_whitespace().collect();
        let result = check_rep(&report);
        if result {
            safe_reports += 1;
        } else {
            let mut ok = false;
            for idx in 0..report.len() {
                let sub_reports: Vec<&str> = [&report[..idx], &report[idx+1..]].concat();
                if check_rep(&sub_reports) {
                    ok = true;
                }
            }
            if ok {
                l_safe_reports += 1;
            }
        }
    }

    println!("Safe at the first place: {}", safe_reports);
    println!("Safe after removing a single report: {}", l_safe_reports);
    println!("Total: {}", safe_reports + l_safe_reports);
}
