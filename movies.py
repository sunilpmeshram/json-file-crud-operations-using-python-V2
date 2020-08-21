import json
from datetime import datetime


class MoviesClass:
    filename = 'movies.json'

    def __init__(self):
        with open(MoviesClass.filename, encoding="utf8") as json_file:
            self.data = json.load(json_file)

    def dump_data(self, updated_data):
        with open(MoviesClass.filename, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_record(self, new_data):
        self.data.append(new_data)
        self.dump_data(self.data)
        return True

    def update_record(self, title):
        res = [sub['Title'] for sub in self.data if sub['Title'] in title]
        if res.count(title) > 1:
            raise Exception("Title is not Unique!")
        else:
            for i in self.data:
                if i['Title'] == title:
                    print(i)
                    new_title = str(input("Please enter new title: "))
                    i['Title'] = new_title

            self.dump_data(self.data)
        return True

    def find_record(self, title):
        res = [sub['Title'] for sub in self.data if sub['Title'] in title]
        if res.count(title) == 0:
            raise Exception("Record not found!")
        else:
            for i in self.data:
                if i['Title'] == title:
                    res = i
        return res

    def delete_record(self, title):
        res = [sub['Title'] for sub in self.data if sub['Title'] in title]
        if res.count(title) == 0:
            raise Exception("Record not found!")
        else:
            for i in self.data:
                if i['Title'] == title:
                    self.data.remove(i)

            self.dump_data(self.data)
        return True

    def listing(self, key, value):
        new_list = []
        if key == 'Major_Genre':
            for i in self.data:
                if i[key] == value:
                    new_list.append(i)
        else:
            for i in self.data:
                dt = datetime.strptime(i[key], "%b %d %Y")
                if dt.year == value:
                    new_list.append(i)

        return new_list
