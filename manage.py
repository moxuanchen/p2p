# -*- coding: utf-8 -*-


from flask_script import Manager
from flask_script import Shell
from flask_script import Server
from p2p.app import create_app

app = create_app()
manager = Manager(app)

if __name__ == "__main__":
    manager.add_command("server", Server)
    manager.add_command("shell", Shell)
    manager.run()
