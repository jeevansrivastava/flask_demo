# Installation 
  - Active Virtual Env `source bin/activate`
  - Install Dependency `pip install -r requirements.txt`
  - Set-up Flask App 
    - Ubuntu ~ `$ export FLASK_APP=run.py`
    - Windows ~ `C:\path\to\app>set FLASK_APP=run.py`
  - Migration 
    - Init migration `py migration db init`
    - migtate `py migration db migrate`
    
  - Run Application `flask run`
  
  
# File Structure

  ```
  C:.
│   .gitignore
│   app.db
│   app.py
│   config.py
│   migrate.py
│   requirements.txt
│   run.py
│
├───migrations
│   │   alembic.ini
│   │   env.py
│   │   README
│   │   script.py.mako
│   │
│   └───versions
│           dadfff043c5e_.py
│
├───models
│       category.py
│       comment.py
│       __init__.py
│
├───resources
│       Category.py
│       Comment.py
│       Hello.py
│
└───utility
        Response.py
  ```      

