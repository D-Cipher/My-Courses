$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
Write-host "My directory is $dir"

Get-ChildItem $dir *.md  |
    Foreach-Object {
        $c = ($_ | Get-Content) 
        $c = $c -replace '<code>','`'
        $c = $c -replace '</code>','`'
		$c = $c -replace '````','```'
		$c = $c -replace '```python','
		~~~~~~~~'
		$c = $c -replace '```','~~~~~~~~'
        [IO.File]::WriteAllText($_.FullName, ($c -join "`r`n"))
    }