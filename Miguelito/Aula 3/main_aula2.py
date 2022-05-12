from logging import exception
from services.IO_services.exportation_services import ExportationServices
from services.yaml_services import YamlServices
from services.data_services import DataServices
from services.etl_services import Etl
from services.convertion_services import ConvertionServices
from services.IO_services.importation_services import ImportationServices

for x in range(0,20):
    print('---')   

# Importing YAML
yaml_file = ImportationServices.import_yaml_config()

# Validate YAML Filters and Exportation type
yaml_file = YamlServices.filter_validation(yaml_file)

# OPEN CSV FILES
sci = ImportationServices.read_csv_file('project_files/imports/ranking_files/scimagojr 2020.csv')
jcs = ImportationServices.read_csv_file('project_files/imports/ranking_files/jcs_2020.csv')
original_csv = ImportationServices.read_csv_file('project_files/exports/csv_data.csv')


# SCI ETL
sci=Etl.sci_etl(sci)
# print(sci)


# JCS ETL
jcs=Etl.jcr_etl(jcs)
# print(jcs)

# CSV ETL 
original_csv=Etl.create_upper_title(original_csv,'Book Title/Journal')
# print(original_csv)


# MERGING AND ETL
merged = Etl.merge_etl(sci,jcs,original_csv)


# APPLY FILTERS 
print(f'Shape before filtering: {merged.shape}')
merged=DataServices.filter_values(yaml_file['filter_options'][0],merged)
print(f'Shape after filtering: {merged.shape}\n')

# print(merged.columns)
# print(merged['Year'])
# print(merged[['Year','JCS_FACTOR']])
# print(merged['JCS_FACTOR'])
print(merged[['Year','JCS_FACTOR','SCI_FACTOR']])
print()
# print(merged['SCI_FACTOR'])


# CONVERT CSV TO DICT 
dict_list=ConvertionServices.convert_csv_to_dict_list(merged)

# EXPORTATION 
exportation_type=yaml_file['exportation_type'][0]['type']
match exportation_type: 

  case 'csv': 
    ExportationServices.export_csv(merged,'project_files/exports/ranking_files/')
    print('Successful exporting to csv\n')

  case 'json':
    json_file=ConvertionServices.convert_dict_to_json(dict_list)
    ExportationServices.export_json(json_file,'project_files/exports/ranking_files/')
    print('Successful exporting to json\n')
 
  case 'yaml':
    yaml_export_file=ConvertionServices.convert_dict_to_yaml(dict_list)
    ExportationServices.export_yaml(yaml_export_file,'project_files/exports/ranking_files/')
    print('Successful exporting to yaml\n')
  
  case 'xml':
   xml_file=ConvertionServices.convert_dict_xml(dict_list)
   ExportationServices.export_xml(xml_file,'project_files/exports/ranking_files/')
   print('Successful exporting to xml\n')
  
  case _: 
      raise exception
