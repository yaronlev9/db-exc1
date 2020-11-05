create table team(
  name varchar(100) primary key,
  noc char(3) not null
);

create table game(
  name varchar(100) primary key,
  year char(4) not null,
  season char(6) not null,
  city varchar(100) not null,
  check(season = 'Summer' or season = 'Winter')
);

create table event(
  name varchar(100) primary key,
  sport varchar(100) not null
);

create table medal(
  place varchar(6) primary key check(place = 'Bronze' or place = 'Silver' or place = 'Gold')
);

create table athlete(
  id integer not null,
  tname varchar(100) not null,
  gname varchar(100) not null,
  name varchar(100) not null,
  sex char(1) not null check(sex = 'M' or sex = 'F'),
  primary key(id, tname, gname),
  foreign key(tname) references team(name) on delete cascade,
  foreign key(gname) references game(name) on delete cascade
);

create table plays(
  id integer not null,
  tname varchar(100) not null,
  gname varchar(100) not null,
  ename varchar(100) not null,
  age integer check(age > 0),
  height float check(height > 0),
  weight float check(weight > 0),
  place varchar(6) check(place = 'Bronze' or place = 'Silver' or place = 'Gold' or place = ''),
  primary key(id, tname, gname, ename),
  foreign key(id, tname, gname) references athlete(id, tname, gname) on delete cascade,
  foreign key(ename) references event(name) on delete cascade
);




