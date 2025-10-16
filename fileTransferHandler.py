import subprocess

def getFileContents(path):

    try:
        # Invoke powershell to display file contents, permissions, length, and name
        result = subprocess.run(["powershell", "-Command", f'Get-ChildItem "{path}"'], capture_output=True, text=True)

        print(result.stdout)

    except Exception as e:
        print(f"An error occurred: {e}")

def copyFile(source, destination):

    try:
        # Copy single file from source to destination 
        result = subprocess.run(["powershell", "-Command", f'Copy-Item -Path "{source}" -Destination "{destination}"'], capture_output=True, text=True)


    except Exception as e:
        print(f"An error occurred: {e}")

def moveFile(source, destination):

    try:
        # Move single file from source to destination
        result = subprocess.run(["powershell", "-Command", f'Move-Item -Path "{source}" -Destination "{destination}"'], capture_output=True, text=True)

    except Exception as e:
        print(f"An error occurred: {e}")

def openFile(path):

    try:
        # Open file using standard set path
        result = subprocess.run(["powershell", "-Command", f'Invoke-Item -Path "{path}"'], capture_output=True, text=True)

    except Exception as e:
        print(f"An error occurred: {e}")

def deleteFile(path):

    try:
        # Delete file at specified path
        result = subprocess.run(["powershell", "-Command", f'Remove-Item -Path "{path}"'], capture_output=True, text=True)

    except Exception as e:
        print(f"An error occurred: {e}")    
