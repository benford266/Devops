import-module -name Azure*
$RG = "*"
$UDR = "Ben-TestGateway-UDR"
$NGF_VM_IP = "*"
$NGF_VM_IFC_Name = "fw1-gbzs1-services-e114"
$NGF_VM_IFC_RG = "*"
[System.Net.WebRequest]::DefaultWebProxy.Credentials = [System.Net.CredentialCache]::DefaultCredentials

login-azurermaccount
Select-AzureRmSubscription -SubscriptionId 

$routetable = Get-azurermroutetable -ResourceGroupName $RG -Name $UDR
$count = 1
$RT1 = Get-AzureRmEffectiveRouteTable -NetworkInterfaceName $NGF_VM_IFC_Name -ResourceGroupName $NGF_VM_IFC_RG
    foreach ($element in $RT1) {
        if( ($element.NextHopType.CompareTo("VirtualNetworkGateway") -eq 0)) {
           
           $count = $count + 1

            $routename = $element.AddressPrefix.Item(0) -replace '/','_'
            if ($count -lt 402){
            Add-AzureRmRouteConfig -Name $routename -AddressPrefix $element.AddressPrefix.Item(0) -NextHopType VirtualAppliance -NextHopIpAddress $NGF_VM_IP -RouteTable $routetable
            }
        }
        }

set-azurermroutetable -RouteTable $routetable

