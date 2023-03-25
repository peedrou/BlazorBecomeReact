from dataclasses import dataclass
from .BlazorProcesses.CheckPackageInstallation import Package
from .BlazorProcesses.CheckRegisteredComponent import Registration
from .BlazorProcesses.NonClassFunctions import WriteToProgramFile
from .BlazorProcesses.NonClassFunctions import PublishComponents
from BlazorProcesses.NonClassFunctions import CopyAndPasteFolders
from BlazorProcesses.NonClassFunctions import ChangeHTML

@dataclass
class BBR:
    ReactPublicFolder: str
    ReactHTMLDirectory: str
    BlazorRootFolder: str
    BlazorProgramFileDirectory: str

    def ConvertAllRegisteredComponents(self) -> None:
        reactPublicFolder = self.ReactPublicFolder
        blazorPublishFolder = fr"{self.BlazorRootFolder}\bin\Debug\net7.0\publish\wwwroot"
        reactHTML = self.ReactHTMLDirectory

        CopyAndPasteFolders(blazorPublishFolder, reactPublicFolder)
        ChangeHTML(reactHTML)

    def ConvertComponent(self, ComponentName: str)-> None:
        pass

    def RegisterComponentInBlazor(self, RazorWidgetName: str, NewComponentName: str) -> None:
        pathToProgram = self.BlazorProgramFileDirectory
        pathToRoot = self.BlazorRootFolder

        Package.CheckPackage()
        if Registration.CheckRegistration(NewComponentName=NewComponentName):
            print("A component already exists with that name")
            return
        WriteToProgramFile(RazorWidgetName, NewComponentName, pathToProgram)
        PublishComponents(pathToRoot)

    
