import sys
sys.dont_write_bytecode = True

from modules.startup import startup_banner, create_app
startup_banner()
app = create_app()

if __name__ == '__main__':
    app.run()


