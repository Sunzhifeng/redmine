drop database if exists redmine;

create database redmine;

use redmine;

grant select, insert, update, delete on redmine.* to 'root@localhost' identified by '123456';

create table users (
    `_id` varchar(50) not null,
    `name` varchar(50) not null,
    `password` varchar(50) not null,
    `admin` bool not null,
    `email` varchar(50) not null,
    `created_at` real not null,
    unique key `idx_name` (`name`),
    unique key `idx_email` (`email`),
    key `idx_created_at` (`created_at`),
    primary key (`_id`)
) engine=innodb default charset=utf8;

create table bugs (
    `_id` varchar(50) not null,
    `num` integer not null,
    `title` varchar(200) not null,
    `description` mediumtext,
    `submitter_id` varchar(50) not null,
    `submitter_name` varchar(50) not null,
    `status` varchar(50) not null,
    `found_in` varchar(200),
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`_id`)
) engine=innodb default charset=utf8;

create table improvements (
    `_id` varchar(50) not null,
    `num` integer not null,
    `title` varchar(200) not null,
    `description` mediumtext,
    `submitter_id` varchar(50) not null,
    `submitter_name` varchar(50) not null,
    `status` varchar(50) not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`_id`)
) engine=innodb default charset=utf8;

create table features(
    `_id` varchar(50) not null,
    `num` integer not null,
    `title` varchar(200) not null,
    `target_sprint` mediumtext,
    `description` mediumtext,
    `submitter_id` varchar(50) not null,
    `submitter_name` varchar(50) not null,
    `status` varchar(50) not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`_id`)
) engine=innodb default charset=utf8;

create table ticketings(
    `_id` varchar(50) not null,
    `ticket_id` varchar(50) not null,
    `assignee_id` varchar(50) not null,
    `assignee_name` varchar(50) not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`_id`)
) engine=innodb default charset=utf8;

