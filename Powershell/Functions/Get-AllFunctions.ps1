$homepath = $env:USERPROFILE + '\desktop\powershell\azure\functions'
cd $homepath

$functionfiles = ls

foreach ($function in $functionfiles){
$functionpath = "C:\Users\bf1602\desktop\powershell\azure\functions\" + $function.Name
. $functionpath
}
