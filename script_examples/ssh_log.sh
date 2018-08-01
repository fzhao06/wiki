#!/bin/expect -f
set 1 [lindex $argv 0]
set 2 [lindex $argv 1]
set timeout 60
#spawn ssh $1@$2
#xpect "assword:" { send "scaleflux\r" }
#expect "# " { send "mkdir -p .ssh\r" } 
#expect "# " { send "exit\r" }
spawn scp .ssh/id_rsa.pub $1@$2:~/id_rsa.pub
expect {
  "(yes/no" { 
    send "yes\r" 
    exp_continue
  } 
  "assword:" { 
    send "scaleflux\r" 
  } 
}
expect { "$ " "# " }
spawn ssh $1@$2
expect "assword:" { send "scaleflux\r" }
expect "# " { send "mkdir -p ~/.ssh\r" }
expect "# " { send "mv -f ~/id_rsa.pub .ssh\r" }
expect "# " { send "cat .ssh/id_rsa.pub >> .ssh/authorized_keys\r" }
expect "# "
#send  "cat .ssh/id_rsa.pub >> .ssh/authorized_keys\r"
