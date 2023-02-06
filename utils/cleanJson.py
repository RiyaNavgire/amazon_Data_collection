import json
from data_trials.exception import DataTrialException
from data_trials.logger import logger
from data_trials.entity.config_entity import DataIngestionConfig
import sys



class cleanJson():

    def cleanJsonfile():
        try:
            file_name = "D://MLProjectNeuron//ny2019jan.json"
        
            with open(file_name, 'r', encoding='utf-8') as f:
             my_list = json.load(f)

            y_objects = []
    
            for key in my_list.items():
            # print (str(key)+'->'+str(value))
                if("response" in key):
                    l_1 = list(my_list.values())[1]
                for k,v in enumerate(l_1):
                    if("0" in str(k)):
                        l_2 = list(l_1.values())[0]
                        y_objects.append(l_2)              
                        break
        
    
            new_file_name = 'D://MLProjectNeuron//modified.json'

            with open(new_file_name, 'w', encoding='utf-8') as f:
                for k,v in enumerate(y_objects):
                    f.write(str(v))
            f.close() 
        
        except Exception as e:
            raise DataTrialException(e, sys)