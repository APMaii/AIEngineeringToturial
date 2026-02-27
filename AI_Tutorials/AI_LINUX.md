# Linux Tutorial

Khob inja mikhaym rajebe Linux harf bznim k asan chie?
Linux yek Operating system(OS) has yani mese windows , mese macos ke modiriate mikone hardware(CPU, MEMORY, DISK) va software shomaro.
---
---

**Linux** open-source has va hamchnin **modular** , **customizable** va **command-driven** hast.

aval bayad bedonim **Unix** chie
Unix dar asl yek original OS bode ke sale 1970 sakhte shode
Linux hamon Unix-like oS has va shabihe Unixe ama free va jadide. 
baghie Unix-like system ha mese MacOS hastand.

## Chera Linux?
- choon aksare, servra , supercomputer ha , embedded device ha az linux support mikonan. 
- paydario amn bodan
- balatarin control ro mdie roo systemt

## Kernel chie?
kernel yani core (haste) e linux has k sohbat mikone ba hardware (sakht afzaret)

**distribution (distro)** yani kernel + software + package management va ma ziad darim mese ubuntu, debian, fedora , arch ,...

yani bebin kernel mesle motore machine. distro : machino badane o hgamechizeshe.

---
---
## Linux File system Basics
khob dar nazar bgir k vaghty varede yek servr mishi bayad shoam yechi dahste bashi mesle terminus va baghie chiza k bsh hastan va ejaze midan to vasl shi va sohbat koni ba kernele linux.

vaghty vared mishi hamechi tooye **linux** file va folder hast.

avalin jaee k hasti **/** hast k behesh migan root directory (ya jae k hamchi az inja shoro mishe) 

hala too haminaj ma folder haye ziadi darim mesle **bin** , **sbin** **usr** , **home** , **etc** , **var** va **tmp** khob ina daghighan chian?

| Folder | Purpose |
|--------|---------|
| `/` | Root directory (everything starts here) |
| `/bin` | Essential command binaries (like ls, cp) |
| `/sbin` | System binaries (for admin, e.g., ifconfig) |
| `/usr` | User programs and libraries |
| `/home` | Home directories for users |
| `/etc` | Configuration files |
| `/var` | Variable files (logs, databases) |
| `/tmp` | Temporary files |


khob daghighan mesle darse [AI_CLI.md](/AI_CLI.md) ma ag bekhaym bbinim kojaeem kafie bzanim

```bsh
pwd
```
behemoon mige kojaeem daghighan

bekhahim harekat konim az **cd** estefade mikonim
```bsh
cd /home/user/Documents
cd ..   # moves to /home/user
cd .    # stays in /home/user/Documents
```


hamchnin mesle tamame CLI in dastoorate bash kar mikone dakhelesh

| Command | Description |
|---------|-------------|
| `ls` | List files |
| `cd` | Change directory |
| `pwd` | Print working directory |
| `cat` | View file contents |
| `rm` | Remove files or directories |
| `mv` | Move or rename files |
| `cp` | Copy files or directories |
| `mkdir` | Create directory |
| `touch` | Create empty file or update timestamp |
| `echo` | Print text or variables to output |
| `grep` | Search for pattern in files or input |
| `find` | Find files by name, type, or other criteria |
| `head` | Show first lines of a file |
| `tail` | Show last lines of a file (e.g. `tail -f` for logs) |
| `less` | View file with scroll (quit with `q`) |
| `chmod` | Change file permissions (read/write/execute) |
| `chown` | Change file owner or group |
| `man` | Show manual page for a command |
| `which` | Show path of a command |
| `exit` | Exit the current shell |


---
---

## Users and permissions
linux **multi-user** hast. 
- root: superuser hast k full system access dare
- normal user : limited permission

khob daghighan mesle windows k shoma mitoni chanta user dashte bashi , aval k varede linux mishi fght **root** hast k b hamchi dastresi dare, ama badesh mitoni user besazi va in user ha **normal user** hastan va khob permission ya dastresishon mahdode ama ag varede oon user shode bashid baraye inek kari koni k fght superuser mitone kone bayad ghable dastoorat o commande khdoetoon **sudo** bezanid
- sudo : temporary root access for commands

#### Package Managers
linux mesle windows fili chizi mesle .exe installer nadare bejas ma yek **package manager** darim k software installation ro handle mikone
- Debian/ubuntu : apt
- Fedora: dnf
- Arch: pacman

hamishe avalesh k mirid too server bayad az dastoore zir bezanid k khode **apt** ro update konid
```bsh
sudo apt update
```

hamchin in **apt** vase in hast k betoonid harchi bekhayd ro install konid mesle dastore zir
```bsh
sudo apt install name_of_tool_you_want
```

baraye mesal
```bsh
sudo apt install git
```

### More details on directories
midonim k jaee k bodim root bod yani **/**  khob hala daghigh tar bekhaym bbinim hamchin jaee hastim

