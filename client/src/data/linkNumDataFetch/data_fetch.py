# Link num data fetch for bar chart information
import json
with open('/Users/lexiezhou/Desktop/Visual_KnowledgeGraph/client/src/data/datav4/new_records4.json', encoding='utf-8-sig') as f:
    data = json.load(f)

nodes_data = []
labels = ['api', 'database', 'hardware', 'library', 'operating_system', 'programming_language', 'software', 'tool']
api_link_num = []
db_link_num = []
hw_link_num = []
lib_link_num = []
os_link_num = []
pl_link_num = []
sw_link_num = []
tool_link_num = []
driver_link_num = []
runtime_link_num = []
application_link_num = []

official_name = {
    "wxpython": "wxPython",
    "tensorflow": "TensorFlow",
    "tfds": "TensorFlow Datasets",
    "tensorboard": "TensorBoard",
    "pytorch": "PyTorch",
    "numpy": "NumPy",
    "scipy": "SciPy",
    "scikit-learn": "scikit-learn", 
    "pandas": "pandas",
    "keras": "Keras",
    "flask": "Flask",
    "tensorflow-transform": "TensorFlow Transform",
    "zappa": "Zappa",
    "subprocess": "subprocess",
    "sqlalchemy": "SQLAlchemy",
    "psycopg": "psycopg",
    "flask-sqlalchemy": "Flask SQLAlchemy",
    "airflow": "Airflow",
    "fftw": "FFTW",
    "tensorflow-core-platform": "TensorFlow Core Platform",
    "cuda": "CUDA",
    "cudnn": "cuDNN",
    "python": "Python",
    "ubuntu": "Ubuntu",
    "windows": "Windows",
    "macos": "macOS",
    "centos": "CentOS",
    "android": "Android",
    "ios": "iOS",
    "debian": "Debian",
    "bazel": "Bazel",
    "glibc": "glibc",
    "jetpack": "JetPack",
    "gcc": "GCC",
    "gzip": "gzip",
    "coremltools": "Core ML Tools",
    "postgres": "PostgreSQL",
    "mysql": "MySQL",
    "blender": "Blender",
    "emr": "Amazon EMR"
}


# add node id, name and version information
for i in range(len(data['nodes'])):
    name = data['nodes'][i]['name']
    if name in official_name:
        name = official_name[name]
    name_info = name + ' ' + data['nodes'][i]['version']
    nodes_data.append({"name": name_info, "id": data['nodes'][i]['id']})
    if data['nodes'][i]['label'][0] == 'api':
        api_link_num.append({"id": data['nodes'][i]['id'], "name": name_info, "link_num": data['nodes'][i]['links_num']})
    elif data['nodes'][i]['label'][0] == 'database':
        db_link_num.append({"id": data['nodes'][i]['id'], "name": name_info, "link_num": data['nodes'][i]['links_num']})
    elif data['nodes'][i]['label'][0] == 'hardware':
        hw_link_num.append({"id": data['nodes'][i]['id'], "name": name_info, "link_num": data['nodes'][i]['links_num']})
    elif data['nodes'][i]['label'][0] == 'library':
        lib_link_num.append({"id": data['nodes'][i]['id'], "name": name_info, "link_num": data['nodes'][i]['links_num']})
    elif data['nodes'][i]['label'][0] == 'operating_system':
        os_link_num.append({"id": data['nodes'][i]['id'], "name": name_info, "link_num": data['nodes'][i]['links_num']})
    elif data['nodes'][i]['label'][0] == 'programming_language':
        pl_link_num.append({"id": data['nodes'][i]['id'], "name": name_info, "link_num": data['nodes'][i]['links_num']})
    elif data['nodes'][i]['label'][0] == 'software':
        sw_link_num.append({"id": data['nodes'][i]['id'], "name": name_info, "link_num": data['nodes'][i]['links_num']})
    elif data['nodes'][i]['label'][0] == 'tool':
        tool_link_num.append({"id": data['nodes'][i]['id'], "name": name_info, "link_num": data['nodes'][i]['links_num']})
    elif data['nodes'][i]['label'][0] == 'driver':
        driver_link_num.append({"id": data['nodes'][i]['id'], "name": name_info, "link_num": data['nodes'][i]['links_num']})
    elif data['nodes'][i]['label'][0] == 'runtime':
        runtime_link_num.append({"id": data['nodes'][i]['id'], "name": name_info, "link_num": data['nodes'][i]['links_num']})
    elif data['nodes'][i]['label'][0] == 'application':
        application_link_num.append({"id": data['nodes'][i]['id'], "name": name_info, "link_num": data['nodes'][i]['links_num']})

# add label information
for i in range(len(labels)):
    nodes_data.append({"name": labels[i]})  

# sort the link number and store only the top 5
sorted_api_link_num = sorted(api_link_num, key=lambda x: x['link_num'], reverse=True)[:5]
sorted_db_link_num = sorted(db_link_num, key=lambda x: x['link_num'], reverse=True)[:5]
sorted_hw_link_num = sorted(hw_link_num, key=lambda x: x['link_num'], reverse=True)[:5]
sorted_lib_link_num = sorted(lib_link_num, key=lambda x: x['link_num'], reverse=True)[:5]
sorted_os_link_num = sorted(os_link_num, key=lambda x: x['link_num'], reverse=True)[:5]
sorted_pl_link_num = sorted(pl_link_num, key=lambda x: x['link_num'], reverse=True)[:5]
sorted_sw_link_num = sorted(sw_link_num, key=lambda x: x['link_num'], reverse=True)[:5]
sorted_tool_link_num = sorted(tool_link_num, key=lambda x: x['link_num'], reverse=True)[:5]
sorted_driver_link_num = sorted(driver_link_num, key=lambda x: x['link_num'], reverse=True)[:5]
runtime_link_num = sorted(runtime_link_num, key=lambda x: x['link_num'], reverse=True)[:5]
application_link_num = sorted(application_link_num, key=lambda x: x['link_num'], reverse=True)[:5]


search_data = {'nodes': nodes_data}
linkNum_data = {'api': sorted_api_link_num, 
                'database': sorted_db_link_num, 
                'hardware': sorted_hw_link_num, 
                'library': sorted_lib_link_num, 
                'operating_system': sorted_os_link_num, 
                'programming_language': sorted_pl_link_num, 
                'software': sorted_sw_link_num, 
                'tool': sorted_tool_link_num,
                'driver': sorted_driver_link_num,
                'runtime': runtime_link_num,
                'application': application_link_num}

# with open('/Users/zhouzihan/Desktop/visual_kg/public/data.json', 'w') as f:
#     json.dump(search_data, f, indent=4)
with open('/Users/lexiezhou/Desktop/Visual_KnowledgeGraph/client/src/data/linkNum_data.json', 'w') as f:
    json.dump(linkNum_data, f, indent=4)
