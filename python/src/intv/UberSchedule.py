import yaml

thetasks = """
task1:
    cores_required: 2
    execution_time: 100
task2:
    cores_required: 1
    execution_time: 200
task3:
    cores_required: 4
    execution_time: 50
task4:
    cores_required: 3
    execution_time: 70
task5:
    cores_required: 2
    execution_time: 40
    parent_tasks: "task1, task2"
task6:
    cores_required: 5
    execution_time: 100
    parent_tasks: task2
task7:
    cores_required: 3
    execution_time: 150
    parent_tasks: task3
task8:
    cores_required: 1
    execution_time: 80
    parent_tasks: task5
task9:
    cores_required: 2
    execution_time: 120
    parent_tasks: "task2, task6"
task10:
    cores_required: 3
    execution_time: 90
    parent_tasks: task7
"""

class Task(object):
    PRIORITY_DEFAULT = 0
    def __init__(self, task, cores, exetime, ptasks):
        self.task = task
        self.cores = cores
        self.exetime = exetime;
        self.ptasks = set(ptasks)
        self.labelled = False
        self.path_time = 0
        self.track = 0     # only track the last node
        self.priority = Task.PRIORITY_DEFAULT

    def priority_set(self):
        return self.priority != Task.PRIORITY_DEFAULT

    def __str__(self):
        return "Task {0:2d}: cores {1}; exetime {2:3d}; path_time {3:4d}; parent tasks {4}; track {5:2d}; priority{6:2d}".format(
            self.task, self.cores, self.exetime, self.path_time, self.ptasks, self.track, self.priority
        )

def build_tree():
    # Read all the tasks
    T = []

    doc = yaml.load(thetasks)
    for k,v in doc.items():
        task = int(k.replace('task', ''))
        if 'execution_time' in v:
            exetime = v['execution_time']
        if 'cores_required' in v:
            cores = v['cores_required']
        if 'parent_tasks' in v:
            stasks = v['parent_tasks']
            stasks = stasks.replace('task', '')
            stasks = stasks.replace(' ', '')
            ptasks = stasks.split(',')
            ptasks = [int(i) for i in ptasks]
        else:
            ptasks = set()          # empty set

        t = Task(task, cores, exetime, ptasks)
        T.append(t)

    return T

def build_layers(T):
    Layers = []
    layered_nodes = set()

    while True:
        L = set()
        for t in T:
            if t.labelled: continue
            if not (t.ptasks - layered_nodes):
                L.add(t)
                t.labelled = True
        Layers.append(L)
        layered_nodes |= set([l.task for l in L])
        if len(layered_nodes) >= len(T): break

    return Layers

def calculate(T, Layers):
    task_left = False
    for layer in Layers:
        for task in layer:
            if task.priority_set(): continue
            task_left = True
            
            if not task.ptasks:
                task.path_time = 0
            else:
                max_path_time = -99
                for k in task.ptasks:
                    ptask = T[k-1]
                    if ptask.priority_set(): continue
                    if ptask.path_time + ptask.exetime > max_path_time:
                        max_path_time = ptask.path_time + ptask.exetime
                        task.track = k
                task.path_time = max_path_time
    return task_left

def print_schedule(T, Layers):
    print "\n\nThe schdule is:"
    for layer in Layers:
        task_list = sorted(layer, key=lambda x : x.priority)
        for a in task_list:
            print a
        

def main():
    T = build_tree()

    Layers = build_layers(T)
    for i, l in enumerate(Layers):
        print i, [x.task for x in l]

    priority = 0
    layer_to_check = len(Layers) - 1
    while True:
        for t in T: t.path_time = 0         # reset the path_time
        task_left = calculate(T, Layers)
        if not task_left:
            for t in T: print t
            print_schedule(T, Layers)
            return

        # Find the back track path
        last_layer = Layers[layer_to_check]
        max_time = 0
        candidate = 0
        find_task = False
        for task in last_layer:
            if task.priority_set(): continue
            find_task = True
            if task.path_time + task.exetime > max_time:
                max_time = task.path_time + task.exetime
                candidate = task
        if not find_task:
            if layer_to_check <= 0: break
            layer_to_check -= 1
            continue
        print "Find the max length candidate task [", candidate, "]. Timespan is", max_time
        priority += 1
        candidate.priority = priority

        track = [candidate.task]
        while candidate.track > 0:
            task = T[candidate.task - 1]
            candidate = T[task.track - 1]
            candidate.priority = priority
            track.insert(0, candidate.task)
        print track

if __name__ == "__main__":
    main()