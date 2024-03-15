# Digital Clock Application User Manual

## Introduction

The Digital Clock Application is a simple mobile application developed in Python that displays the current time in either a 12-hour or 24-hour format. This user manual provides detailed instructions on how to install the necessary dependencies and how to use the application.

## Installation

To install the Digital Clock Application, follow these steps:

1. Ensure that you have Python installed on your system. If not, download and install Python from the official website (https://www.python.org).

2. Clone the repository containing the application code from the GitHub repository: [link to repository].

3. Open a terminal or command prompt and navigate to the directory where the application code is located.

4. Create a virtual environment for the application by running the following command:

   ```
   python -m venv venv
   ```

5. Activate the virtual environment by running the appropriate command for your operating system:

   - Windows: 
     ```
     venv\Scripts\activate
     ```

   - macOS/Linux:
     ```
     source venv/bin/activate
     ```

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage

To use the Digital Clock Application, follow these steps:

1. Ensure that the virtual environment is activated. If not, activate it using the command mentioned in step 5 of the installation process.

2. Run the main.py file using the following command:

   ```
   python main.py
   ```

3. The application will display the current time in the console. By default, the time will be displayed in a 24-hour format. If you want to display the time in a 12-hour format, you can modify the settings.py file by changing the value of the `TIME_FORMAT_24H` variable to `False`.

4. The application will continuously update the displayed time every second.

5. To stop the application, press `Ctrl + C` in the terminal or command prompt.

## Conclusion

Congratulations! You have successfully installed and used the Digital Clock Application. Enjoy using the application to display the current time in either a 12-hour or 24-hour format. If you have any questions or encounter any issues, please refer to the documentation or contact our support team for assistance.