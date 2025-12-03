use anyhow::Result;
use std::fs;

mod part1;
mod part2;

fn main() -> Result<()> {
    let input_filename = "input.txt";
    let input_path = std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join(input_filename);
    let input = fs::read_to_string(&input_path)?;

    println!("Part 1: {}", part1::solve(&input)?);
    println!("===");
    println!("Part 2: {}", part2::solve(&input)?);

    Ok(())
}
