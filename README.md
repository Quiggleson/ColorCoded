# ColorCoded

## Development server
Every time you pull new code, run the following to update necessary packages:
```bash
npm i
pip install -r requirements.txt # Make sure you're in the src/api/ directory
```

### Front end

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

### Back end

In a new terminal, navigate to `src/api/` then run the following commands:

#### Virtual environment 
Creating the virtual environment only has to be done once and is only required for the python portion of this project <br>
Run the following to create the virtual environment
```
python -m venv .venv
```
Activating a virtual environment has to be done with every new terminal session <br>
Run the following commands to work with the virtual environment on unix or [See here for other systems](https://docs.python.org/3/library/venv.html#how-venvs-work)
```bash
. .venv/bin/activate # Activate the virtual env
deactivate # Deactivate the virtual env
```

# Angular mumbo jumbo
## Code scaffolding
Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build
Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.
