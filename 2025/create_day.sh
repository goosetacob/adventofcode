#!/bin/bash
if [ -z ${1+x} ]; then
    echo "Usage: ./create_day.sh DD"
    echo "Example: ./create_day.sh 05"
    exit 1
fi

DAY=$1
DIR="day$DAY"

cp -r day00 $DIR;

# update day00 to day02 in $DIR/Cargo.toml
sed -i '' "s/day00/$DIR/g" $DIR/Cargo.toml

# append to workspace members
tomato append workspace.members $DIR ./Cargo.toml

echo "Created day$DAY"
echo "Next steps:"
echo "  1. Add input to $DIR/sample_input.txt"
echo "  2. Run: cargo run --bin $DIR"
