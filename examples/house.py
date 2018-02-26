# See images/house1.jpg to see what this looks like

from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create()

x,y,z = mc.player.getPos()

## Front and back

for num in range(1, 3):

    z_pos = z + (num * 5)
    print(z_pos, end='\n')

    # Bottom row
    mc.setBlocks(x+3,y,z_pos, x-3,y,z_pos,block.BRICK_BLOCK.id)

    # Either side of windows and in between
    mc.setBlock(x+3, y+1, z_pos, block.BRICK_BLOCK.id)
    mc.setBlock(x-3, y+1, z_pos, block.BRICK_BLOCK.id)
    mc.setBlocks(x+1,y+1,z_pos, x-1,y+3,z_pos,block.BRICK_BLOCK.id)

    # Row above door
    mc.setBlocks(x+3,y+2,z_pos, x-3,y+2,z_pos,block.BRICK_BLOCK.id)

    # Either side of windows and in between
    mc.setBlock(x+3, y+3, z_pos, block.BRICK_BLOCK.id)
    mc.setBlock(x-3, y+3, z_pos, block.BRICK_BLOCK.id)
    mc.setBlocks(x+1,y+3,z_pos, x-1,y+3,z_pos,block.BRICK_BLOCK.id)

    # Top row
    mc.setBlocks(x+3,y+4,z_pos, x-3,y+4,z_pos,block.BRICK_BLOCK.id)

    # Windows
    mc.setBlock(x+2, y+1, z_pos, block.GLASS_PANE.id)
    mc.setBlock(x-2, y+1, z_pos, block.GLASS_PANE.id)
    mc.setBlock(x+2, y+3, z_pos, block.GLASS_PANE.id)
    mc.setBlock(x-2, y+3, z_pos, block.GLASS_PANE.id)
    
# Sides
for num in [+3, -3]:
    x_pos = x + num
    mc.setBlocks(x_pos,y,z+5, x_pos,y+4,z+10,block.BRICK_BLOCK.id)

# Roof
#mc.setBlocks(x+3,y+5,z+5, x-3,y+5,z+10,block.STONE.id)
#mc.setBlocks(x+2,y+6,z+6, x-2,y+6,z+9,block.STONE.id)
#mc.setBlocks(x+1,y+7,z+7, x-1,y+7,z+8,block.STONE.id)
#mc.setBlocks(x,y+8,z+7, x,y+8,z+7,block.STONE.id)

mc.setBlocks(x+3,y+5,z+5, x-3,y+5,z+10,block.STONE_SLAB.id)

# Door (in front of user)
mc.setBlocks(x,y,z+5, x,y+1,z+5,block.WOOD.id)




