class Call(object):
    def __init__(self, i_d, caller_name, caller_number, time_of_call, reason_for_call):
        self.id = i_d
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call

    def callAttributes(self):
        print "ID: " + str(self.id)
        print "Caller Name: " + self.caller_name
        print "Caller Phone Number: " + self.caller_number
        print "Time of Call: " + self.time_of_call
        print "Reason for Call:" + self.reason_for_call
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)
        

    def add(self, call):
        self.calls.append(call)
        self.queue_size+=1
        print self.queue_size
        return self.calls       

    def remove(self):
        self.calls.pop()
        self.queue_size-=1
        return self

    def info(self):
        for call in self.calls:
            print Call(caller_name), Call(caller_number)
        print self.queue_size
        return self

cc = CallCenter()
cc.add(Call(123124, 'Sam', '654-234-4532', '12:23', 'just checkinig in'))
cc.add(Call(1231, 'Laura', '533-234-2342', '13:32', 'complain'))


print CallCenter().info()