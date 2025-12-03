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
        println!("-");
        println!("dial_position: {}", dial_position);
        println!("rotation: {}", rotation);
        dial_position += rotation;

        at_zero_count += dial_position.div_euclid(100).abs();
        dial_position = dial_position.rem_euclid(100);

        println!("dial is rotated {} to {}", rotation, dial_position);
        println!("crossings: {}", dial_position.div_euclid(100).abs());
        println!("at_zero_count: {}", at_zero_count);
    }

    Ok(at_zero_count.to_string())
}
