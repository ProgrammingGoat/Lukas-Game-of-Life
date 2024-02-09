@echo off

echo Checking if venv exists...

set "venv_path=.\venv"

IF EXIST "%venv_path%" (
    echo Virtual environment exists!
    @echo Activating virtual environment...
    call .\venv\Scripts\activate.bat
    @echo Virtual environment activated!

) ELSE (
    echo Virtual env does not exist. Installing...
    python -m venv venv

    @echo Activating virtual environment...
    call .\venv\Scripts\activate.bat

    echo Installing dependencies...
    python -m pip install -r requirements.txt

    echo Virtual environment installed!
)



@echo Starting program...
python main.py

@echo Deactivating virtual environtment.
deactivate