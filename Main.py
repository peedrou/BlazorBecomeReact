from dataclasses import dataclass
from .BlazorProcesses.CheckPackageInstallation import Package
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

    def CreateCustomComponent(self, RazorWidgetName: str, NewComponentName: str) -> None:
        pass
    
