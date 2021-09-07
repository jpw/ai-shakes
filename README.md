# ai-shakes

From https://github.com/minimaxir/aitextgen
 see https://docs.aitextgen.io/dataset/

## setup
```
python3 -m venv env
source env/bin/activate
which python
pip3 install aitextgen
deactivate
```

## to run

See the various Python scripts, or using the defaults via the shell:

`aitextgen generate --to_file False --n 2 --temperature 1.7 --prompt "Miffy went to the gallery and"`

### MBP benchmark

training shakes started at 19:40, %CPU ~155
    finished around 21:00
