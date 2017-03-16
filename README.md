# Quokka CMS
## The Happiest CMS in the world


> NOTE: QuokkaCMS is being rewritten from scratch to be more simpler and use a flat file DB system
> the old QuokkaCMS based in MongoDB will be still available in <1.0.0 branch but will no longer be
> maintained or updated and fixes and improvements will be only community driven.
> I recommend you to use the migration script if you are using the old QuokkaCMS.

Quokka CMS is a small and simple Content Management System based
in Python, Flask, Flask-Admin and TinyDB.

The default database system is TinyDB because it does not require a database system
and stores data in a flat JSON file.

Altough you can also use MongoDB if you need to run the CMS in a concurrent admin user
environment.

# Why use QuokkaCMS?

- You want a simple but powerful CMS for your website or blog
- You want a lightweight platform simple to deploy
- You want to be able to run without a database system
- You want the possibility to optionally use a powerful NoSQL database
- You want to have a web admin interface to manage your content and posts
- You want to optionally generate your CMS as a static HTML website to host on github.io
- You want to use the already existing and powerful Pelican Themes
- You want to install and develop plugins easily
- You like Quokkas (the animal)
- You like Python
- You like Flask

# Quick Start

## Install quokka

    $ pip install quokka

> NOTE: QuokkaCMS runs only in Python 3.6+

## Start a project

    $ quokka init mywebsite
    Generating new quokka project in ~/mywebsite

The above command will generate your project files as:

    theme\       # Pelican theme files
    uploads\     # Files uploaded by you via admin interface
    database\    # JSON database if using TinyDB (default)
    plugins\     # Plugins (some generated by default)
    build\       # Whwn static HTML is generated file output goes here
    setting.yml  # Configurations
    manage.yml   # Command line interface `quokka manage <command name>`

You can optionally pass arguments:

    $ quokka init mywebsite --theme http://github.com/user/theme

## Run your website

    $ quokka manage runserver --port 5000

## (optional) Populate with sample database

    $ quokka manage sample_database

## Access admin interface

    http://localhost:5000/admin

## Access your site

    http://localhost:5000


# Deploy

## You can deploy your Quokka Website in a WSGI server

Check the wsgi.py and refer to it when deploying in wsgi servers.

gunicorn and uwsgi examples given in examples folder.

# Publish Static HTML website

## You can generate a static HTML website to host anywhere

Once you have your website running locally you can easily generate a
static HTML website from it.

    $ quokka freeze
    Generating static HTML website on ./build folder

Once you have a ./build folder populated with static website you can deploy it
using SCP, FTP or git.

## Deploying to github pages from command line.

    $ quokka publish --static --git=rochacbruno/mysite --branch=gh_pages

The above is also available in admin under 'publish' menu.


## Deploying via SCP

    $ quokka publish --static --scp --dest='me@hostname:/var/www/mysite'
    password : ...
    # you can pass --key to use it instead of password

## Deploying yo Heroku

    $ quokka publish --static --heroku --options

## Deploying via FTP

    $ quokka publish --static --ftp --host='ftp://server.com' --dest='/var/www/mysite'

## Load database from remote deployment (only for TinyDB)

When you publish a static website along with the static files the database also
goes to the server under the databases/ folder only as a backup and snapshot.

You can load that remote database locally e.g: to add new posts and then re-publish

    $ quokka restoredb --remote --git=rochacbruno/mysite
    Creating a backup of local database...
    Downloading remote database
    Restoring database..
    Done...

Now you can run `quokka runserver` open your `localhost:5000/admin` write new content
and then `Publish` website again using command line or admin interface.

> If you want to restore a local database use --local and --path

# Using MongoDB

You can choose to use MongoDB instead of TinyDB, That is useful specially if
you deploy or local instance has more than one admin user concurrently
and also useful if you want to install plugins which support MongoDB only
(because it relies on aggregations and gridfs)

You only need a running instance
of Mongo server and change `settings.yml` on your project from:

    db_system: tinydb
    db_folder: databases

to:

    db_system: mongodb
    db_name: my_database
    db_host: 127.0.0.1
    db_port: 2600
    db_username: xxxx
    db_password: xxxx

Then when running `quokka` again it will try to connect to that Mongo Server.

With that you can deploy your site on `wsgi` server or can also generate `static` website.

> NOTE: Not all commands and plugins works with mongoDB