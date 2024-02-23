# Uptime Kuma on Ubuntu via Multipass and MacOS

## Multipass

### Install Multipass
```
brew install --cask multipass
```

### Create Uptime Kuma Instance with Mulitpass
```
multipass launch --name uptimekuma01 --memory 1G --disk 5G --network en1
```

### Apply changes to Ubuntu via Multipass exec
```
multipass exec uptimekuma01 -- bash
```

