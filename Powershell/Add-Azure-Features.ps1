## Script to install new features into all subscriptions.



## All CCM Subsccriptions need to be in the list.
$SUBSCRIPTIONS = ''''


## Azure Login requirements
[System.Net.WebRequest]::DefaultWebProxy.Credentials = [System.Net.CredentialCache]::DefaultCredentials
login-azurermaccount

## Add Features

foreach($Subscriptionname in $SUBSCRIPTIONS)
{
$subscription = Get-AzureRmSubscription -SubscriptionName $Subscriptionname
Select-AzureRmSubscription -SubscriptionId $subscription.Id

write-host "Adding Features to $Subscriptionname"

## Change below with correct regiester commands for feature
Register-AzureRmProviderFeature -FeatureName AllowLBPreview -ProviderNamespace Microsoft.Network
Register-AzureRmProviderFeature -FeatureName AllowLBPreviewWave2 -ProviderNamespace Microsoft.Network
Register-AzureRmProviderFeature -FeatureName AllowLBPreviewWave3 -ProviderNamespace Microsoft.Network


}


## Wait for Features to complete registering, 10 minutes as specified my MS isnt enough 
Write-host "Waiting 20 Minutes for registering to complete"
Start-Sleep -s 1200


## Check Features are registered

foreach($Subscriptionname in $SUBSCRIPTIONS)
{
$subscription = Get-AzureRmSubscription -SubscriptionName $Subscriptionname
Select-AzureRmSubscription -SubscriptionId $subscription.Id
write-host "Checking Registration for $Subscriptionname"

## Change below to correct command to check features
Get-AzureRmProviderFeature -FeatureName AllowLBPreview -ProviderNamespace Microsoft.Network
Get-AzureRmProviderFeature -FeatureName AllowLBPreviewWave2 -ProviderNamespace Microsoft.Network
Get-AzureRmProviderFeature -FeatureName AllowLBPreviewWave3 -ProviderNamespace Microsoft.Network


}

## Re-Register Module

write-host "Re-Registering All module"

foreach($Subscriptionname in $SUBSCRIPTIONS)
{
$subscription = Get-AzureRmSubscription -SubscriptionName $Subscriptionname
Select-AzureRmSubscription -SubscriptionId $subscription.Id
Write-host "Re-Registering Module in $Subscriptionname"
## Change below command to correct module
Register-AzureRmResourceProvider -ProviderNamespace Microsoft.Network


}

Write-host "*** *** Feature Add Complete *** ***"