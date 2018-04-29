create user if not exists 'finalguirao'@'finalguirao'
    identified by 'finalguirao';

create schema if not exists finalguirao;

grant all privileges on finalguirao.* to 'finalguirao'@'localhost';

