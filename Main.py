from dataclasses import dataclass
import typer

@dataclass
class BBR:
    ReactRootComponent: str
    BlazorRootComponent: str

    def ConvertAllRegisteredComponents(ReactRootComponent, BlazorRootComponent):
        pass
    
