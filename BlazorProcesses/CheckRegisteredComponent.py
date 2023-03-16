from dataclasses import dataclass

@dataclass
class Registration:

    Registered: bool = False

    def CheckRegistration(self, NewComponentName) -> bool:
        pass