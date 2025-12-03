use anyhow::Result;

pub fn solve(input: &str) -> Result<String> {
    // 0 - 99
    // start 50
    // LXX => -XX
    // RXX => +XX
    let rotations: Vec<i32> = input
        .split_whitespace()
        .into_iter()
        .map(|s| {
            if let Some(num_str) = s.strip_prefix('L') {
                -num_str.parse::<i32>().expect("invalid number")
            } else if let Some(num_str) = s.strip_prefix('R') {
                num_str.parse::<i32>().expect("invalid number")
            } else {
                panic!("invalid direction")
            }
        })
        .collect();

    let mut dial_position: i32 = 50;
    let mut at_zero_count = 0;
    for rotation in rotations.iter() {
        let old_position = dial_position;
        dial_position += rotation;

        let crossings = if *rotation >= 0 {
            // R: count multiples of 100 in (old, new]
            dial_position.div_euclid(100) - old_position.div_euclid(100)
        } else {
            // L: count multiples of 100 in [new, old)
            (old_position - 1).div_euclid(100) - (dial_position - 1).div_euclid(100)
        };

        at_zero_count += crossings;
    }

    Ok(at_zero_count.to_string())
}
