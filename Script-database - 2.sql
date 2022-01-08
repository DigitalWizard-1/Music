drop table Si_Al_Buffer;
drop table Sb_Tr_Buffer;
drop table Ge_Si_Buffer;
drop table Track;
drop table Album;
drop table Sbornik;
drop table Genre;
drop table Singer;


create table if not exists Genre (
	id serial primary key,
	title varchar(40) unique not null
);

create table if not exists Singer (
	id serial primary key,
	name_singer varchar(80) unique not null
);

create table if not exists Ge_Si_Buffer (
	genre_id int references Genre(id),
	singer_id int references Singer(id),
	constraint GS primary key (genre_id, singer_id)
);

create table if not exists Album (
	id serial primary key,
	name_album varchar(80) not null,
	year_album int
);

create table if not exists Si_Al_Buffer (
	singer_id int references Singer(id),
	album_id int references Album(id),
	constraint SA primary key (singer_id, album_id)
);

create table if not exists Sbornik (
	id serial primary key,
	name_sbornik varchar(80) not null,
	year_sbornik int
);

create table if not exists Track (
	id serial primary key,
	name_track varchar(80) not null,
	duration int,
	album_id int references Album(id)	
);

create table if not exists Sb_Tr_Buffer (
	sbornik_id int references Sbornik(id),
	track_id int references Track(id),
	constraint ST primary key (sbornik_id, track_id)
);


