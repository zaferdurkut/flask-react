from flask_script import Manager,Server
from flask_migrate import MigrateCommand, Migrate
from flask_sqlalchemy import SQLAlchemy

from config.config import Config
from run import app

db = SQLAlchemy(app)

server = Server(host=Config.HOST, port=Config.PORT)


manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", server)

if __name__ == '__main__':
    manager.run()
