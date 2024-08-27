# -*- coding: utf-8 -*-
from QingYunModLibs.ModInit.QingYunMod import *
Mod = QingYunMod()
Mod.InitMod("arrisFarmersDelightScripts")
# ================ 通用 ================
Mod.ServerInit("modServer.farmersDelightCommon")
Mod.ClientInit("modClient.farmersDelightCommon")
# ================ 厨锅 ================
Mod.ServerInit("modServer.cookingPot")
Mod.ClientInit("modClient.cookingPot")
# ================ 附加效果 ================
Mod.ServerInit("modServer.effect")
# ================ 绳子与安全网 ================
Mod.ServerInit("modServer.ropeAndNet")
# ================ 农作物耕作与沃土 ================
Mod.ServerInit("modServer.farmCrop")
# ================ 盘装食物 ================
Mod.ServerInit("modServer.platePackagedFood")
# ================ 煎锅 ================
Mod.ServerInit("modServer.skillet")
Mod.ClientInit("modClient.skillet")
# ================ 炉灶 ================
# Mod.ServerInit("modServer.xxx")
# Mod.ClientInit("modClient.xxx")
# ================ 砧板 ================
# Mod.ServerInit("modServer.xxx")
# Mod.ClientInit("modClient.xxx")
