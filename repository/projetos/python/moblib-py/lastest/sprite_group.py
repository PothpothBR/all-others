
from spritesheet import LoadSpriteSheet

# classe para animar sprites de diferentes formas
# e agrupar animacoes de uma mesma spritesheet
class LoadSprites(LoadSpriteSheet):
    
    def __init__(self,filename,cols_rows,surface,handle=0):
        LoadSpriteSheet.__init__(self,filename,cols_rows[0],cols_rows[1],surface,handle)
        
        self.count = []
        self.interval = []
        self.start = []
        self.end = []
        self.direction = []
        self.identy = {}
        self.index_anim = []
        self.rangeOfCells = []
        self.flip = []
        self.jump = []
        self.x_y = []
        self.step = []
        #             nome|quant d/sprits|sprit d/inicio|direcao|intervalo entre sprites
    def new_animation(self,identy,x_y,rangeOfCells,startCell=1,direction=0,cellInterval=0,stepCell=0):
            
        self.identy.update({identy: len(self.end)})
        
        if direction == 2 or direction == 'flip':
            self.count.append(startCell)# -2
        else:
            self.count.append(startCell-2)# -2
        self.start.append(startCell-1)# -1
        self.end.append((startCell-1)+ rangeOfCells-1)
        self.x_y.append(x_y)            
        self.interval.append(cellInterval+1)
        self.jump.append(0)
        self.direction.append(direction)
        self.index_anim.append(identy)
        self.rangeOfCells.append(rangeOfCells-1)
        self.flip.append(-(stepCell+1))
        self.step.append(stepCell+1)
    
    def mod_anim_start(self,identy,start):
        i = self.identy[identy]
        
        self.start[i] = start -1
        if self.direction[i] == 2 or self.direction[i] == 'flip':
            self.count[i] = start
        else:
            self.count[i] = start -2 # -1 para contagem de vetor, -1 para o inicio
        self.end[i] = (start -1) + self.rangeOfCells[i] -1
    
    def mod_anim_range(self,identy,range):
        self.range[self.identy[identy]] = range - 1
        self.end[i] = self.start[self.identy[identy]] + range - 1
        
    def mod_anim_direction(self,identy,direct):
        self.direction[self.identy[identy]] = direct
        
    def mod_anim_step(self,identy,step):
        self.step[self.identy[identy]] = step+1
         
    def mod_anim_interval(self,identy,interval):
        self.interval[self.identy[identy]] = interval
    
    def anim_normal(self,identy):
        
        i = self.identy[identy]
       
        self.count[i] += self.step[i]
           
        if self.count[i] > self.end[i]:
            self.count[i] = self.start[i]
         
        return self.count[i]
        
    def anim_inverse(self,identy):
        
        i = self.identy[identy]
        
        self.count[i] -= self.step[i]
        
        if self.count[i] < self.start[i]:
            self.count[i] = self.end[i]
       
        return self.count[i]
    
    def anim_flip(self,identy):
        
        i = self.identy[identy]
        
        
        if self.count[i] <= self.start[i] or self.count[i] >= self.end[i]:
            
            self.flip[i] *= -1
            
        self.count[i] += self.flip[i]
           
  
        return self.count[i]
    
    def anim(self,identy):
        i = self.identy[identy]
        if self.jump[i] > 0:
            self.jump[i] -= 1
            return self.count[i]
        else:
            self.jump[i] = self.interval[i]
            if self.direction[i] == 0 or self.direction[i] == 'normal':
                return self.anim_normal(identy)
            
            elif self.direction[i] == 1 or self.direction[i] == 'inverse':
                return self.anim_inverse(identy)
            
            elif self.direction[i] == 2 or self.direction[i] == 'flip':
                return self.anim_flip(identy)
 
    def draw_animation(self, identy):
      
        self.draw(self.x_y[self.identy[identy]],self.anim(identy))
       
       
