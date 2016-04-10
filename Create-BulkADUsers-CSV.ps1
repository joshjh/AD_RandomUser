Import-Module ActiveDirectory
Import-Csv "names.csv" | ForEach-Object {
 $userPrincinpal = $_."samAccountName" + "@BOSHED"
New-ADUser -Name $_."Name" -Path $_."ParentOU"  -SamAccountName  $_."samAccountName"  -UserPrincipalName  $userPrincinpal -Streetaddress $_."Address" -AccountPassword (ConvertTo-SecureString "MyPassword123" -AsPlainText -Force) -ChangePasswordAtLogon $true -Enabled $true 
 Add-ADGroupMember "Script-Generated-Users" -Members $_."samAccountName";
}