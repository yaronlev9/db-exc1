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
  color varchar(100) primary key
);

create table athlete(
  id integer,
  tname varchar(100),
  gname char(11),
  name varchar(100) unique not null,
  sex char(1) not null check(sex = 'M' or sex = 'F'),
  primary key(id, tname, gname),
  foreign key(tname) references team(name) on delete cascade,
  foreign key(gname) references game(name) on delete cascade
);

create table plays(
  id integer,
  tname varchar(100),
  gname varchar(100),
  ename varchar(100),
  age integer check(age > 0),
  height integer check(height > 0),
  weight integer check(weight > 0),
  color varchar(6) check(color = 'Bronze' or color = 'Silver' or color = 'Gold' or color = ''),
  primary key(id, tname, gname, ename),
  foreign key(id) references athlete(id) on delete cascade,
  foreign key(tname) references team(name) on delete cascade,
  foreign key(gname) references game(name) on delete cascade,
  foreign key(ename) references event(name) on delete cascade
);




