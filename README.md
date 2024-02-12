# Description
This app is a submission of my second coding round at CatalystMI. The app's functionality is as follows:-
1. A web application coded in Django(4.2.10) which allows users to login, register to the `catalyst-count` application.
2. Users can upload a large volume (1GB) of data csv.
3. After the csv file is uploaded, one can view its data in the database.
4. A user can also create queries to get a count of all the data present in the database.

# Setup
1. Clone the repository -
```sh
$ git clone https://github.com/rohanpandavv/catalyst-count.git
$ cd catalyst_count
```
2. Create a virtual environment (OR) directly do a pip install of `requirements.txt` inside the root directory by running the following command -
```sh
$ pip install -r requirements.txt
```
3. Create a `.env` file in the same directory as `manage.py` and add the following variables in it -  
`SECRET_KEY={secret_key}`  
`DATABASE_URL={your_database_url}`  
`DATABASE_USERNAME={your_database_username}`  
`DATABASE_PASSWORD={your_database_password}`

4. You are now ready to run the `catalyst-count` application! Run the following command -  
```sh
$ ls
(NOW CHECK IF manage.py COMES IN THE LIST, if not then type in cd/catalyst-count)
python3 manage.py runserver
```
**the env variable python3 can vary from system to system so possible names of python's env varialbe are - python, python3, py, py3**

5. Once the local server starts running, go to the following endpoint to signup into the platform -
``http://127.0.0.1:8000/accounts/signup``
After the signup, a user is sent to `http://127.0.0.1:8000/csv/upload/` where they can upload a csv file (validation handled in case of any other extension being uploaded).

6. Once uploaded, go to `http://127.0.0.1:8000/query_builder/` url to access the filters on the data.
![Filter Success](https://i.imgur.com/pfDyQmv.png "Filter Success")

![Filter Error](https://i.imgur.com/RmDFv8F.png "Filter Failed")  

7. To add users, head to `http://127.0.0.1:8000/accounts/list/` url to access a list of all users.
![Users Table](https://i.imgur.com/jrYMmB8.png "Users Found")

[Dataset Used](https://www.dropbox.com/s/at6f63rdznw4bqs/free-7-million-company-dataset.zip?dl=0)
**note that the above dataset has 7 million rows in it and is 1gb in size**  

[Alternate Dataset for Testing](https://sendanywhe.re/E117MWZP)
