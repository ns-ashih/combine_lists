# combine_lists

A simple command-line tool to generate text combinations from multiple `.txt` files.

Each input file contains one item per line.  
The script generates all valid combinations using a Cartesian product, with support for **optional lists whose elements may appear or be skipped**.

## Features

- Accepts multiple input `.txt` files
- Supports required and optional lists
- Easy-to-use command-line interface
- Clean, predictable output format
- No external dependencies

## Input format

Each input file should contain **one item per line**.

Example:

`fruits.txt`  
apple  
mango

`drinks.txt`  
juice  
smoothie

`modifiers.txt`  
fresh  
cold

## Usage

### Basic usage

```bash
python combine_lists.py fruits.txt drinks.txt
```
This generates combinations using only required lists and writes to output.txt.

### With optional lists
```bash
python combine_lists.py \
  fruits.txt \
  drinks.txt \
  --optional modifiers.txt \
  -o output.txt
```
In this case, each element in modifiers.txt may appear or not appear in the output.

## Output example
```
apple juice
apple juice fresh
apple juice cold
apple smoothie
apple smoothie fresh
apple smoothie cold
mango juice
mango juice fresh
mango juice cold
...
```

## Arguments

### Positional arguments
- `required`
    - One or more required .txt files.
    
### Optional arguments
- `--optional`
    - Zero or more optional .txt files.
    - Elements from these files may appear or be skipped.
- `-o`, `--output`
    - Output file path. Default: output.txt
