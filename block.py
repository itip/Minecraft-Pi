from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create()

# pos = mc.player.getPos()
x,y,z = mc.player.getPos()

#mc.setBlock(x+1, y, z, block.LAVA.id)

mc.setBlocks(x+1,y+1,z+1, x+5,y+5,z+1,block.BRICK_BLOCK.id)