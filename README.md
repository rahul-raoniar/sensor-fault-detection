# sensor-fault-detection
Problem statement


-- Create a setup.py file
-- (run command) python setup install setup.py

-- add -e . inside requirements.txt
<!-- 
# add the -e . inside requirements.txt
# find and run setup file 
# Then run packages = find_packages()
# Then it find the sensor folder (it is a package as it contains __init__.py -->

-- install using: pip install -r requirements.txt

##############################
# folder structure
#############################

--pipeline: model building pipelines

- cloud storage: for could storage functioanlities

-- components: 

-- configuration: storing all connections to cloud services

-- constant: Various model component (database name, file name that does not change)

-- data access: to access the data base (load data from mongodb)

-- entity: to define the input and output of ml components (ML artifact)
--> it contains artifact_entity.py
--> it also need a config_entity.py

-- ml: for storing code related to custom ml codes (accuracy, feature engineering)

--> create a logger file to query log
--> exception file to log exception


<!-- Artifact in ML: An artifact is a machine learning term that is used to describe the output created by the training process. Output could be a fully trained model, a model checkpoint, or a file created during the training process. -->


