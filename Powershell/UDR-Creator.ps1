import-module -name Azure*
$RG = read-host "Resource Group Name"
$UDR = read-host "UDR Name"
$Subscriptionname = read-host "Subscription"
start-process notepad.exe "C:\Users\*\Desktop\Powershell\list.txt" -nonewwindow -wait 
$list = get-content "C:\Users\*\Desktop\Powershell\list.txt"
$NGF_VM_IP = ""
#$routename = "10.10.10.0_24"
#$subnet = "10.10.10.0/24"
[System.Net.WebRequest]::DefaultWebProxy.Credentials = [System.Net.CredentialCache]::DefaultCredentials
login-azurermaccount

$subscription = Get-AzureRmSubscription -SubscriptionName $Subscriptionname
Select-AzureRmSubscription -SubscriptionId $subscription.Id
New-AzureRmRouteTable -ResourceGroupName $RG -Location Uksouth -Name $UDR
$routetable = Get-azurermroutetable -ResourceGroupName $RG -Name $UDR
foreach ( $route in $list )
{
    $routename = $route -replace '/','_'
    Add-AzureRmRouteConfig -Name $routename -AddressPrefix $route -NextHopType VirtualAppliance -NextHopIpAddress $NGF_VM_IP -RouteTable $routetable
}
set-azurermroutetable -RouteTable $routetable