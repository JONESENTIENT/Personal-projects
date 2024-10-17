# step 2 Now we import the init.py file
# website folder is now a python package since it holds init.py
from website import create_app

app = create_app()

# tells python to only run app if it is opened, not during import
if __name__ == '__main__':
    app.run(debug = True)
    