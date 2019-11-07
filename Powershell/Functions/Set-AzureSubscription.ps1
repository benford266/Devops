## Function to set azure Subscription
function Set-AzureSubscription($subscriptionname)
{
$subscription = Get-AzureRmSubscription -SubscriptionName $Subscriptionname
Select-AzureRmSubscription -SubscriptionId $subscription.Id
}