@@echo off

set BINDIR= C:\Users\manoj\Downloads\Training\sathiya work
set input_file = SMS-DATA.csv

set egif_log= %BINDIR%\egif_log.txt
call python %BINDIR%\test.py %BINDIR% %input_xml% >> %egif_log%