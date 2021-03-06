Building the Windows MSI
========================

This document provides instructions on creating the MSI.

Prerequisites
-------------

1. Turn on the '.NET Framework 3.5' Windows Feature (required for WIX Toolset).

2. Install 'WIX Toolset build tools' if not already installed. (e.g. WiX v3.10.3)
    http://wixtoolset.org/releases/

3. Get Git for Windows (it has several tools used for the build).
    - https://github.com/git-for-windows/git/releases/download/v2.12.2.windows.1/Git-2.12.2-32-bit.exe
    - Choose the 'Use Git and optional Unix tools from the Windows Command Prompt' option.

4. Install 'Microsoft Build Tools 2015'.
    https://www.microsoft.com/en-us/download/details.aspx?id=48159

5. Install Python 3.6
    - https://www.python.org/ftp/python/3.6.1/python-3.6.1.exe
    - python-installer.exe /quiet InstallAllUsers=0 TargetDir=%PYTHON_DIR% PrependPath=0 AssociateFiles=0 CompileAll=1 Shortcuts=0 Include_test=0 Include_doc=0 Include_dev=0 Include_launcher=0 Include_tcltk=0 Include_tools=0
    - %PYTHON_DIR% should be on PATH.

5. Clone the repository.
    - git clone https://github.com/azure/azure-cli

Note: The above can be done on a Windows 10 VM.

Building
--------

1. Set the `CLI_VERSION` environment variable.

2. Run `build_scripts\windows\scripts\build.cmd`.

3. The unsigned MSI will be in the `.\out` folder.
