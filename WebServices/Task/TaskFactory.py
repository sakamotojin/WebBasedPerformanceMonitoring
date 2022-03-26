from WebServices.Task.WebSitePerformanceTest import WebSitePerformanceTest
from WebServices.PersistanceStorage.PersistanceStorage import PersistanceStorage

class TaskFactory:
    TaskReferences = {}

    def __init__(self):
        TaskFactory.TaskReferences["WebSitePerformanceTest"] = WebSitePerformanceTest
        if not PersistanceStorage.getInstance().Tasks.checkTaskType(1):
            PersistanceStorage.getInstance().Tasks.addTaskType(1, "WebSitePerformanceTest", "For PerformanceTesting Of Dashboard")

    def getTask(self , Name, Value:dict):
        TaskId = int(Value["TaskId"])
        OnlyOnce, Interval, Description = int(Value["OnlyOnce"]), int(Value["Interval"]), str(Value["Description"])
        if Name == 'WebSitePerformanceTest':
            return TaskFactory.TaskReferences[Name](TaskId=TaskId, OnlyOnce=OnlyOnce, TaskInterval=Interval, Description=Description, Value=Value)
        raise Exception("Invalid TaskType")
