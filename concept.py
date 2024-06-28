import random
import threading

def sortus(input):
    change = True
    while change:
        change = False
        for i in range(1, len(input)):
            if input[i-1] > input[i]:
                input[i], input[i-1] = input[i-1], input[i]
                change = True
    return input

def create_testdata(num, max_val):
    return [random.randint(0, max_val) for _ in range(num)]

def split_into_many(input, tasksnum):
    number_per_vector = int((len(input) / tasksnum) + 1)
    output = []
    num = 0
    for _ in range(tasksnum):
        temp = []
        for _ in range(number_per_vector):
            if len(input) > num:
                temp.append(input[num]) 
                num += 1
        output.append(temp)
    return output

def sort_agent(input, tasksnum):
    def task(sublist):
        sorted_sublist = sortus(sublist)
        with lock:
            ninput.append(sorted_sublist)
    
    while tasksnum > 0:
        input = split_into_many(input, tasksnum)
        global ninput
        ninput = []
        threads = []
        lock = threading.Lock()
        
        for sublist in input:
            thread = threading.Thread(target=task, args=(sublist,))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
        
        input = []
        for sublist in ninput:
            input.extend(sublist)
        
        tasksnum //= 2
    
    return sortus(input)

if __name__ == "__main__":
    daten = create_testdata(100000, 10000)
    print(sort_agent(daten, 20))
