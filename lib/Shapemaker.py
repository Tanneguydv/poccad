import random
import string
from OCC.Core.BRepTools import breptools_Read, breptools_Write
from OCC.Core.TopoDS import TopoDS_Shape
from OCC.Core.BRep import BRep_Builder

class MakeShape:
    def __init__(self, method, parameters, use_brep):
        self.method = method
        self.parameters = parameters
        self.use_brep = use_brep

    def generate_random_name(self, length=8):
        """Génère un nom aléatoire de longueur donnée."""
        characters = string.ascii_lowercase
        return ''.join(random.choice(characters) for _ in range(length))

    def ensure_name_in_dict(self): #TODO check parameters vs line_input, même chose??
        """Vérifie si 'name' existe dans le dictionnaire, génère un nom aléatoire s'il est manquant."""
        for param_name, param_input in self.parameters.items():
            if param_input == "":
                if 'float' in param_name:
                    self.parameters[param_name] = 10.0
                elif 'str' in param_name:
                    self.parameters[param_name] = self.generate_random_name()
                elif 'pnt' in param_name:
                    self.parameters[param_name] = 'gp_Pnt(0, 0, 0)'
                elif 'axe' in param_name:
                    self.parameters[param_name] = 'axis'

    def generate_prompt(self):
        prompt = 'Press Enter or specify: '
        for param_name, param_type in self.parameters.items():
            prompt += f'<u>{param_name[0].upper()}</u>{param_name[1:]}, '

        prompt = prompt[:-2]  # Supprime la virgule en trop à la fin
        return prompt
    
    def set_name_dumped_shape(self, name):
        self.dumped_shape_name = name

    def generate_command(self, input_line):
        self.parameters = input_line
        self.ensure_name_in_dict()
        for param_name, param_type in self.parameters.items():
            if param_name is 'name_str':
                self.name = input_line.get(param_name, '0')
                if self.method == '':
                    command = f'{self.name} = occ.'
                else:
                    command = f'{self.name} = occ.{self.method}('
            elif "edge" in param_name and "axe" in param_name:
                command = f'edge=occ.load_shape("{self.dumped_shape_name}")\n' + \
                'axis=occ.ax2_from_edge(edge)\n' + command
            else :
                param_value = input_line.get(param_name, '0')  # Utilise '0' comme valeur par défaut si non spécifié
                command += f'{param_value}, '

        command = command[:-2]  # Supprime la virgule en trop à la fin
        if self.method != '':
            command += f')'
        return command


class MakeBox(MakeShape):
    def __init__(self):
        method = 'Box'
        parameters = {
            'name_str': 'str',
            'pnt_pick' : 'gp_Pnt',
            'sizeX_float': 'float',
            'sizeY_float': 'float',
            'sizeZ_float': 'float',
        }
        use_brep = False
        super().__init__(method, parameters, use_brep)

class MakeCylinder(MakeShape):
    def __init__(self):
        method = 'Cylinder'
        parameters = {
            'name_str': 'str',
            'pick_edge_axe' : 'edge',
            'radius_float': 'float',
            'length_float': 'float',
        }
        use_brep = True
        super().__init__(method, parameters, use_brep)

class CenterPoint(MakeShape):
    def __init__(self):
        method = ''
        parameters = {
            'name_str' : 'str',
            'face_pick' : 'gp_Pnt',
        }
        use_brep = False
        super().__init__(method, parameters, use_brep)



class ShapeConverter():
    def __init__(self) -> None:
        pass

    def generate_random_name(self, length=8):
        """Génère un nom aléatoire de longueur donnée."""
        characters = string.ascii_lowercase
        return ''.join(random.choice(characters) for _ in range(length))+'.brep'

    def dump_shape(self, shape_to_convert, name=None):
        if name is None:
            name = self.generate_random_name()
            breptools_Write(shape_to_convert, name)
            return name
        else:
            breptools_Write(shape_to_convert, name)

    def load_shape(self, name):
        shape = TopoDS_Shape()
        builder = BRep_Builder()
        breptools_Read(shape, name, builder)
        return shape

def main():
    make_box = MakeBox()
    # make_box = CenterPoint()
    print(make_box.generate_prompt())

    input_line = {
        'point': 'gp_Pnt(0, 0, 0)',
        'sizeX': '10',
    }

    command = make_box.generate_command(input_line)
    print(command)


if __name__ == '__main__':
    main()

