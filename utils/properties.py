import json, os


def create_properties_file(path):
    properties = {'lastPage': 0}
    write_properties(path, properties)
    
    
def write_properties(path, properties):
    with open(get_path(path, 'properties.json'), 'w') as properties_file:
        json.dump(properties, properties_file)
        
        
def read_properties(path):
    with open(get_path(path, 'properties.json')) as properties_file:
        return json.load(properties_file)
    
    
def read_property(path, property_name):
    data = read_properties(path)
    return data[property_name]


def update_property(path, property_name, property_value):
    data = read_properties(path)
    data[property_name] = property_value
    write_properties(path, data)

    
def get_path(path, file_name):
    if path == '':
        return file_name
    return path + '/' + file_name