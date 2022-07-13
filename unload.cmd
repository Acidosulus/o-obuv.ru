rem python obuv.py good "https://o-obuv.ru/tapochki-rozovo-goluboy-edinorog" ".\csvs\test.csv" "1"
python obuv.py catalog "https://o-obuv.ru" ".\csvs\unload.csv" "1"
python obuv.py reverse ".\csvs\unload.csv"
python obuv.py ansi ".\csvs\unload.csv"