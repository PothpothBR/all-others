from sprite_group import LoadSprites

class Animate(LoadSprites):
    
    def __init__(self):
        
        self.group = {}
        self.index_obj = []
        self.index_anim = []
    
    def new_object(self,identy,filename, cols_rows, surface, handle=0):
        self.group.update({identy:LoadSprites(filename,cols_rows,surface,handle)})
        self.index_obj.append(identy)
    
    def remove_object(self,identy):
        self.group.pop(identy)
        self.index_obj.remove(identy)
    
    def obj(self,identy):
        return self.group[identy]
    
    def index_object(self,identy,z_index):
        self.index_obj.remove(identy)
        self.index_obj.insert(z_index-1,identy)
        
    def index_animation(self,identy_obj,identy,z_index):
        self.group[identy_obj].index_anim.remove(identy)
        self.group[identy_obj].index_anim.insert(z_index-1,identy)
                   
    def draw_objs(self):
        
        for i in self.index_obj:
            i = self.group[i]
            for id in i.index_anim:
                i.draw_anim(i,id)
            
