 $user_name = Read-Host "Enter the User name" 
 $password = Read-Host "Enter the password" 
 $psw = 'cloud@123'
 
  if($password -ne $psw)
  {
  
  
	Write-Error "$date Entered passwords are not same. Script is exiting" 
    break 
  
  
  }
  
  Connect-VIServer -Server 10.207.214.153 -Protocol https -User $user_name -Password $password