from dataclasses import dataclass
from .BlazorProcesses.CheckPackageInstallation import Package
from .BlazorProcesses.CheckRegisteredComponent import Registration
from .BlazorProcesses.NonClassFunctions import WriteToProgramFile
from .BlazorProcesses.NonClassFunctions import PublishComponents
import typer

@dataclass
class BBR:
    ReactPublicFolder: str
    BlazorRootFolder: str
    BlazorProgramFolder: str

    def ConvertAllRegisteredComponents(self) -> None:
        pass

    def ConvertComponent(self, ComponentName: str)-> None:
        pass

    def RegisterComponentInBlazor(self, RazorWidgetName: str, NewComponentName: str) -> None:
        pathToProgram = self.BlazorProgramFolder
        pathToRoot = self.BlazorRootFolder
        Package.CheckPackage()
        if Registration.CheckRegistration(NewComponentName=NewComponentName):
            print("A component already exists with that name")
            return
        WriteToProgramFile(RazorWidgetName, NewComponentName, pathToProgram)
        PublishComponents(pathToRoot)

    
