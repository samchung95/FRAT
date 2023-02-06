# FRAT
Facial Recognition Attendance Taker is an application that helps to take attendance using a webcam and the cascade classifier from OpenCV. A simple csv writer has been created to write the attendance of users whos face has been captured and has not been already written in the csv for that day.


# Installation
1. Install Python 3.10 from dependencies folder
1. Install Cmake from dependencies folder 
1. Instal Visio Studio <br>
Install the c++ compiler of the visual studio code community version

    ![image](https://user-images.githubusercontent.com/41113285/209984918-77f3893b-38fe-4430-b070-71ddfa9f78ac.png)
1.  Update pip, setuptools and wheel <br>
    ```
    py -m pip install --upgrade pip setuptools wheel
    ```

1. Set the execution policy for the current user scope <br>
    ```
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```

1. Optionally, create a virtual environment <br>
    ```
    py -m venv tutorial_env
    tutorial_env\Scripts\activate
    ```
1. Install requirements.txt <br>
    ```
    pip install -r requirements.txt
    ```

# Example

1. Run example.py

    ```
    python example.py
    ```


# How to use

0. import FRAT
    ```python
    from frat import FRAT
    ```

1. Create FRAT class with callback if any
    ```python
    frat = FRAT(callback)
    ```

2. Create encodings
    ```python
    frat.encodeFaces()
    ```
    Note: Make sure to put an image in a folder inside 'images' before encoding faces. e.g.(image/samuel/samuel.jpg)

3. Start FRAT
    ```python
    frat.start()
    ```


# References