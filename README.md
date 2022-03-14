
## My Two Cents

# Description

This is a personal blogging website where you can create and share your opinions and other users can read and comment on them. Additionally, users can create and manage their own blogs, with the ability to delete inappropriate comments.

## Author

[Sharon Korir](https://github.com/sharonkorir)

# Dependencies

In order for you to use the content on this repo ensure you have the following:

- A computer that runs on either of the following; (Windows 7+, Linux, Mac OS)
- Python 3.x+

## Screenshot

<img src="" >

## Installation/setup instructions

To get the code..

1. Cloning the repository:

```bash
git clone https://github.com/sharonkorir/my-two-cents.git
```

2. Navigate to the folder and install requirements. 

```bash
cd my-two-cents
python3 -m venv virtual
pip install -r requirements.txt
```

3. Exporting Configurations

```bash
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
```

4. Running the application

```bash
python3 manage.py server
```

5. Testing the application

```bash
python3 manage.py test
```

Open the application on localhost `127.0.0.1:5000`.

## Live link

https://my-two-cents-blog.herokuapp.com/

## Technology used

* [Python3.8](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)

## Known Bugs

- No known bugs yet

## Support and contact details

If you run into any issues or have questions, ideas or concerns, reach out to me via e-mail, at sharon.korir@student.moringaschool.com

### License
https://choosealicense.com/licenses/mit/ 
Copyright (c) {2022} **Sharon Korir**

