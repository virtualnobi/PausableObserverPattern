#!python
# -*- coding: latin-1 -*-
"""
(c) by nobisoft 2016-
"""


# Imports
## Standard
## Contributed
## nobi
from ObserverPattern import Observer
from PausableObservable import PausableObservable



# Constants
AspectName = 'aspect'
MessageOne = 'no pausing'
MessageTwo = 'paused on object 1'
MessageThree = 'paused on class'



# Observable class
class PauseableObservableObject(PausableObservable):
    def __init__(self, identifier):
        super(PauseableObservableObject, self).__init__([AspectName])
        self.identifier = identifier
        self.message = ''
        
    def doChange(self, msg):
        self.message = msg
        self.changedAspect(AspectName)
        
    def getMessage(self):
        return('Observable %s changed (%s)' % (self.identifier, self.message))



# Observer class
class ObserverObject(Observer):
    def updateAspect(self, observable, aspect):
        Observer.updateAspect(self, observable, aspect)
        print(observable.getMessage())



# Globals
observableObject1 = PauseableObservableObject('1')
observableObject2 = PauseableObservableObject('2')
observerObject = ObserverObject()


# Executable Script
if __name__ == "__main__":
    observableObject1.addObserverForAspect(observerObject, AspectName)
    observableObject2.addObserverForAspect(observerObject, AspectName)
    observableObject1.doChange(MessageOne)
    observableObject2.doChange(MessageOne)
    print('Pausing updates from observable object 1')
    PausableObservable.pauseUpdates(observableObject1, None, None)
    observableObject1.doChange(MessageTwo)
    observableObject2.doChange(MessageTwo)
    PausableObservable.resumeUpdates(observableObject1, None, None)
    print('Pausing a class')
    PausableObservable.pauseUpdates(PauseableObservableObject, None, None)
    observableObject1.doChange(MessageThree)
    observableObject2.doChange(MessageThree)
    PausableObservable.resumeUpdates(PauseableObservableObject, None, None)
    print('No more pausing')
    observableObject1.doChange(MessageOne)
    observableObject2.doChange(MessageOne)
