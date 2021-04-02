import traceback
from flask import request
import json
from WebServices.TaskSheduler.TaskScheduler import TaskScheduler
from WebServices.Task.TaskFactory import TaskFactory
from WebServices.PersistanceStorage.PersistanceStorage import PersistanceStorage


class Controller:
    __instance = None

    @staticmethod
    def getInstance():
        if Controller.__instance is None:
            Controller()
        return Controller.__instance

    def __init__(self):
        if Controller.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Controller.__instance = self
            self.TaskScheduler = TaskScheduler.getInstance()
            self.PersistanceStorage = PersistanceStorage.getInstance()
            self.TaskFactory = TaskFactory()
            self.TaskScheduler.start()



    def getTaskDetails(self):
        print('GET TASK DETAILS')
        try:
            data = request.json
            TaskId = int(data["TaskId"])
            response = json.dumps(self.PersistanceStorage.Tasks.getTaskInfo(TaskId))
            return response
        except Exception as e:
            traceback.print_exc()
            return {"Error" : "Error Processing Request" + str(e)}

    def addNewTask(self):
        print('ADD A NEW TASK')
        try:
            data = request.json
            print(data)
            TaskType = data["TaskType"]
            Value = dict(data["Arg"])
            print(Value)
            Value["TaskId"] = self.PersistanceStorage.Tasks.getTaskId()
            NewTask = self.TaskFactory.getTask(TaskType, Value)
            NewTask.addTaskToStorage()
            self.TaskScheduler.addTask(NewTask)
            return {"TaskId" : Value["TaskId"]}
        except Exception as e:
            traceback.print_exc()
            return {"Error": str(e)}


    #Not To Be Done Now
    def UpdateTask(self):
        print('Update Task')

    def DeleteTask(self):
        print('Delete Task')
        try:
            data = request.json
            TaskId = int(data["TaskId"])
            if self.TaskScheduler.isTaskIdPresent(TaskId):
                response = {"Success" : self.TaskScheduler.deleteTaskById(TaskId)}
            else:
                response = {"Success" : self.PersistanceStorage.Tasks.deleteTaskById(TaskId)}
            return response
        except Exception as e:
            traceback.print_exc()
            return {"Error" : "Error Processing Request" + str(e)}

    def getAllTasks(self):
        print("Get All Tasks")
        try:
            response = json.dumps(self.PersistanceStorage.Tasks.getAllTasks())
            return response
        except Exception as e:
            traceback.print_exc()
            return {"Error" : "Error Processing Request" + str(e)}

    def getTasksStatus(self):
        print('Update Task')


    def __del__(self):
        print("end")
