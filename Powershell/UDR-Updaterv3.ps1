## Script to Create and Update UDRs from ExpressRoutes
## Also script can update all udrs in subscription


## Import Azure Modules
import-module -name Azure*
## Gets Params from User
$New_UDR = read-host "Is this a new UDR? y or n"
$Allupdate = read-host "Would you like to update all udrs in a subscription? y or n"
$RG = read-host "Please enter RG"
echo "Please make sure there is a powered on machine in a subnet in this RG and all routing is working"

## If not all UDR it will prompt for UDR name
if ($Allupdate -eq "n" ){$UDR = read-host "Please enter UDR Name"}
$Subscriptionname = read-host "Subscription Name"

## Static Params
$NGF_VM_IP = "*"

## Use this to limit the ammount of routes added to UDR
$RouteAmmount = 402

## To work behind proxy
[System.Net.WebRequest]::DefaultWebProxy.Credentials = [System.Net.CredentialCache]::DefaultCredentials

## Login and select subscription
login-azurermaccount
## Get subscription information and set
<#$subscription = Get-AzureRmSubscription -SubscriptionName $Subscriptionname
Select-AzureRmSubscription -SubscriptionId $subscription.Id#>

## Get VM info for powered on machine in RG, This is used for automating route collection

$vms = get-azurermvm -status
foreach ($vm in $vms)
{
	if ($vm.powerstate -eq "VM running")
	{
    ## Below stores the first powered up machines details
	$vmname = $vm.name
	$vmrg = $vm.ResourceGroupName
	$vmlocal = $vm.location
	break
	}
}

$MyVM = get-azurermvm -ResourceGroupName $vmrg -name $vmname
Get-AzureRmNetworkInterface | Where { $_.Id -eq $MyVM.NetworkProfile[0]}
$NicDetails = Get-AzureRmResource -ResourceId $MyVM.NetworkProfile[0].NetworkInterfaces.id

## Gets a list of the UDRS currently in the Subscription

if ($Allupdate -eq "y"){
clear-variable -name udrs
$resources = Get-AzureRmResource
foreach ($resource in $resources)
{
	if ($resource.resourcetype -eq "Microsoft.Network/routeTables")
	{
    ## Stores list of udrs in variable
	$udrs = $udrs + "`r`n" + $resource.Name
	}
	
}
}



## Creates UDR if selected
if ($New_UDR -eq "y"){
New-AzureRmRouteTable -ResourceGroupName $RG -Location Uksouth -Name $UDR
}

## Does all the bits n bobs for single UDR
if($Allupdate -eq "n")
{
$routetable = Get-azurermroutetable -ResourceGroupName $RG -Name $UDR
$count = 1
$RT1 = Get-AzureRmEffectiveRouteTable -NetworkInterfaceName $NicDetails -ResourceGroupName $vmrg
    foreach ($element in $RT1) {
        if( ($element.NextHopType.CompareTo("VirtualNetworkGateway") -eq 0)) {
           
           $count = $count + 1

            $routename = $element.AddressPrefix.Item(0) -replace '/','_'
            if ($count -lt $RouteAmmount){
            Add-AzureRmRouteConfig -Name $routename -AddressPrefix $element.AddressPrefix.Item(0) -NextHopType VirtualAppliance -NextHopIpAddress $NGF_VM_IP -RouteTable $routetable
            }
        }
        }

## Saves routing table
set-azurermroutetable -RouteTable $routetable

}

## Does all the bits n bobs for all Routing tables in Subscription
if($Allupdate -eq "y")
{
foreach($UDR in $udrs){
$routetable = Get-azurermroutetable -ResourceGroupName $RG -Name $UDR
$count = 1
$RT1 = Get-AzureRmEffectiveRouteTable -NetworkInterfaceName $NicDetails -ResourceGroupName $vmrg
    foreach ($element in $RT1) {
        if( ($element.NextHopType.CompareTo("VirtualNetworkGateway") -eq 0)) {
           
           $count = $count + 1

            $routename = $element.AddressPrefix.Item(0) -replace '/','_'
            if ($count -lt $RouteAmmount){
            Add-AzureRmRouteConfig -Name $routename -AddressPrefix $element.AddressPrefix.Item(0) -NextHopType VirtualAppliance -NextHopIpAddress $NGF_VM_IP -RouteTable $routetable
            }
        }
        }

## Saves routing table
set-azurermroutetable -RouteTable $routetable
}

}

