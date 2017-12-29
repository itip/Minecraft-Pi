from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# pos = mc.player.getPos()
x,y,z = mc.player.getPos()

print("X: %1.2f, Y:%1.2f, Z:%1.2f" % (x, y, z))

# Teleport

mc.player.setPos(x, y+20, z)