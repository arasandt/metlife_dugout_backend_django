import environ
env = environ.Env()
try:
    root = environ.Path(__file__)
    environ.Env.read_env()
except:
        environ.Env.ENVIRON = dict(
        PORT=os.environ['PORT'],
        SECRET_KEY=os.environ['SECRET_KEY'],
        DB_NAME=os.environ['DB_NAME'],
        DB_HOST=os.environ['DB_HOST'],
        DB_USER=os.environ['DB_USER'],
        DB_PASSWORD=os.environ['DB_PASSWORD'],
    )
