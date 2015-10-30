from fabric.api import *
from fabric.colors import green, red
import datetime

SERVER_20 = '23.21.163.107'
env.hosts = [ SERVER_20 ]
env.warn_only = True

path = "/var/www/ddjj_admin"


def dump_db():
    with cd("%s/admin_ddjj" % path) :
        print(green("dumping data"))
        file_name_dump = "dump_data/dump_{0}.json".format(datetime.datetime.now().strftime('%d%m%y_%H%M'))
        run("source %s/venv_ddjj_admin/bin/activate && python manage.py dumpdata > %s" % (path, file_name_dump))


def deploy():

    print(red("Beginning Deploy:"))

    with cd("%s/admin_ddjj" % path) :
        print(run("pwd"))

        print(green("Pulling master from GitHub..."))
        run("git pull origin master")

        print(green("Installing requirements..."))
        try:
            run("source %s/venv_ddjj_admin/bin/activate && pip install -r requirements.txt" % path)
        except ValueError:
            print(green(ValueError))

        print(green("Collecting static files..."))
        run("source %s/venv_ddjj_admin/bin/activate && python manage.py collectstatic --noinput" % path)

        # print(green("Compress static files..."))
    #     run("source %s/votacionesenv/bin/activate && python manage.py compress" % path)

        # dump_db()
        
        print(green("Migrating the database..."))
        run("source %s/venv_ddjj_admin/bin/activate && python manage.py migrate" % path)

        print(green("Restart the uwsgi process"))
        run("touch admin_ddjj/wsgi.py")

    print(red("DONE!"))

