[CmdletBinding()]
param(
    [switch]$Force
)

$variableName = "OPENALEX_API_KEY"
$currentValue = [Environment]::GetEnvironmentVariable($variableName, "User")

if ($currentValue -and -not $Force) {
    Write-Host "$variableName is already configured for this Windows user."
    Write-Host "Use -Force to replace it. Restart Codex after changing it."
    exit 0
}

$secureKey = Read-Host "Paste your OpenAlex API key (input is hidden)" -AsSecureString
$keyPointer = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureKey)

try {
    $plainKey = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($keyPointer)
    if ([string]::IsNullOrWhiteSpace($plainKey)) {
        throw "empty_key"
    }

    $encodedKey = [Uri]::EscapeDataString($plainKey.Trim())
    $validationUrl = "https://api.openalex.org/rate-limit?api_key=$encodedKey"

    try {
        $null = Invoke-RestMethod -Uri $validationUrl -Method Get -TimeoutSec 30 -ErrorAction Stop
    }
    catch {
        Write-Error "OpenAlex did not accept the key, or the validation request could not reach the API. Nothing was saved."
        exit 1
    }

    [Environment]::SetEnvironmentVariable($variableName, $plainKey.Trim(), "User")
    Write-Host "$variableName was validated and saved for this Windows user."
    Write-Host "Restart Codex before running OpenAlex discovery."
}
finally {
    if ($keyPointer -ne [IntPtr]::Zero) {
        [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($keyPointer)
    }
    $plainKey = $null
    $secureKey = $null
}
