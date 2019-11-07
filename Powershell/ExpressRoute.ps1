##Script to get Azure Express Route information

$ResourceGroup = ""
$ERCN = ""

$ERCI = Get-AzureRmExpressRouteCircuit -ResourceGroupName $ResourceGroup -Name $ERCN
$ERCR = Get-AzureRmExpressRouteCircuitRouteTable -ResourceGroupName $ERCI.ResourceGroupName -ExpressRouteCircuitName $ERCI.Name -PeeringType AzurePrivatePeering -DevicePath Primary

