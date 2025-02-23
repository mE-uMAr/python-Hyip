# Python HYIP

This repository contains a Python-based High Yield Investment Program (HYIP) script. The script is designed to manage and track investments, calculate returns, and handle user accounts.

## Features

- User account management
- Investment tracking
- Return calculation
- Referal and invite mechanism
- Admin dashboard
- Secure authentication
- Secure Depositt and Withdraw System

## Installation and Usage

1. #### Clone the repository:
    ```sh
    git clone https://github.com/mE-uMAr/python-Hyip.git
    cd python-Hyip
    ```

2. #### Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. #### Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. #### Install Django:
    ```sh
    pip install django
    ```
5. #### Navigate to directory
    Look for manage.py navigte to that directory using
    ```sh
    cd <path to manage.py>
    ```
6. #### Make Migrations
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```
7. #### Run Server
    ```sh
    python manage.py runserver
    ```

2. Access the application in your web browser at `http://localhost:8000`.

## Configuration

- Update the configuration settings in `settings.py` to match your environment and requirements.

## Contributing

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m "Description of changes"
    ```
4. Push to the branch:
    ```sh
    git push origin feature-branch
    ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or inquiries, please contact the repository owner.
