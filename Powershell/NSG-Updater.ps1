## Script to update NSG's

## Import Azure Modules
#import-module -name Azure*

## To work behind proxy
[System.Net.WebRequest]::DefaultWebProxy.Credentials = [System.Net.CredentialCache]::DefaultCredentials

## Login and select subscription
login-azurermaccount
## Get subscription information and set
#$subscriptionname = read-host "Please enter subscription name?"
#$subscription = Get-AzureRmSubscription -SubscriptionName $Subscriptionname
#Select-AzureRmSubscription -SubscriptionId $subscription.Id

$MasterRuleSet = import-csv ""

foreach($rule in $MasterRuleSet)
{
$nsg = Get-AzureRmNetworkSecurityGroup -ResourceGroupName Back -name BenBackTest-New
Add-AzureRmNetworkSecurityRuleConfig -NetworkSecurityGroup $nsg -Name $rule.name -access $rule.Action -Direction $rule.Direction -Priority $rule.Priority -Protocol $rule.Protocol -Description $rule.Description -SourceAddressPrefix $rule.Source -DestinationAddressPrefix $rule.Destination -DestinationPortRange $rule.'Destination Port Ranges' -SourcePortRange $rule.'Source Port Ranges'
}

## Command to create new NSG
#New-AzureRmNetworkSecurityGroup -Name NSG-Back-Test -ResourceGroupName Back -location uksouth

## Command to update NSG
#New-AzureRmNetworkSecurityGroup -ResourceGroupName Back -location uksouth -Name BenBackTest-New -SecurityRules $rule1
DCC