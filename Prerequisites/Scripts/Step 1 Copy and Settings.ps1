#Powershell prompt 
#enable running of unsigned local scripts 
Set-Executionpolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

mkdir C:\Prerequisites -ErrorAction SilentlyContinue
# Copy

CD C:\Prerequisites
