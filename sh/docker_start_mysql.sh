docker run --name mysql-free -v mysql_data:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=mysql123 -d mysql --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
