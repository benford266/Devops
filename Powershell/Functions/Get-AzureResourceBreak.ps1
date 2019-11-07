function Get-AzureResourceBreak($resource)
{
$resourcetype = $resource.split('-')[0]
$resourcelocation = $resource.split('-')[1]
$resourcesubscription = $resource.split('-')[2] + '-' + $resource.split('-')[3] + '-' + $resource.split('-')[4] + '-' + $resource.split('-')[5]
$resourcedescription = $resource.split('-')[6]
echo 'Resource Type: ' $resourcetype
echo 'Resource Location: ' $resourcelocation
echo 'Resource Subscription: ' $resourcesubscription
echo 'Resource Description: ' $resourcedescription
}

