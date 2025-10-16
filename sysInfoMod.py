import subprocess

def getSystemInfo():

    try:
        # Run the command using subprocess and strip the output to remove extra whitespace/newlines
        systemName = subprocess.run(["powershell", "-Command", '$(Get-ComputerInfo).CsName'], capture_output=True, text=True)
        systemDate = subprocess.run(["powershell", "-Command", 'Get-Date -Format "ddMMyyyy"'], capture_output=True, text=True)
        CName = subprocess.run(["powershell", "-Command", '(Get-CimInstance -ClassName Win32_Processor).Name'], capture_output=True, text=True)
        CNumCores = subprocess.run(["powershell", "-Command", '(Get-CimInstance -ClassName Win32_Processor).NumberOfCores'], capture_output=True, text=True)
        CNumProcessors = subprocess.run(["powershell", "-Command", '(Get-CimInstance -ClassName Win32_Processor).NumberOfLogicalProcessors'], capture_output=True, text=True)

        # Store only cleaned output values in dictionary
        sysInfoDict = dict(
            sysName = systemName.stdout.strip(),
            sysDate = systemDate.stdout.strip(),
            cpuName = CName.stdout.strip(),
            cpuCores = CNumCores.stdout.strip(),
            cpuProcessors = CNumProcessors.stdout.strip()
        )

    except Exception as e:
        print(f"An error occurred: {e}")
        sysInfoDict = {}  # Return empty dictionary on error

    return sysInfoDict

def getDiskInfo():
    
    try:
        # Run the command using subprocess and strip the output to remove extra whitespace/newlines
        diskModel = subprocess.run(["powershell", "-Command", '(Get-PhysicalDisk).FriendlyName'], capture_output=True, text=True)
        diskSpec = subprocess.run(["powershell", "-Command", '(Get-PhysicalDisk).MediaType'], capture_output=True, text=True)
        bitsDiskSize = subprocess.run(["powershell", "-Command", '(Get-PhysicalDisk).Size'], capture_output=True, text=True)

        gbDiskSize = round((int(bitsDiskSize.stdout.strip(),) / (1024 ** 3)), 2)

        # Store only cleaned output values in dictionary
        diskInfoDict = dict(
            diskName = diskModel.stdout.strip(),
            diskType = diskSpec.stdout.strip(),
            diskSize = str(gbDiskSize)
        )

    except Exception as e:
        print(f"An error occurred: {e}")
        diskInfoDict = {}  # Return empty dictionary on error

    return diskInfoDict
