
# step to set up node

prequisition #1:
  - Prepare 4 config folder with files (config.docker, genesis.block, node(n).priv, node(n).pub, root@sorakh.priv, root@sorakh.pub)
  - the differentiation between these 4 folders is node(n).pub and node(n).priv

configuration #2: 
  - config genesis block 
      - adding peer to of all node with address(container name with default port 10001 from config.docker file) 
        and peer key( node(n) public key )
      - create default domain (sorakh)
      - create default asset (khr and usd with domain sorakh)
      - create root user (with root@sorakh.pub key)
      - append admin and money_creator role to root user( user role is already appended by default domain role)
      
  - create docker file with postgres
  - mount volume with any host machine folder to store block



# Deployment 

```docker-compose up -d```

# Install Server Dependency
  Note: you must have python 3 install your machine
  - set up Iroha module
```pip3 install -r requirement.txt --user```

#  Run Server
```python3 app.py```
 Note: only three default account supported (root@sorakh, alice@sorakh, bob@sorakh)




