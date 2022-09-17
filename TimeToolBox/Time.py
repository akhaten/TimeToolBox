import abc
import datetime


class SimpleDuration:

    def __init__(self, duration: datetime.timedelta) -> None:
        self.duration: datetime.timedelta = duration
        
    @property
    def duration(self) -> datetime.timedelta:
        return self.__duration


    @duration.setter
    def duration(self, value: datetime.timedelta):

        if not isinstance(value, datetime.timedelta):
            raise TypeError('\"duration\" must be datetime.timedelta')
        
        if value < datetime.timedelta(0) :
            raise AssertionError('\"duration\" must be higher than datetime.timedelta(0)')
        
        self.__duration: datetime.timedelta = value


    def export(self) -> dict:
        return { 'duration' : str(self.duration) }


    def __eq__(self, other: "SimpleDuration") -> bool:

        if not isinstance(other, SimpleDuration):
            return False
        
        return self.duration == other.duration


class SimpleTime(SimpleDuration):


    def __init__(self, begin: datetime.datetime, duration: datetime.timedelta):
        SimpleDuration.__init__(self, duration)
        self.begin: datetime.datetime = begin


    @property
    def end(self) -> datetime.datetime:
        return self.begin+self.duration


    @end.setter
    def end(self, value: datetime.timedelta) -> None:
        raise AttributeError('\"end\" is not writeable')

    def export(self) -> dict:
        export: dict = SimpleDuration.export(self)
        export['begin'] = str(self.begin)
        return export

    @classmethod
    def make(cls, begin: datetime.datetime, end: datetime.datetime) -> "SimpleTime":
    
        if end <= begin:
            raise ValueError('\"end\" must be higher than \"begin\"')
        
        duration: datetime.timedelta = end-begin
        
        return SimpleTime(begin, duration)
        
    @classmethod
    def copy(cls, other: "SimpleTime") -> "SimpleTime":
        if not isinstance(other, SimpleTime):
            raise AssertionError('object is not a instance of \"SimpleTime\"')
        return SimpleTime(other.begin, other.duration)


    def __eq__(self, other: "SimpleTime") -> bool:
        if not isinstance(other, SimpleTime):
            return False
        return (self.begin == self.begin) and SimpleDuration.__eq__(self, other)



class SimpleEvent(SimpleTime):

    
    class AbstractInformation(abc.ABC):

        @abc.abstractmethod
        def export(self) -> dict:
            pass

        @abc.abstractmethod
        def __eq__(self, other: "SimpleEvent.AbstractInformation") -> bool:
            pass

        @abc.abstractmethod
        def __str__(self) -> str:
            pass
        


    def __init__(self, infos: AbstractInformation, begin: datetime.datetime, duration: datetime.timedelta):
        self.infos: SimpleEvent.AbstractInformation = infos
        SimpleTime.__init__(self, begin, duration)


    @classmethod
    def make(cls, infos: AbstractInformation, begin: datetime.datetime, end: datetime.datetime) -> "SimpleEvent":
        duration: datetime.timedelta = end-begin
        return SimpleEvent(infos, begin, duration)
        

    def export(self) -> dict:
        export: dict = SimpleTime.export(self)
        export_infos: dict = self.infos.export()
        export.update(export_infos)
        return export


    def __eq__(self, other: "SimpleEvent")-> bool:

        if not isinstance(other, SimpleEvent):
            return False

        return (self.infos == other.infos) \
            and (self.begin == other.begin) \
            and (self.duration == other.duration)


