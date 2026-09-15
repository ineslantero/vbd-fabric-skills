$ErrorActionPreference = "Stop"
$url = "https://assetsprod.microsoft.com/en-us/wwi-sample-dataset.zip"
$out = Join-Path $PSScriptRoot "wwi-sample-dataset.zip"
if (Test-Path $out) { Write-Host "Already downloaded: $out"; exit 0 }
Write-Host "Downloading WWI sample dataset (~1.9 GB)..."
Invoke-WebRequest -Uri $url -OutFile $out -UseBasicParsing
Write-Host "Done: $out"
