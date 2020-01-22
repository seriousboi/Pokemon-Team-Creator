cd compiled
rmdir /q/s data
del PokemonTeamCreator.exe
mkdir data
pyinstaller -w -F -i ../data/icons/turtwig_icon.ico ../main.py
cd dist
copy main.exe ..
cd ..
Xcopy /E /I ..\data data
rmdir /q/s build
rmdir /q/s dist
del main.spec
rename main.exe PokemonTeamCreator.exe
cd ..
