


class Todo:
    tasks = []

    def add(self,task):
        self.tasks.append(task)
        print(self.tasks)
    
    def delete(self,task):
        self.tasks.remove(task)
        print(self.tasks)
    def get_tasks(self):
        return self.tasks