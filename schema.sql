drop table if exists users;
    create table users (
    id integer primary key autoincrement,
    Email text not null,
    Shuttletime TIME not null
);