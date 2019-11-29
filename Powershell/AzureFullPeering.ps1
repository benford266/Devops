$subscriptions = Get-AzSubscription
foreach ($subscription in $subscriptions){
Select-AzSubscription -Subscription $subscription

$vnets = get-azvirtualnetwork

foreach( $vnetname in $vnets.name){
$vnet = get-azvirtualnetwork -name $vnetname
foreach ( $peer in $vnet.VirtualNetworkPeerings.Remotevirtualnetwork.id){
write-host $vnetname ',' $peer
}
}
}
