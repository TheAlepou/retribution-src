from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class PVPGameCTLAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('PVPGameCTLAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)