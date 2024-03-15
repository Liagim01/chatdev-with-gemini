# ChatDev Umbrella Application User Manual

## Introduction

The ChatDev Umbrella Application is a Python-based application that simulates raindrops falling down the screen, with the mouse cursor acting as an umbrella to prevent raindrops from falling underneath it. This user manual provides detailed instructions on how to install the application and how to use it effectively.

## Installation

To install the ChatDev Umbrella Application, follow the steps below:

1. Make sure you have Python installed on your system. If not, download and install Python from the official Python website (https://www.python.org).

2. Clone the ChatDev Umbrella Application repository from GitHub using the following command:

   ```
   git clone https://github.com/ChatDev/Umbrella-Application.git
   ```

3. Navigate to the cloned repository directory:

   ```
   cd Umbrella-Application
   ```

4. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage

To use the ChatDev Umbrella Application, follow the steps below:

1. Open a terminal or command prompt and navigate to the cloned repository directory.

2. Run the main.py file using the following command:

   ```
   python main.py
   ```

3. A window will open displaying raindrops falling down the screen.

4. Move your mouse cursor to control the umbrella. The umbrella will follow the movement of the cursor.

5. Raindrops will not fall underneath the umbrella. They will bounce off the umbrella's surface.

6. Enjoy playing with the umbrella and raindrops!

## Customization

The ChatDev Umbrella Application can be customized according to your preferences. Here are a few customization options:

- Raindrop Speed: You can adjust the speed at which the raindrops fall by modifying the `fall` method in the `Raindrop` class in the `raindrop.py` file.

- Umbrella Image: You can replace the default umbrella image with your own image by modifying the `Umbrella` class in the `umbrella.py` file. Update the `self.image` attribute to point to the path of your custom image.

- Background Color: You can change the background color of the application window by modifying the `main.py` file. Look for the line `canvas.configure(bg='white')` and replace `'white'` with your desired color.

## Troubleshooting

If you encounter any issues while installing or using the ChatDev Umbrella Application, please try the following troubleshooting steps:

1. Make sure you have installed all the required dependencies correctly by running the `pip install -r requirements.txt` command again.

2. Check that your Python version is compatible with the application. The ChatDev Umbrella Application requires Python 3 or above.

3. Ensure that your system meets the minimum hardware requirements to run the application smoothly.

4. If the application crashes or freezes, try restarting your computer and running the application again.

If the issue persists, please contact our support team for further assistance.

## Conclusion

Congratulations! You have successfully installed and learned how to use the ChatDev Umbrella Application. Enjoy the experience of controlling the umbrella with your mouse cursor and preventing raindrops from falling underneath it. If you have any feedback or suggestions, please feel free to reach out to us. Happy coding!