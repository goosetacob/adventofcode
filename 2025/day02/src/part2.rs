use anyhow::Result;

// identify any number which is made only of some sequence of digits repeated twice
pub fn has_repeated_sequence(n: u64) -> bool {
    let seq = n.to_string();
    let seq_len = seq.len();

    for pattern_len in 1..=(seq_len / 2) {
        let pattern = &seq[..pattern_len];
        let repetitions = seq_len / pattern_len;

        if pattern.repeat(repetitions) == seq {
            return true;
        }
    }

    false
}

pub fn solve(input: &str) -> Result<String> {
    let ranges: Vec<(u64, u64)> = input
        .trim()
        .split(',')
        .into_iter()
        .map(|range| {
            // DDD-DDDD
            let range_parts: Vec<&str> = range.split("-").collect();
            (
                range_parts[0].parse::<u64>().expect("invalid number"),
                range_parts[1].parse::<u64>().expect("invalid number"),
            )
        })
        .collect();

    let mut invalid_ids = vec![];
    for range in ranges {
        println!("{:?}", range);
        for n in range.0..=(range.1 + 1) {
            let is_invalid = has_repeated_sequence(n);
            if is_invalid {
                println!("n: {:?} is_repeated_sequence: {}", n, is_invalid,);
                invalid_ids.push(n);
            }
            // println!("n: {:?} is_repeated_sequence: {}", n, is_invalid,);
        }
    }

    println!("invalid_ids: {:?}", invalid_ids);
    let invalid_ids_sum: u64 = invalid_ids.iter().sum();
    Ok(invalid_ids_sum.to_string())
}
