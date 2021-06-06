@Echo off
chcp 65001
cls
color 5
title Reapz Pinger(Made By Luxar#6810.)

echo.
echo    888888ba                                       
echo  88    `8b 
   
        
echo a88aaaa8P' .d8888b. .d8888b.  88d888b. d888888b 
echo  88   `8b. 88ooood8 88'  `88  88'  `88    .d8P' 
echo  88     88 88.  ... 88.  .88  88.  .88  .Y8P    
echo  dP     dP `88888P' `88888P8  88Y888P' d888888P 
echo ooooooooooooooooooooooooooooo~88~ooooooooooooooo                              dP                                                                                     
echo.  -----------------------------
echo     
echo.
       
     
set /p IP=Enter IP=
color 5
:top
PING -n 1 %IP% | FIND "TTL="
title ::Luxar Is Pinging %IP%
IF ERRORLEVEL 1 (echo [Booted] %IP% [Ip])
set /a num= (%Random%%%9)+1
color %num%
ping -t 2 0 10 127.0.0.1 >nul
GoTo top   
@Copyright ( Luxar)                                                         