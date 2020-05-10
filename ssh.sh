#!/bin/sh

REMOTE=api-endpoint
REMOTE_HOST=157.245.205.223

SSH_REMOTEPORT=22
SSH_LOCALPORT=10022

TUNNEL_REMOTEPORT=5000
TUNNEL_LOCALPORT=5000

createTunnel() {
    /usr/bin/ssh -f -N  -L$SSH_LOCALPORT:127.0.0.1:$SSH_REMOTEPORT -R$TUNNEL_LOCALPORT:127.0.0.1:$TUNNEL_REMOTEPORT $REMOTE
    if [[ $? -eq 0 ]]; then
        echo Tunnel to $REMOTE created successfully
    else
        echo An error occurred creating a tunnel to $REMOTEHOST RC was $?
    fi
}

## Run the 'ls' command remotely.  If it returns non-zero, then create a new connection
/usr/bin/ssh -p $SSH_LOCALPORT -i /home/pi/.ssh/id_rsa root@localhost ls >/dev/null 2>&1
if [[ $? -ne 0 ]]; then
    echo Creating new tunnel connection
    createTunnel
fi
