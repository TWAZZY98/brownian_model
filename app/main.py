import gui

VERSION:str = "Alpha"

def main():
    ginterface = gui.GUI(VERSION)
    ginterface.main_menu()


if __name__ == "__main__": 
    print(f"{__name__} is being run directly")
else: 
    print(f"{__name__} is being imported")
    
main()



