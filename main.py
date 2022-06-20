import mongoengine as db
import requests


database_name ='repositorio'
DB_URI = ''
db.connect(host=DB_URI)


class RepoUser(db.Document):
    user_id = db.IntField()
    name_user = db.StringField()
    repositorios = db.ListField()

    def to_json(self):
        return {
            'user_id': self.user_id,
            'name_user': self.name_user,
            'repositorios': self.repositorios
        }


user = str(input('User: '))

r = requests.get(f'https://api.github.com/users/{user}/repos')
repos = r.json()

repo_list = []


for repo in repos:
    repo_list.append(repo['name'])

user_repo = RepoUser(user_id =1,
                name_user = user,
                repositorios = repo_list)
user_repo.save()

print(user_repo.to_json())


