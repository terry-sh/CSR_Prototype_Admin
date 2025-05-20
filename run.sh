# Install dependencies
pip3 install --user pipenv

python3 manage.py runserver

# 更新数据模型
python3 manage.py makemigrations activity
python3 manage.py migrate

# 创建管理员账号
python manage.py createsuperuser

# Clean
rm -rf ./activity/migrations & rm db.sqlite3
