from app import create_app, db
from flask_script import Manager, Server
from app.models import Post, User
from flask_migrate import Migrate, MigrateCommand

# creating app instance
# TODO(S) 
'''DEVELOPMENT'''
#app = create_app('development')
'''PRODUCTION'''
app = create_app('production')
'''TESTING'''
# app = create_app('test')

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    '''
    run unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Post = Post)
    # return dict(app=app, db=db, '''User=User''' )


if __name__ == '__main__':
    manager.run()
