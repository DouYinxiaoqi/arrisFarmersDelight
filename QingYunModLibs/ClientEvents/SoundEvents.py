# coding=utf-8
OnMusicStopClientEvent = "OnMusicStopClientEvent"
'''
描述

音乐停止时，当玩家调用StopCustomMusic来停止自定义背景音乐时，会触发该事件

参数

musicName	str	音乐名称
返回值

无
'''


PlayMusicClientEvent = "PlayMusicClientEvent"
'''
描述

播放背景音乐时触发

参数

name	str	即资源包中sounds/music_definitions.json中的event_name，并且对应sounds/sound_definitions.json中的key
cancel	bool	设为True可屏蔽该次音效播放
返回值

无
'''


PlaySoundClientEvent = "PlaySoundClientEvent"
'''
描述

播放场景音效或UI音效时触发

参数

name	str	即资源包中sounds/sound_definitions.json中的key
pos	tuple(float,float,float)	音效播放的位置。UI音效为(0,0,0)
volume	float	音量，范围为0-1
pitch	float	播放速度，正常速度为1
cancel	bool	设为True可屏蔽该次音效播放
返回值

无
'''