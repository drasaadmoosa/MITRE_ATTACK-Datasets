# Windows

## ATT&CK Navigator View

<iframe src="https://mitre-attack.github.io/attack-navigator/enterprise/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fhunters-forge%2Fmordor%2Fmaster%2Fdocs%2Fnotebooks%2Fsmall%2Fwindows%2Fwindows.json&tabs=false&selecting_techniques=false" width="950" height="450"></iframe>

## Table View

|Created|Dataset|Description|Simulator|Author|
| :---| :---| :---| :---| :---|
|2019/10/27 |[Covenant DCSync All](https://mordordatasets.com/notebooks/small/windows/06_credential_access/SD-191027064128.html) |This dataset represents adversaries abusing Active Directory Replication services to retrieve NTLM hashes from all domain accounts |Covenant|Roberto Rodriguez @Cyb3rWard0g |
|2019/10/27 |[Covenant Grunt Msbuild](https://mordordatasets.com/notebooks/small/windows/05_defense_evasion/SD-191027042312.html) |This dataset represents adversaries using trusted windows utilities such as msbuild to proxy execution of malicious code. |Remote Desktop Protocol|Roberto Rodriguez @Cyb3rWard0g |
|2019/10/27 |[Covenant InstallUtil](https://mordordatasets.com/notebooks/small/windows/02_execution/SD-191027223020.html) |This dataset represents adversaries proxying execution of code through InstallUtil, a trusted Windows utility. |Remote Desktop Protocol|Roberto Rodriguez @Cyb3rWard0g |
|2019/12/05 |[Covenant Mimikatz Logonpasswords](https://mordordatasets.com/notebooks/small/windows/06_credential_access/SD-191205033226.html) |This dataset represents adversaries using mimikatz and module `logonpasswords` to dump credentials from the memory contents of lsass.exe |Covenant|Roberto Rodriguez @Cyb3rWard0g |
|2019/12/05 |[Covenant Mimikatz LSA Cache](https://mordordatasets.com/notebooks/small/windows/06_credential_access/SD-191205043030.html) |This dataset represents adversaries using Mimikatz to exract cached password hashes from HKEY_LOCAL_MACHINE\SECURITY\Cache |Covenant|Roberto Rodriguez @Cyb3rWard0g |
|2019/12/05 |[Covenant Mimikatz LSA Secrets](https://mordordatasets.com/notebooks/small/windows/06_credential_access/SD-191205043410.html) |This dataset represents adversaries using Mimikatz to get the SysKey to decrypt SECRETS entries (from registry or hives). |Covenant|Roberto Rodriguez @Cyb3rWard0g |
|2019/03/01 |[Empire DCSync](https://mordordatasets.com/notebooks/small/windows/06_credential_access/SD-190301174830.html) |This dataset represents adversaries abusing Active Directory Replication services to retrieve NTLM hashes from domain accounts |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/03/01 |[Empire DCSync ACL](https://mordordatasets.com/notebooks/small/windows/05_defense_evasion/SD-190301125905.html) |This dataset represents adversaries with enough permissions (domain admin) adding an ACL to the Root Domain for any user, despite being in no privileged groups, having no malicious sidHistory, and not having local admin rights on the domain controller itself. |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/05/18 |[Empire DLL Injection](https://mordordatasets.com/notebooks/small/windows/05_defense_evasion/SD-190518221344.html) |This dataset represents adversaries injects a Dll into an arbitrary process |Empire|Roberto Rodriguez @Cyb3rWard0g |
|19/05/18 |[Empire Elevated Registry](https://mordordatasets.com/notebooks/small/windows/03_persistence/SD-190518183936.html) |This dataset represents adversaries modifying HKLM:SOFTWARE\Microsoft\Windows\CurrentVersion\Run registry keys for persistence. |Empire|Roberto Rodriguez @Cyb3rWard0g |
|19/05/18 |[Empire Elevated Scheduled Tasks](https://mordordatasets.com/notebooks/small/windows/03_persistence/SD-190518184109.html) |This dataset represents adversaries creating scheduled tasks to maintain persistence in the environment |Empire|Roberto Rodriguez @Cyb3rWard0g |
|19/05/18 |[Empire Elevated WMI Subscription](https://mordordatasets.com/notebooks/small/windows/03_persistence/SD-190518184306.html) |This dataset represents adversaries leveraging WMI subscriptions for persistence. |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/05/18 |[Empire Enabling RDP](https://mordordatasets.com/notebooks/small/windows/05_defense_evasion/SD-190518203650.html) |This dataset represents adversaries enabling RDP and adding a firewall exception to a compromised system |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/05/18 |[Empire Find Local Admin Access](https://mordordatasets.com/notebooks/small/windows/07_discovery/SD-190518224039.html) |This dataset represents adversaries using the OpenSCManagerW Win32API call to establish a handle to the remote host and verify if the current user context has local administrator acess to the target. |Empire|Roberto Rodriguez @Cyb3rWard0g |
|19/05/19 |[Empire Get Local Sessions](https://mordordatasets.com/notebooks/small/windows/07_discovery/SD-190519005224.html) |This dataset represents adversaries executing the NetSessionEnum Win32API call to query the local host for active sessions |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/05/18 |[Empire Invoke DCOM](https://mordordatasets.com/notebooks/small/windows/08_lateral_movement/SD-190518211052.html) |This dataset represents adversaries executing commands on remote hosts via MMC20.Application COM object over DCOM. |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/05/18 |[Empire Invoke Msbuild](https://mordordatasets.com/notebooks/small/windows/05_defense_evasion/SD-190518213907.html) |This dataset represents adversaries using trusted windows utilities such as msbuild to proxy execution of malicious code. |Empire|Roberto Rodriguez @Cyb3rWard0g |
|19/05/18 |[Empire Invoke PsExec](https://mordordatasets.com/notebooks/small/windows/08_lateral_movement/SD-190518210652.html) |This dataset represents adversaries executing malicious code remotely psexec style |Empire|Roberto Rodriguez @Cyb3rWard0g |
|19/05/18 |[Empire Invoke PSRemoting](https://mordordatasets.com/notebooks/small/windows/08_lateral_movement/SD-190518211456.html) |This dataset represents adversaries executing malicious code on remote hosts using PowerShell Remotely. |Empire|Roberto Rodriguez @Cyb3rWard0g |
|19/05/18 |[Empire Invoke Runas](https://mordordatasets.com/notebooks/small/windows/05_defense_evasion/SD-190518204300.html) |This dataset represents adversaries creating processes with explicit credentials (runas style). |Empire|Roberto Rodriguez @Cyb3rWard0g |
|19/05/18 |[Empire Invoke Smbexec](https://mordordatasets.com/notebooks/small/windows/08_lateral_movement/SD-190518210125.html) |This dataset represents adversaries performing SMBExec style command execution with NTLMv2 pass the hash authentication. |Empire|Roberto Rodriguez @Cyb3rWard0g |
|19/05/18 |[Empire Invoke WMI](https://mordordatasets.com/notebooks/small/windows/08_lateral_movement/SD-190518214442.html) |This dataset represents adversaries using WMI to execute malicious code on endpoints remotely |Empire|Roberto Rodriguez @Cyb3rWard0g |
|19/05/18 |[Empire Invoke WMI Debugger](https://mordordatasets.com/notebooks/small/windows/08_lateral_movement/SD-190518215622.html) |This dataset represents adversaries using WMI to set the debugger for a target binary on a remote machine. Setting sethc.exe to be C:\Windows\System32\cmd.exe |Empire|Roberto Rodriguez @Cyb3rWard0g |
|19/05/18 |[Empire Launcher VBS](https://mordordatasets.com/notebooks/small/windows/05_defense_evasion/SD-190518182022.html) |This dataset represents adversaries executing a VBS script as a launcher for initial access |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/05/18 |[Empire Mimikatz Export Master Key](https://mordordatasets.com/notebooks/small/windows/06_credential_access/SD-190518235535.html) |This dataset represents adversaries using tools like Mimikatz to export the master key from the domain controller remotely. |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/05/18 |[Empire Mimikatz Extract Tickets](https://mordordatasets.com/notebooks/small/windows/06_credential_access/SD-190518230752.html) |This dataset represents adversaries using PowerSploit's Invoke-Mimikatz function to extract kerberos tickets from memory in base64-encoded form. |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/05/18 |[Empire Mimikatz Logonpasswords](https://mordordatasets.com/notebooks/small/windows/06_credential_access/SD-190518202151.html) |This dataset represents adversaries using mimikatz and module `logonpasswords` to dump credentials from the memory contents of lsass.exe |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/06/25 |[Empire Mimikatz Lsadump SAM](https://mordordatasets.com/notebooks/small/windows/06_credential_access/SD-190625103712.html) |This dataset represents adversaries using PowerSploit's Invoke-Mimikatz function to extract hashes from the Security Account Managers (SAM) database |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/03/19 |[Empire Mimikatz OPTH](https://mordordatasets.com/notebooks/small/windows/06_credential_access/SD-190319131123.html) |This dataset represents adversaries taking a hash into a fully-fledged Kerberos TGT |Empire|Roberto Rodriguez @Cyb3rWard0g |
|19/03/19 |[Empire Net All Local Users](https://mordordatasets.com/notebooks/small/windows/07_discovery/SD-190319020729.html) |This dataset represents adversaries enumerating all local users via the net.exe utility |Empire|Roberto Rodriguez @Cyb3rWard0g |
|19/03/19 |[Empire Net All User Domain](https://mordordatasets.com/notebooks/small/windows/07_discovery/SD-190319021158.html) |This dataset represents adversaries enumerating all users that belong to a domain via the net.exe utility |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/05/18 |[Empire Net Domain Admins Group](https://mordordatasets.com/notebooks/small/windows/07_discovery/SD-190518201207.html) |This dataset represents adversaries enumerating members of the "Domain Admins" active directory group via net.exe. |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/03/19 |[Empire Net Local Administrators Group](https://mordordatasets.com/notebooks/small/windows/07_discovery/SD-190319020147.html) |This dataset represents adversaries enumerating members of the local Administratrors group via the net.exe utility |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/05/18 |[Empire Net User Domain Specific](https://mordordatasets.com/notebooks/small/windows/07_discovery/SD-190518230446.html) |This dataset represents adversaries enumerating a specific domain user via the net.exe utility |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/06/25 |[Empire Powerdump](https://mordordatasets.com/notebooks/small/windows/06_credential_access/SD-190625132210.html) |This dataset represents adversaries dumping hashes from HKLM:\SAM\SAM\Domains\ registry keys. |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/05/18 |[Empire PSInject](https://mordordatasets.com/notebooks/small/windows/05_defense_evasion/SD-190518200432.html) |This dataset represents adversaries using Empire psinject script to inject Unmanaged PowerShell into any process. |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/06/25 |[Empire Reg Dump SAM](https://mordordatasets.com/notebooks/small/windows/06_credential_access/SD-190625133822.html) |This dataset represents adversaries with administrator privileges using the windows reg utility to dump the SAM registry hive. |Remote Desktop Protocol|Roberto Rodriguez @Cyb3rWard0g |
|2019/03/19 |[Empire Rubeus ASKTGT](https://mordordatasets.com/notebooks/small/windows/06_credential_access/SD-190319145126.html) |This dataset represents adversaries crafting raw AS-REQ (TGT request) traffic for a specific user and encryption key (/rc4, /aes128, /aes256, or /des) to request TGTs |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/03/19 |[Empire Rubeus ASKTGT CreateNetOnly](https://mordordatasets.com/notebooks/small/windows/06_credential_access/SD-190319151006.html) |This dataset represents adversaries crafting raw AS-REQ (TGT request) traffic for a specific user and encryption key (/rc4, /aes128, /aes256, or /des) to request TGTs |Empire|Roberto Rodriguez @Cyb3rWard0g |
|19/03/19 |[Empire Userland Registry](https://mordordatasets.com/notebooks/small/windows/03_persistence/SD-190319023812.html) |This dataset represents adversaries modifying HKLM:SOFTWARE\Microsoft\Windows\CurrentVersion\Run registry keys for persistence. |Empire|Roberto Rodriguez @Cyb3rWard0g |
|19/03/19 |[Empire Userland Scheduled Tasks](https://mordordatasets.com/notebooks/small/windows/03_persistence/SD-190319024742.html) |This dataset represents adversaries creating scheduled tasks to maintain persistence in the environment |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/05/18 |[Empire Wdigest Downgrade](https://mordordatasets.com/notebooks/small/windows/05_defense_evasion/SD-190518201922.html) |This dataset represents adversaries setting the UseLogonCredential property value from HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest key to 1 to enable plain text passwords. |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/12/25 |[Extended NetNTLM Downgrade](https://mordordatasets.com/notebooks/small/windows/06_credential_access/SD-191225045202.html) |This dataset represents adversaries downgrading the challenge/response authentication protocol used for network logons, the minimum security negotiated for applications using NTLMSSP, and security settings that restrict outgoing NTLM traffic to remote servers in an environment |Empire|Roberto Rodriguez @Cyb3rWard0g |
|2019/10/27 |[Interactive Task Manager Lsass dump](https://mordordatasets.com/notebooks/small/windows/06_credential_access/SD-191027054517.html) |This dataset represents adversaries using task manager interactively and dump the memory space of lsass. |Remote Desktop Protocol|Roberto Rodriguez @Cyb3rWard0g |
|2020/06/09 |[MSF Record Microphone](https://mordordatasets.com/notebooks/small/windows/09_collection/SD-200609225055.html) |This dataset represents adversaries accessing the microphone of an endpoint. |Metasploit|Roberto Rodriguez @Cyb3rWard0g |
|2019/10/27 |[Remote Interactive Task Manager Lsass dump](https://mordordatasets.com/notebooks/small/windows/06_credential_access/SD-191027055035.html) |This dataset represents adversaries using RDP and task manager interactively and dump the memory space of lsass. |Remote Desktop Protocol|Roberto Rodriguez @Cyb3rWard0g |
|19/04/03 |[SCM and Dll Hijacking IKEEXT](https://mordordatasets.com/notebooks/small/windows/08_lateral_movement/SD-190403133337.html) |This dataset represents adversaries copying a file remotely to replace the wlbsctrl.dll file which is executed by the IKEEXT (vulnerable to DLL hijack). |Empire|Roberto Rodriguez @Cyb3rWard0g |
|19/05/18 |[WMIC Add User Backdoor](https://mordordatasets.com/notebooks/small/windows/08_lateral_movement/SD-190518231333.html) |This dataset represents adversaries using WMI to add a backdoor user on endpoints remotely |Empire|Roberto Rodriguez @Cyb3rWard0g |