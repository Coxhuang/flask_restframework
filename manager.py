from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand
from flask_restframework import create_app
# from flask_app.models.db import db
# from flask_app.models import vehicle_info, task_info, sensors_info

app = create_app()
manager = Manager(app)
# migrate = Migrate(app, db)

# manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()