# Password Generator App User Manual

## Introduction
The Password Generator App is a basic random password generator application that creates strong and customizable passwords for users. This user manual provides detailed instructions on how to install the app's environment dependencies and how to use the app effectively.

## Installation
To install the Password Generator App, please follow the steps below:

1. Ensure that you have Python installed on your system. If not, you can download and install Python from the official Python website: https://www.python.org/downloads/

2. Clone or download the project files from the repository.

3. Open a terminal or command prompt and navigate to the project directory.

4. Install the required dependencies by running the following command:
```
pip install -r requirements.txt
```

## Usage
To use the Password Generator App, follow the steps below:

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the following command to start the app:
```
python main.py
```

3. The Password Generator App window will open.

4. Enter the desired password length in the "Password Length" field.

5. Select the checkboxes for the character types you want to include in the password (lowercase, uppercase, numbers, symbols).

6. Click the "Generate Password" button.

7. The generated password will be displayed in the app window.

8. You can generate multiple passwords by repeating steps 4 to 7.

9. To exit the app, simply close the app window.

## Notes
- The app validates the password length input to ensure it is a positive integer. If an invalid input is provided, an error message will be displayed.

- The app uses the `password_generator.py` module to generate random passwords. You can customize the character types to include in the passwords by modifying the `generate_password` method in the module.

- The app is built using the Tkinter library for the graphical user interface. Tkinter is included in the `requirements.txt` file and will be installed automatically during the installation process.

- If you encounter any issues or have any questions, please refer to the documentation or contact our support team for assistance.

## Conclusion
Congratulations! You have successfully installed and learned how to use the Password Generator App. Enjoy generating strong and customizable passwords for your users! If you have any feedback or suggestions for improvement, please let us know.