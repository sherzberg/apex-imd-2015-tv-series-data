
drop table if exists episode;
drop table if exists tv_series;

create table tv_series (
	id int(10) not null,
    name varchar(255) not null,
    PRIMARY KEY (id)
);

create table episode (
	id int(10) not null,
    number_in_season int not null,
    title varchar(255) not null,
    season int not null,
    tv_series_id int,
    PRIMARY KEY (id),
    FOREIGN KEY (tv_series_id) REFERENCES tv_series(id)
);

