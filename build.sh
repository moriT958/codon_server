codon build -release -o codon_bin/random_nums ./src/codon_server/random_nums.py

rye run ruff format
rye run ruff check

rye run python ./src/codon_server/main.py