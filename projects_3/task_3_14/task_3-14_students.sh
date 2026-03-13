#!/bin/bash

file="students.txt"

awk '{print $1}' "$file"
echo

awk '{print $2}' "$file"
echo

awk '{print NR, $1}' "$file"
echo