```arduino
/
├── bin
├── etc
├── home
│   └── user
├── usr
└── var
```


| Path | Purpose |
|------|---------|
| `/bin` | Basic commands (everyone can use) |
| `/sbin` | System admin commands (mostly root) |
| `/usr` | Software and libraries (e.g., /usr/bin/git) |
| `/home` | Personal files for each user (/home/alice) |
| `/etc` | System configuration files |
| `/var` | Logs, caches, runtime files |
| `/tmp` | Temporary files |


nokte : **/usr** dar asl narm afzar hast , **/etc** setting hast va **/var** data in motion.


### Usr management
khob hamonto k goftim ma yekseri dastoorat darim k bbinim aslan ch useri hastim idimon chie (che gorohi va ..) 

```bsh
whoami          # see current user
id              # see UID, groups
sudo whoami     # temporarily act as root

```

khob deghat konid k UID 0 yani root, UID 1000+ yani normal users.




--
--
## USER MANAGEMENT
hala ma midonim ama nmidonim chijori bayad user sakht?
aval inke bayar ya root bashid ya ba **sudo** akr konid , yani fgth superuser mitone user bsaze

```bsh
sudo adduser alice
```
ba inakr shoma yek username isazid va hata mitonid password, full name , phon va .. besazid va khob in miad baratoon home directory misaze tooye **/home/alice**


hamchnin ye rahe low-level tar ham dare mesle
```bsh
sudo useradd -m bob  # creates user bob with home folder
sudo passwd bob      # set password for bob
```


## Assigning Users to Groups
mitonim user haro berizim to y grooh. 

injori mitoni check konim groupe e yek user ro
```bsh
groups alice
```

age bekhym yek user ro to yek group berizim
```bsh
sudo usermod -aG sudo alice
```
-ag yani append kon b group



## Switching Users
baraye inke taghir bedid kheyli sade
- su --> switch user (reqwuire password)
- sudo -i --> become root shell
- exit --> go back to your normal user

## Permissions
har file 3 no permission dare va 3 daste 
yani 3 type of permission baraye 3 categories.

- type : r(read) , w(write), x(excute)
- categoris: owner, group , other

vaghty shoma dastore zir ro bznid
```bsh
ls -l myfile.txt
```

shoma ino mibinid
```bsh
-rw-r--r-- 1 alice users 123 Feb 12 12:00 myfile.txt
```
in yani
- rw- -->ownr can read/write
- r-- -->yani group mitone fght bkhoone
- r-- --> other ham fgth mitone bekhone


baraye taghire permission shoma aval bayad tooye khode **root** bashid .
oon file ya folderi k bekhayd ro mitonid rahat taghir bdid masalan

```bsh
chmod +x script.sh  # make file executable
chmod 755 file      # set rwx for owner, r-x for group & others
```

ya agar bekhayd ownership ro taghir bdid
```bsh
sudo chown bob file.txt  # change owner to bob
```

### DELETING USERS
```bsh
sudo deluser alice
```

ya age mikjhayd ham user dleet she ham home directory k dare
```bsh
sudo deluser --remove-home alice  
```

