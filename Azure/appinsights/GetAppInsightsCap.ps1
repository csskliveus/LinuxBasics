# get list of application insights
$appinsightslist=az resource list --resource-type 'Microsoft.Insights/components' | ConvertFrom-Json
#write-host $appinsightslist
$hash = @{}
$hash.Add("resourceGroup.appinsightsName","cap")
foreach ($insight in $appinsightslist)
  {
    write-host $insight.name
    $cap = az monitor app-insights component billing show -a $insight.name -g $insight.resourceGroup  --query 'dataVolumeCap.cap' -o tsv
    $var1 = $insight.resourceGroup+"."+$insight.name
    $hash.Add($var1,$cap )
   
  }

$hash.GetEnumerator() |  Export-Csv -NoTypeInformation -Path .\HashToCsv.csv