
# iBioML

Our main research area is pattern recognition in bioinformatics, especially, biological motif analysis. We developed various bioinformatics tools online.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/K-Tech22/iBioML.git
   cd biotechwebsite
   ```
Create a virtual environment and activate it:
   ```bash
    python -m venv myenv
    source myenv/bin/activate
 
```
Install the required dependencies using pip:
   ```bash
    pip install -r requirements.txt
   ```
Apply the database migrations:
   ```bash 
    python manage.py migrate
   ```
Start the development server:

   ```bash
python manage.py runserver
   ```
The development server will be accessible at http://localhost:8000/.


Project Structure
The main files and directories in this project are:

biotechwebsite/: The main Django project directory.

biotech/: An app directory containing the application's logic and views.
    
register/: An app directory containing the application's logic and views.

manage.py: The Django management script for running various commands.

requirements.txt: A file containing the project's dependencies.