#### Recap for user management

| Task | Command / concept |
|------|-------------------|
| **Create user** (interactive) | `sudo adduser alice` — creates user + home in `/home/alice` |
| **Create user** (low-level) | `sudo useradd -m bob` then `sudo passwd bob` |
| **Check user's groups** | `groups alice` |
| **Add user to group** | `sudo usermod -aG sudo alice` (`-aG` = append to group) |
| **Switch user** | `su` (switch user, needs password), `sudo -i` (become root), `exit` (go back) |
| **Permissions** | `r` read, `w` write, `x` execute — for **owner**, **group**, **other** |
| **View permissions** | `ls -l myfile.txt` → e.g. `-rw-r--r--` (owner rw, group r, others r) |
| **Change permissions** | `chmod +x script.sh`, `chmod 755 file` |
| **Change owner** | `sudo chown bob file.txt` |
| **Delete user** | `sudo deluser alice` |
| **Delete user + home** | `sudo deluser --remove-home alice` |

**Rule:** Creating users, changing ownership, and deleting users require **root** or **sudo**.


---
---
## **Package Management and Software in Linux**

hamoontor k goftim ma ye tool dairm bename **apt** baraye debian/ubuntu ya hata **dnf** va **pacman** vase distru haye dige ke bahash mitonim download konim .

khob avalin kari k varede server mishid konid ine ya hata baraye ehtiat ghabel nasbe har goone tool
```bsh
sudo apt update      # refresh package list
sudo apt upgrade     # upgrade installed packages
```

### Installing Software
shoma hargone tool ya abzari ro mitonid nasb konid, baraye mesal fek konid ma mikhyam **firefox** ro bahash kar konim

search koni ye package ro
```bsh
apt search firefox
```

age install mikhay koni
```bsh
sudo apt install firefox
```

removing package
```bsh
sudo apt remove firefox       # removes software but keeps config files
sudo apt purge firefox        # removes software + config files

```

clean up unsusd packages
```bsh
sudo apt autoremove

```

*advance tare in topic* : vaghty shoma yek tool ya abzar ro zakhire mikonid koja zakhire mishe?

| Path | Purpose |
|------|---------|
| `/usr/bin` | Normal software executables (ls, git) |
| `/usr/sbin` | Admin software (ifconfig, systemctl) |
| `/etc` | Config files |
| `/var` | Logs / data used by software |

# Recap

| Task | Command |
|------|---------|
| Update repos | `sudo apt update` |
| Upgrade software | `sudo apt upgrade` |
| Install software | `sudo apt install package_name` |
| Remove software | `sudo apt remove package_name` |
| Remove unused dependencies | `sudo apt autoremove` |
| Search package | `apt search package_name` |
| Show package info | `apt show package_name` |


---
---
### More on CLI that is used in Linux
doroste ke tooye file [AI_CLI.md](/AI_CLI.md) hesabi sohbat kardim ama khobe ye review dahste bashim inja


#### Basic Navigation Commands

| Command | Purpose |
|---------|---------|
| `pwd` | Print current directory |
| `ls` | List files and folders |
| `ls -l` | Detailed list with permissions |
| `cd /path/to/folder` | Change directory |
| `cd ..` | Move up one directory |
| `cd ~` or `cd` | Go to your home directory |
| `tree` | Show folder structure (install via `sudo apt install tree`) |

example
```bsh
cd /usr
ls -l
cd bin
pwd
```

#### File Operations

| Command | Purpose |
|---------|---------|
| `touch file.txt` | Create empty file |
| `mkdir folder` | Create folder |
| `cp source dest` | Copy file/folder |
| `mv old new` | Move/rename file/folder |
| `rm file` | Remove file |
| `rm -r folder` | Remove folder recursively |

#### Viewing File Contents

| Command | Purpose |
|---------|---------|
| `cat file.txt` | Show file content |
| `less file.txt` | View long files (scrollable) |
| `head file.txt` | Show first 10 lines |
| `tail file.txt` | Show last 10 lines |
| `tail -f file.log` | Monitor logs live |

