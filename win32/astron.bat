@echo off
title POR OTP
cd "../astron"

:main
astrond.exe --loglevel info config/cluster_yaml.yml
goto main
