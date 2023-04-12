"""
Created on Apr 12, 2023

@author: Ron Bublitz

##
# @mainpage Priority Queue
#
# @section description_main Description
#Goal: Implement a simple priority queue_list. Assume an incoming stream of dictionaries 
#containing two keys: command to be executed and priority. Priority is an integer value [0, 10], 
#where work items of the same priority are processed in the order in which they are received.
#
# @section notes_main Notes
# - Specifically not using the available heapq module.


Time used:
9:30am - 10:45am
11:15am - 11:45am
1:00pm - 1:30pm
"""

class PriorityQueue:
    """Class containing functions to manage a priority queue
    """
    
    def __init__(self):
        self.queue_list = []
    
    
    def push(self, priority_command_dict):
        """Add to the queue.  Takes a dictionary containing 2 keys.
        
        @param priority_command_dict Dictionary which has keys: command, priority (integer value between 0 and 10)
        
        @return Nothing
        """
        
        # check if keys exist
        if "command" not in priority_command_dict.keys() or \
                "priority" not in priority_command_dict.keys():
            raise KeyError('Could not find "command" or "priority" as keys:', priority_command_dict)
    
        # use the item's priority
        # ensure priority is between 0 and 10
        priority = priority_command_dict['priority']
        if priority < 0:
            priority = 0
        elif priority > 10:
            priority = 10
        
        # place the item in the correct spot in the queue
        for count, item in enumerate(self.queue_list):
            p = item[0]
            # continue looping if the item's priority is less than the current priority
            if priority < p:
                continue        
            # there can be multiple similar priorities so ensure it is placed as the last item        
            elif priority == p:
                j = count
                while j < len(self.queue_list) and self.queue_list[j][0] == priority:
                    j += 1
                self.queue_list.insert(j, (priority, priority_command_dict['command']))  
                return
            # the item's priority is greater than the current priority so insert it
            else:
                self.queue_list.insert(count, (priority, priority_command_dict['command']))
                return
        
        # the item's priority is the lowest in the queue so append it to the end
        self.queue_list.append((priority, priority_command_dict['command']))
        
    
    def pop(self):
        """Get the next command in the queue.
        
        @return Returns command as string or None
        """
        
        if self.queue_list:
            # get the command as the second item in the tuple
            command = self.queue_list[0][1]
            # update the queue by removing the first item
            self.queue_list = self.queue_list[1:]
            return command
        return None


def do_test():
    """Function to test the features of the priority queue
    
    @return Nothing
    """
    
    p = PriorityQueue()
    #p.push({'command': 'commandA', 'pri': 1})  # error no 'priority' key
    p.push({'command': 'commandA', 'priority': 1})
    p.push({'command': 'commandB', 'priority': 5})
    p.push({'command': 'commandC', 'priority': 8})
    p.push({'command': 'commandD', 'priority': 5})
    p.push({'command': 'commandE', 'priority': 6})
    p.push({'command': 'commandF', 'priority': 5})
    p.push({'command': 'commandG', 'priority': 3})
    
    while True:
        command = p.pop()
        if command is None:
            break
        print(command)


if __name__ == '__main__':
    print('running test')
    do_test()