#### Wildcards and Patterns

| Pattern | Meaning |
|---------|---------|
| `*` | Matches anything |
| `?` | Matches one character |
| `[abc]` | Matches any character in brackets |

```bsh
ls *.txt         # list all txt files
rm file?.txt     # delete file1.txt, file2.txt, etc.
```

#### Pipes and Redirection
Pipe | → send output of one command as input to another
```bsh
ls -l | less      # list files, view scrollable
cat file.txt | grep "error"  # search for "error"

```
Redirection > and >>
> → overwrite file
>> → append to file

```bsh
echo "Hello" > file.txt   # write
echo "World" >> file.txt  # append
```

Redirect errors 2>

```bash
ls /nonexistent 2> error.log
```


#### Useful Command Combinations
```bsh
ps aux | grep firefox     # find processes named firefox
df -h | grep /dev/sda     # check disk usage of a partition

```

----
----
----
## Processes, System Monitoring, and Services

process chie? b runn shdoan yek program migim process. har command tooye linux yek process misaze
process ha da rlinux
- PID --> process id
- owner
- state : running,sleeping,stopped, etc

#### viewing process
ps → snapshot of processes
```bsh
ps aux               # show all processes with details
ps -u alice          # processes of user alice

```

top → real-time interactive view
```bsh
top
```
Shows CPU, memory, and running processes
Press q to quit
htop → nicer top (requires install: sudo apt install htop)



### Controlling Processes

| Task | Command |
|------|---------|
| Kill process by PID | `kill 1234` |
| Kill forcefully | `kill -9 1234` |
| Stop process | `kill -STOP 1234` |
| Resume process | `kill -CONT 1234` |

background and foregound
```bsh
command &       # run in background
fg %1           # bring job #1 to foreground
jobs            # list background jobs

```

#### Monitoring System Resources

- CPU & Memory
```bsh
top / htop
free -h          # memory usage
vmstat 1         # live system stats every 1 second

```

- disk usage
```bsh
df -h            # disk space usage
du -sh folder/   # folder size
```

- network
```bsh
ifconfig         # network interfaces
ip a             # newer alternative to ifconfig
ping google.com  # check connectivity
netstat -tuln    # listening ports

```



----
----
----


## SYSTEMD , Linux Service

systmd dar asl hamon init system ya servic manager  hast k tavasote linux distros estefade mish. in start mikoen process ro vaghty system boot hast va ejaze mide k run bashan va safe stop mikone.

mohem tarin componente yek systemd
- unit -> configuration file has ke describe mikone oon service ro 
- seervice unit --> programi hast k systemd managesh mikone


shoma aval bayad bedonid systemd kojas. yek jaee hast bename **/etc/systmd/system** ag brid oonja 
```bsh
cd /etc/systemd/system
```

ag ls bznid mibinid yekseri file default has k taheshon .service daran, khob inja shoma mitonid service khdoeton ro easy besazid masalan

```bsh
vim myapp.service
```

yani shoma hamchin chzii sakhtid dar **/etc/systemd/system/myapp.service**

```ini
[Unit]
Description=My Test Service
After=network.target

[Service]
Type=simple
User=alice
ExecStart=/usr/bin/python3 /home/alice/myapp.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

[Unit] → metadata about the service
Description → human-readable description
After → start this service after network.target
[Service] → how to run the program
Type=simple → runs the program directly
User=alice → run as this user
ExecStart → command to run
Restart → restart automatically on failure
[Install] → how the service integrates with system boot
WantedBy=multi-user.target → start at normal boot


masalan yek barnaem kh sade besaz tooye /home/alice/myapp.py choon daghighan in esmie k tooye file configuration ya hamoon .service skahti

```python
# /home/alice/myapp.py
import time
while True:
    with open("/home/alice/log.txt", "a") as f:
        f.write("Service running...\n")
    time.sleep(10)

