use finalguirao;

create table people(
	id int primary key auto_increment,
	name varchar(255) not null,
	first_surname varchar(255) not null,
	last_surname varchar(255) not null,
	birth_date date not null
);

