### A Basic Blockchain with python & FastAPI based backend API without any database connection.

### How to use?

- Clone the Repo using: `git clone https://github.com/sakatazizkhan/blockchain-fastapi`
- Change Directory: `cd blockchain-fastapi`
- Install Dependencies: `pip install -r requirements.txt`
- Run the Server: `uvicorn server:app --port 8000 --reload`
- You can access the API using: `http://localhost:8000`
- For API doc use: `http://localhost:8000/docs`

### How to Deploy on EC2 using NGINX?
- Start Docker on your machine
- Use command: `sudo docker-compose up`
https://lcalcagni.medium.com/deploy-your-fastapi-to-aws-ec2-using-nginx-aa8aa0d85ec7