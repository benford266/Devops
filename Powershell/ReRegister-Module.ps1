## Script to Reregister Service providers in all subscriptions, This is needed when a new feature comes out.



## All CCM Subsccriptions need to be in the list.
$SUBSCRIPTIONS = ""

$Serviceproviders = "Microsoft.Insights","Microsoft.Network"


## Azure Login requirements
[System.Net.WebRequest]::DefaultWebProxy.Credentials = [System.Net.CredentialCache]::DefaultCredentials
login-azurermaccount

## Re-Register Module

write-host "Re-Registering All Service Providers"

foreach($Subscriptionname in $SUBSCRIPTIONS)
{
$subscription = Get-AzureRmSubscription -SubscriptionName $Subscriptionname
Select-AzureRmSubscription -SubscriptionId $subscription.Id

## Change below command to correct module
foreach($sp in $Serviceproviders)
{
Write-host "Re-Registering $sp in $Subscriptionname"
Register-AzureRmResourceProvider -ProviderNamespace $sp
}



}

Write-host "*** *** Re-Register Complete *** ***"