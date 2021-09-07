# ai-shakes

From https://github.com/minimaxir/aitextgen
 see https://docs.aitextgen.io/dataset/

## setup
```
python3 -m venv env
source env/bin/activate
which python
pip install --upgrade pip
pip3 install aitextgen
deactivate
```

## to run

See the various Python scripts, or using the defaults via the shell:

`aitextgen generate --to_file False --n 2 --temperature 1.7 --prompt "Miffy went to the gallery and"`

### MBP benchmark

On MBP, training shakes took ~80 minutes with %CPU ~155.
On new Mac Mini took ~30 minutes with %CPU ~169.
