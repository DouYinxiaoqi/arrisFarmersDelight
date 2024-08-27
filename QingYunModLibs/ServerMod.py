# -*- coding: utf-8 -*-
from SystemApi import *
import ServerApi
import ServerEvents
_TimerData = list()


class _Timer(object):
    def __init__(self, Time, Func, Data, While):
        self.DefaultTime = 0
        self.Time = Time
        self.Func = Func
        self.Data = Data
        self.Stop = False
        self.While = While
        self.Destroy = False


@ListenServer("OnScriptTickServer")
def _ComputeTimerServer():
    for Timer in _TimerData:
        Time = Timer.Time
        if Timer.Stop:
            continue
        if Time > 0:
            Timer.Time -= 1
            continue
        Func = Timer.Func
        Data = Timer.Data
        try:
            Func(*Data)
        except Exception as error:
            print "\n %s 延时器迭代过程中发生错误(Having An Error) at %s \n %s %s" % (Bcolors.ERROR, Func.__name__, Bcolors.ERROR, error)
        if Timer.While:
            Timer.Time = Timer.DefaultTime
            continue
        Timer.Destroy = True
        _TimerData.remove(Timer)
        del Timer


def SerTimerState(Timer, State):
    """
    设置延时器运行状态(是否暂停延时器)

    :param Timer: 延时器对象
    :param State: 开关状态(True为开始延时，False为暂停延时)
    """
    Timer.Stop = State


def DestroyTimer(Timer):
    """
    注销延时器(完全销毁，注销后无法再对该延时器对象进行有效操作)

    :param Timer: 延时器对象
    """
    Timer.Stop = True
    if Timer in _TimerData:
        _TimerData.remove(Timer)
    del Timer


def SetTimerTime(Timer, Time, Keep=False):
    """
    动态修改延时器时间

    :param Timer: 延时器对象
    :param Time: 要设置的时间
    :param Keep: 是否接上之前已经经过的时间，设置为True则会沿已经经过的时间继续计时，否则清空之前的时间，重新计时
    """
    if Keep:
        Timer.Time = Time*30 - Timer.Time
    else:
        Timer.Time = Time * 30
    Timer.DefaultTime = Timer.Time


def CreateTimer(Time, Func, While, *args):
    """
    创建延时器，用于延时执行函数任务

    :param Time: 延时的时间，单位为秒/s
    :param Func: 延时执行的函数，函数将会在指定时间后执行
    :param While: 是否循环延时执行，启动后延时器会重复间隔指定时间后执行一次函数，可用StopTimer停止或DestroyTimer彻底注销
    :param args: 延时函数执行时所需要的参数
    :return: Timer 该延时器的可操作对象
    """
    Timer = _Timer(Time*30.0, Func, args, While)
    Timer.DefaultTime = Timer.Time
    _TimerData.append(Timer)
    return Timer


print "\n%s[QyMod] ServerMod加载完毕" % Bcolors.SUC