```


hala vaghty tamom shod inkarie k hamishe mikonan
reload mikonan khode systemd ro 
```bsh
sudo systemctl daemon-reload
```

badesh shoma bayad ye esmi k barash gzoashti amsalan myapp.service , khob bayad start konid va enable

```bsh
sudo systemctl start myapp
sudo systemctl enable myapp
```
harmoghe khastid statusesho check konid kafie bznid

```bsh
sudo systemctl status myapp

```

harmoghe khastid log bebinid
```bsh
journalctl -u myapp -f
```
hamchinin in loge e zende ro neshon mide,  loge hsitory ro mitonid dakhele /home/alice/log.txt bbinid.

ag harvaght taghrii tooye file appeton dadi , kafie fght service ro restatrt konid

```bsh
sudo systemctl restart myapp
```

hamrogeh ham khastid mitonid disable konid
```bsh
sudo systemctl disable myapp
```

#### Recap

**Concepts**

| Term | Meaning |
|------|---------|
| **systemd** | Init system / service manager: starts processes at boot, runs and stops services |
| **unit** | Configuration file that describes a service (e.g. `myapp.service`) |
| **service unit** | A program that systemd manages (defined by a `.service` file) |

**Where:** Service files go in `/etc/systemd/system/` (e.g. `/etc/systemd/system/myapp.service`).

**`.service` file sections**

| Section | Key options | Purpose |
|---------|-------------|---------|
| `[Unit]` | `Description`, `After=network.target` | Metadata, startup order |
| `[Service]` | `Type=simple`, `User=`, `ExecStart=`, `Restart=on-failure` | How and as whom the program runs |
| `[Install]` | `WantedBy=multi-user.target` | Start at normal boot |

**systemctl commands**

| Task | Command |
|------|---------|
| Reload after editing a unit file | `sudo systemctl daemon-reload` |
| Start service | `sudo systemctl start myapp` |
| Enable at boot | `sudo systemctl enable myapp` |
| Check status | `sudo systemctl status myapp` |
| View live logs | `journalctl -u myapp -f` |
| Restart service | `sudo systemctl restart myapp` |
| Disable at boot | `sudo systemctl disable myapp` |

After changing a `.service` file, run `daemon-reload` then `restart` (or `start`/`enable` as needed).


---
---
---
##Advanced topics
you must compelted

### Intermediate Core
- Command-line tools: grep, awk, sed, cut, find, xargs
- System monitoring: top, htop, ps, free, df, du, vmstat
- File compression and archives (tar, gzip, zip)
- Networking basics: ping, netstat, ss, ifconfig/ip, traceroute
- Process management: jobs, fg, bg, kill, nice, renice
- Logging: /var/log, journalctl


### System Administration
- systemd: units, services, timers, targets
- Cron jobs and scheduling tasks (cron, at)
- Disk management: partitions, LVM, mounting, fstab
- Backup & restore: rsync, tar, snapshots
- Firewalls: ufw, iptables, firewalld
- Kernel tuning: sysctl


### Networking & Servers
- SSH, SCP, SFTP basics
- Port forwarding and tunneling
- System logging & monitoring (syslog, rsyslog, logrotate)
- Installing and managing services: web servers (Apache/Nginx), DBs (MySQL/PostgreSQL), mail servers
- Network troubleshooting: tcpdump, wireshark, netcat


### scripting automation
- Bash scripting fundamentals
- Advanced scripting: loops, conditions, functions
- Command substitution, pipes, redirection
- Automating tasks with scripts & cron


### Security & Advanced Topics
- File encryption & SSH keys
- User and group security hardening
- Firewall & iptables rules
- PAM (Pluggable Authentication Modules)
- Containers: Docker, Podman, LXC
- Virtualization: KVM, QEMU
- Monitoring & alerting: Prometheus, Nagios

### Advanced System Internals
- Process scheduling, signals, jobs
- Memory management & swap
- Linux kernel basics
- System boot process (BIOS → GRUB → init/systemd)
- Advanced networking: bonding, bridging, VLANs




