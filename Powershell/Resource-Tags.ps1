## Get Current & Add Tags 

## Params
$subscriptionname = ''
$resourcename = ''
$resourcegroup = ''
$tag = 'VirtualNetwork'
$set = 'no'


## Import Functions

. ""

## Set Subscription and Login to Azure 
[System.Net.WebRequest]::DefaultWebProxy.Credentials = [System.Net.CredentialCache]::DefaultCredentials
login-azurermaccount
Set-AzureSubscription $subscriptionname

## Gets the current resource info
$vnet = Get-AzureRmResource -ResourceName $resourcename -ResourceType 'Microsoft.Network/virtualNetworks' -resourcegroupname $resourcegroup

## Sets Tags if needed
if($set -eq "yes")
{
Set-AzureRmResource -Tag @{ $tag="1"} -ResourceName $resourcename -ResourceType 'Microsoft.Network/virtualNetworks' -resourcegroupname $resourcegroup
}

## Returns Tag info

echo $vnet.Name
echo $vnet.Tags
