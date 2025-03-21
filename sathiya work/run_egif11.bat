@@echo off

set BINDIR=d:\egif\bin
set CONFIGFILE=d:\egif\bin\egif.config

set filename=%1
set filename=%filename:_result.xml=%

mkdir Autonomy_%filename%

call %BINDIR%\EGIF %1 Autonomy_%filename% GIF@bankofamerica.com terrpdb odbcconn r3gr3p0rt!ng ios.txt ALL  IOS 0 %CONFIGFILE%> list.txt 2>&1