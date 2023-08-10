# NewsTeller
you just login and then mark some catagory for showing you in favorite part  

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/amirQuf/NewsTeller
   ```

2. Create a virtual environment:

   ```bash
   python -m venv env
   ```

3. Activate the virtual environment:

   ```bash
   source env/bin/activate
   ```

4. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up the database:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

The project should now be up and running on http://localhost:8000/.

## Usage
use username and password for login and get jwt and put in response body of your request and call  one of end points.

### 3rd party Pakages:
- Django
- simplejwt
- Django restframework
- swagger
- Pillow
- cors
- decouple

### Api end points:

  
### models:
- News
- category
- favcategory
-  
## Features
 - creating and updating News
 - login and register
 - adding and delte and update catagories
 - mark catagories as favcatgori
 - save News
   
## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes and ensure they are thoroughly tested.
4. Commit your changes and push them to your fork.
5. Submit a pull request, explaining the changes you have made.

Please adhere to the project's coding style, conventions, and guidelines. Be respectful and considerate when participating in discussions and addressing issues.

## License

Specify the license under which your Django project is distributed. For example, you can use the MIT License, GNU General Public License (GPL), or any other open-source license that aligns with your project's requirements. Make sure to include any license-related files or links in your project's repository.

Feel free to customize this README file based on your specific Django project. Include relevant details, instructions, and sections that best represent your project and provide value to users and potential contributors.

Good luck with your Django project!
