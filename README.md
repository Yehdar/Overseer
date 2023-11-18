# Overseer
## Abstract
Monitoring app that checks CPU and memory utilization
<p align="center"><img src="https://github.com/Yehdar/overseer/blob/main/demo/demo.png" width="80%"></p>

### Technologies Used
AWS (ECR, boto3, EKR), Docker, Python, Flask, JavaScript, HTML, CSS

<hr> 
Configuration
## Configuration
You can run this project in one of two ways.

**With Docker**

1. Clone the repository to your machine

       $ git clone https://github.com/Yehdar/Overseer.git
       
2. Change into the directory

       $ cd overseer

3. After turning on Docker, run this command first

       $ docker build -t file-repo .

4. After that command has completed, run this command next

       $ docker run -p 5000:5000 --name overseer file-repo

5. The server should now be started, navigate to `http://localhost/` in your browser and try not to break anything!

**Without Docker**

1. It is recommended you send up a virtual environment (but completely optional)
       
       $ virtualenv env
       $ source env/bin/activate

2. Install dependencies

       $ pip3 install -r requirements.txt

1. Start the server (be in the root directory, not in `src/`)

       $ python3 app.py
       
2. The server should now be started, navigate to `http://localhost:5000` in your browser and try not to break anything!

3. Note - if on Windows and not using Docker, you may need to go into `src/main.py` and change `app.run(host='0.0.0.0')` to `app.run(host='127.0.0.1')`
