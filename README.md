# odoo_14_hebrew
VScode 

# Debug Odoo in container: 

Link: https://dev.to/kerbrose/how-to-remote-debugging-odoo-docker-images-python-based-framework-4o2h 

# Original postgress image is used 

docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name hebrew_db_14 postgres:13 

docker image build -t hebrew_learning_odoo_14:latest . 

# Start without debug: 

docker run --mount type=bind,source="$(pwd)"/hebrew_learning,target=/mnt/extra-addons/hebrew_learning -p 8069:8069 --link hebrew_db_14:db --name hebrew_odoo_14 -t pythongeek88/hebrew_learning_odoo_14:latest /usr/bin/python3 /usr/bin/odoo --db_user=odoo --db_host=db --db_password=odoo 

# Start with debug: 

docker run -p 8888:3001 -p 8879:8069 --link hebrew_db_14:db --name hebrew_odoo_14_debug -t pythongeek88/hebrew_learning_odoo_14:latest /usr/bin/python3 -m debugpy --listen 0.0.0.0:3001 /usr/bin/odoo --db_user=odoo --db_host=db --db_password=odoo 

Connect and use debug - .vscode/ launch.json: 

{ 

    "version": "0.2.0", 

    "configurations": [ 

        { 

            "name": "Odoo: Attach for debug", 

            "type": "python", 

            "request": "attach", 

            "port": 8879, 

            "debugServer": 8888, 

            "host": "localhost", 

            "pathMappings": [ 

                { 

                    "localRoot": "${workspaceFolder}", 

                    "remoteRoot": "/mnt/extra-addons", //path to custom addons inside docker 

                } 

            ], 

            "logToFile": true 

        } 

    ] 

} 
