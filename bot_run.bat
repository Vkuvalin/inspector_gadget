@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd  %~dp0telegram_bot

set TOKEN=5194627649:AAEmIdgm6SjKA0Yxm_tVYQEDOO5blCakuuE
set admin_id=5009372827

python main.py

pause