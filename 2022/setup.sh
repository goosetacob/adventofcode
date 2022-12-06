#!/bin/bash
if [ -z ${1+x} ];
then echo "error: ./setup.sh DD"; exit 0;
fi

cp ./01.go ./$1.go
cp ./01.input.txt ./$1.input.txt
