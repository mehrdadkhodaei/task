
#### Steps
[Optional] [Set up a virtualenv and activate] (https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)

##### Get the code
    git clone https://github.com/mehrdadkhodaei/task.git
    cd django-gentelella

##### Install requirements 
    pip install -r requirements.txt

##### Run the code
    cd task
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 
    
##### Behold!
Go to http://localhost:8000/
