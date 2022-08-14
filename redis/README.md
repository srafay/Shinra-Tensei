# Remote Dictionary Server (Redis)
Made this subdirectory to record commonly used Redis commands that I come across.

## What is Redis
Redis is an in-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker, with optional durability. Redis supports different kinds of abstract data structures, such as strings, lists, maps, hashes, etc.

## How to install Redis

### Linux
- For linux its easy, download from the [official website](https://redis.io/download#installation).

### Windows
For Windows, there are options. 
- [Memurai](https://www.memurai.com/) is a version of Redis ported to Windows. Its free for development. After installation, it creates a Windows Service which runs the Redis server in background. It uses almost the same configuration options and commands as Redis (redis.conf). 
  - It needs to be restarted every 10 days since its a free version.

- Install Redis using Windows Subsystem for Linux (**WSL** / **WSL2**). WSL is a compatibility layer which allows Linux packages and binaries to run on Windows OS. Virtualization needs to be enabled from BIOS settings to be able to install and use WSL.
  - Install WSL by following the [documentation](https://docs.microsoft.com/en-us/windows/wsl/install)
  - Download a Linux distribution from Windows Store (such as Debian or Ubuntu)
  - Now you have Linux installed, download and run Redis normally as you would do on a Linux OS.

- Run Redis in a container through Docker.
  - Docker needs to be installed on Windows first, which itself requires virtualization to be enabled and WSL/WSL2 installed.
    - [Docker installation guide](https://docs.docker.com/desktop/install/windows-install/)
  - [Download Redis image](https://hub.docker.com/_/redis/) from Docker Hub.
  - Start a Redis instance
    - ```docker run --name my-redis-server -d redis```
    
## Connecting to Redis
- Connect to Redis server through command line using:
  - If its not password protected:
    - ```redis-cli```
  - If the server is password protected (defined in requirepass option -> redis.conf)
    - ```redis-cli -a yourPassword```
    
- Connect to Redis server programatically
  - Check the [available clients list](https://redis.io/docs/clients/) for options.
