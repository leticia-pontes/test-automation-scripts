@echo off

cd /d %~dp0scripts\python\

echo Rodando testes em Python...
python -m unittest test_gerador_numeros_primos.py
set PYTHON_RESULT=%ERRORLEVEL%

if %PYTHON_RESULT%==0 (
    echo Todos os testes passaram com sucesso!
) else (
    echo Alguns testes falharam.
)

rem Verifique a pontuação de 90%
rem Adicione sua lógica aqui para calcular a pontuação
rem Exemplo: 
set SCORE=95
rem Suponha que essa variável represente a pontuação

echo A pontuacao foi de %SCORE%%%.

pause
