'''
This is the main entry point of the application. It initializes the GUI and sets up the main loop.
'''
import gui
def main():
    app = gui.ArticleApp()
    app.run()
if __name__ == "__main__":
    main()