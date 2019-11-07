## Script to Create and Update UDRs from ExpressRoutes


## Import Azure Modules
import-module -name Azure*
## Gets Params from User
$New_UDR = read-host "Is this a new UDR? y or n"
$RG = read-host "Please enter RG"
$UDR = read-host "Please enter UDR Name"
## Static Params
$NGF_VM_IP = "*"
$NGF_VM_IFC_Name = "fw1-gbzs1-services-e114"
$NGF_VM_IFC_RG = "*"
$RouteAmmount = 402

## To work behind proxy
[System.Net.WebRequest]::DefaultWebProxy.Credentials = [System.Net.CredentialCache]::DefaultCredentials

## Login and select subscription
login-azurermaccount
Select-AzureRmSubscription -SubscriptionId a60e7536-49f3-4630-83d5-22defd3eb524

## Creates UDR if selected
if ($New_UDR -eq "y"){
New-AzureRmRouteTable -ResourceGroupName $RG -Location Uksouth -Name $UDR
}

## Does all the bits n bobs
$routetable = Get-azurermroutetable -ResourceGroupName $RG -Name $UDR
$count = 1
$RT1 = Get-AzureRmEffectiveRouteTable -NetworkInterfaceName $NGF_VM_IFC_Name -ResourceGroupName $NGF_VM_IFC_RG
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

