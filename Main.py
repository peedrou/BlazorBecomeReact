from dataclasses import dataclass
from .BlazorProcesses.CheckPackageInstallation import Package
from .BlazorProcesses.CheckRegisteredComponent import Registration
from .BlazorProcesses.NonClassFunctions import WriteToProgramFile
import typer

@dataclass
class BBR:
    ReactRootComponentFolder: str
    BlazorRootComponentFolder: str
    BlazorProgramFolder: str

    def ConvertAllRegisteredComponents(self) -> None:
        pass

    def ConvertComponent(self, ComponentName: str)-> None:
        pass

    def RegisterComponentInBlazor(self, RazorWidgetName: str, NewComponentName: str) -> None:
        Package.CheckPackage()
        if Registration.CheckRegistration(NewComponentName=NewComponentName):
            print("A component already exists with that name")
            return
        path = self.BlazorProgramFolder
    
