from dataclasses import dataclass
from .BlazorProcesses.CheckPackageInstallation import Package
import typer

@dataclass
class BBR:
    ReactRootComponentFolder: str
    BlazorRootComponentFolder: str
    BlazorProgramFolder: str

    def ConvertAllRegisteredComponents(ReactRootComponent, BlazorRootComponent) -> None:
        pass

    def ConvertComponent(ReactRootComponent, BlazorRootComponent, ComponentName: str)-> None:
        pass

    def CreateCustomComponent(BlazorProgramFolder, RazorWidgetName: str, NewComponentName: str) -> None:
        pass
    
