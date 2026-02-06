@echo off
echo ========================================
echo   SISTEMA DE CAIXA - INICIANDO
echo ========================================
echo.

if not exist "venv" (
    echo ERRO: Ambiente virtual nao encontrado!
    echo Execute primeiro: instalar.bat
    pause
    exit /b 1
)

echo Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo Iniciando servidor Flask...
echo.
echo ========================================
echo   SISTEMA RODANDO!
echo ========================================
echo.
echo Acesse no navegador: http://localhost:5000
echo.
echo Usuario: admin
echo Senha: 123
echo.
echo Pressione CTRL+C para encerrar o servidor
echo ========================================
echo.

python app.py

pause
