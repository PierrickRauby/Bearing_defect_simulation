# from dataclasses import dataclass, field
# from typing import Callable
# 
# @dataclass(order=True)
# class Event:
        # t: int
        # f: Callable=field(compare=False) 
# 
# class FutureEventList:
    # def __init__(self):
        # self.events = []
    # def __iter__(self):
        # return self
# 
    # def __next__(self) -> Event:
        # from heapq import heappop
        # if self.events:
            # return heappop(self.events)
        # raise StopIteration
    # def __repr__(self) -> str:
        # from pprint import pformat
        # return pformat(self.events)
# 
# def schedule(e: Event, fev: FutureEventList):
    # from heapq import heappush
    # heappush(fev.events, e)
