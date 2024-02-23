# Uptime Kuma on Ubuntu

## Disable IPv6 via GRUB
```
sudo su -
cp /etc/default/grub /etc/default/grub.backup
sed -ie '/GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"/s//GRUB_CMDLINE_LINUX_DEFAULT="ipv6.disable=1 quiet splash"/' /etc/default/grub
sed -ie '/GRUB_CMDLINE_LINUX=""/s//GRUB_CMDLINE_LINUX="ipv6.disable=1"/' /etc/default/grub
grep ipv6.disable /etc/default/grub
diff /etc/default/grub /etc/default/grub.backup
update-grub
reboot
```

### Install NodeJS, PM2 & Uptime Kuma
```
sudo apt update
sudo apt install nodejs

git clone https://github.com/louislam/uptime-kuma.git
cd uptime-kuma
npm run setup

#optional, test if server starts up
#node server/server.js

#run in the background using PM2
sudo npm install pm2 -g && pm2 install pm2-logrotate
pm2 start server/server.js --name uptime-kuma
pm2 save && pm2 startup
sudo env PATH=$PATH:/usr/bin /usr/lib/node_modules/pm2/bin/pm2 startup systemd -u ubuntu --hp /home/ubuntu
sudo reboot
```

### Verify Uptime Kuma is running
Use curl for a HTTP HEAD request

Should return a redirect 302 to the dashboard
```
curl -I http://uptimekuma01:3001 2>/dev/null | head -n 1 | awk '{print $2}'
```

Should return a 200 for the dashboard
```
curl -I http://uptimekuma01:3001/dashboard 2>/dev/null | head -n 1 | awk '{print $2}'
```

### Setup the admin password
Goto http://uptimekuma01:3001. Create your admin account following the prompts

# References
Uptime Kuma by Louis Lam [https://github.com/louislam/uptime-kuma]


