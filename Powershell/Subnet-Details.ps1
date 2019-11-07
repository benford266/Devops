## Script to output all Subnets with applied NSG's and RTABS

import-module -name Azure*

[System.Net.WebRequest]::DefaultWebProxy.Credentials = [System.Net.CredentialCache]::DefaultCredentials

$login = read-host "Do you need to log into Azure y/n? "
if ($login -eq "y")
{
login-azurermaccount
}

<#
$outputtofile = read-host "Would you like to output to File y/n? "
if ($outputtofile -eq "y"){
$filepath = read-host "Please Enter File Path: "
}
#>

$SUBSCRIPTIONS = ""


foreach ($Subscriptionname in $SUBSCRIPTIONS){

$subscription = Get-AzureRmSubscription -SubscriptionName $Subscriptionname
Select-AzureRmSubscription -SubscriptionId $subscription.Id | out-null

$VirtualNetworks = Get-azurermvirtualnetwork
Write-host " "
Write-host " "
write-host "Subscription: "$Subscriptionname
Write-host " "

foreach ($Network in $VirtualNetworks){
write-host "   Virtual Network: "$Network.name
write-host " "
foreach ($subnet in $network.Subnets){

write-host "       Subnet: "$subnet.name
write-host "       NSG Applied: "$subnet.NetworkSecurityGroup.Id
write-host "       Route Table: "$subnet.RouteTable.Id
write-host " "
}
}
}

<#
if($outputtofile -eq "y"){
$results | out-file $filepath -Append
}
else{
$results
}
#>


