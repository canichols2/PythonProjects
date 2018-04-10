from time import sleep

# def compute():
#     rv = []
#     for i in range(10):
#         sleep(.5)
#         rv.append(i)
#     return rv


# class Compute:
#     def __iter__(self):
#         self.last = 0
#         return self
    
#     def __next__(self):
#         rv=self.last
#         self.last += 1
#         if self.last > 10:
#             raise StopIteration()
#         sleep(.5)
#         return rv

def Compute():
    for i in range(10):
        sleep(.5)
        yield i

for val in Compute():
    print(val)