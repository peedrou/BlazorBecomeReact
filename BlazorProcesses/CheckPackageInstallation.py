from dataclasses import dataclass

@dataclass
class Package:

    PackageInstalled: bool = False

    def CheckPackage(self):
        answer = input("Have you installed the package (microsoft.aspnetcore.components.customelements) in your Blazor Project? [Y/N] ")
        if answer == "Y" or "y":
            self.PackageInstalled = True
            return self.PackageInstalled
        elif answer == "N" or "n":
            print("Please install the package before continuing")
            return
        else:
            print("Invalid input, please enter Y or N.")
            return
    


