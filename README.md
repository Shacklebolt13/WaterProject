# Welcome to StackEdit!

To use the code on the server, follow the steps below:

1. Pull the code to the server:
		 
    ```git pull https://github.com/Shacklebolt13/WaterProject```
2. Install Python 3.9.2:

    ```sudo apt install python3.9.2-full```

3. Create a Virtual Environment:
   
    ```python3 -m venv venv```

4. Activate the Virtual Environment:
 
    ```source  venv/bin/activate```

5. Install the dependencies:

    ```pip install -r requirements.txt```

6. Create service files and nginx config:

7. Restart Nginx Daemon and reload systemctl
   
    ```sudo systemctl reload
    sudo service waterProject start
    sudo service nginx restart```


